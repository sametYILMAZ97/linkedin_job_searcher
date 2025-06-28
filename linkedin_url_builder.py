"""
LinkedIn Job Searcher - URL Builder Tool
This application helps you create optimized LinkedIn job search URLs with advanced filtering options.
"""

import urllib.parse
from typing import Optional


class LinkedInURLBuilder:
    """Build optimized LinkedIn job search URLs with customizable parameters."""

    BASE_URL = "https://www.linkedin.com/jobs/search/"

    # Common time filters in seconds
    TIME_FILTERS = {
        "1 hour": 3600,
        "2 hours": 7200,
        "4 hours": 14400,
        "8 hours": 28800,
        "12 hours": 43200,
        "24 hours": 86400,
        "3 days": 259200,
        "1 week": 604800,
        "2 weeks": 1209600,
        "1 month": 2592000,
    }

    # Sort options
    SORT_OPTIONS = {"relevance": "R", "date_posted": "DD"}

    # NOTE: Geographic IDs change frequently and are unreliable
    # This tool now focuses on letting users input their own verified geo IDs
    # To find your correct geo ID:
    # 1. Go to LinkedIn Jobs manually
    # 2. Search for jobs in your desired location
    # 3. Copy the URL and look for geoId=XXXXXX
    # 4. Use that number in the geo ID field

    # We keep a few verified ones, but prefer manual input
    VERIFIED_GEO_IDS = {
        # Only verified, working geo IDs
        "united_states": "103644278",  # Verified working
        "remote": "0",  # For remote jobs
    }

    def __init__(self):
        self.params = {}
        # Add required LinkedIn parameters for proper functionality
        self.params["origin"] = "JOB_SEARCH_PAGE_JOB_FILTER"
        self.params["refresh"] = "true"

    def set_keywords(self, keywords: str) -> "LinkedInURLBuilder":
        """Set job search keywords."""
        if keywords:
            self.params["keywords"] = keywords
        return self

    def set_location(self, location: str) -> "LinkedInURLBuilder":
        """Set job search location."""
        if location:
            self.params["location"] = location
        return self

    def set_geo_id(self, geo_id: str) -> "LinkedInURLBuilder":
        """Set geographic ID for more precise location targeting."""
        if geo_id:
            self.params["geoId"] = geo_id
            # Remove location parameter if geoId is provided (LinkedIn prefers geoId)
            if "location" in self.params:
                del self.params["location"]
        return self

    def set_distance(self, distance: int) -> "LinkedInURLBuilder":
        """Set search radius in miles."""
        if distance and distance > 0:
            self.params["distance"] = str(distance)
        return self

    def set_time_filter(self, time_filter: str) -> "LinkedInURLBuilder":
        """Set time filter for job postings."""
        if time_filter in self.TIME_FILTERS:
            seconds = self.TIME_FILTERS[time_filter]
            self.params["f_TPR"] = f"r{seconds}"
        return self

    def set_custom_time_hours(self, hours: float) -> "LinkedInURLBuilder":
        """Set custom time filter in hours."""
        if hours and hours > 0:
            seconds = int(hours * 3600)
            self.params["f_TPR"] = f"r{seconds}"
        return self

    def set_sort_by(self, sort_by: str) -> "LinkedInURLBuilder":
        """Set sorting option."""
        if sort_by in self.SORT_OPTIONS:
            self.params["sortBy"] = self.SORT_OPTIONS[sort_by]
        return self

    def set_experience_level(self, levels: list[str]) -> "LinkedInURLBuilder":
        """Set experience level filters."""
        # Experience levels: 1=Internship, 2=Entry level, 3=Associate, 4=Mid-Senior level, 5=Director, 6=Executive
        level_map = {
            "internship": "1",
            "entry": "2",
            "associate": "3",
            "mid_senior": "4",
            "director": "5",
            "executive": "6",
        }

        if levels:
            level_codes = [level_map.get(level.lower()) for level in levels if level.lower() in level_map]
            if level_codes:
                self.params["f_E"] = ",".join(level_codes)
        return self

    def set_job_type(self, job_types: list[str]) -> "LinkedInURLBuilder":
        """Set job type filters."""
        # Job types: F=Full-time, P=Part-time, C=Contract, T=Temporary, I=Internship, V=Volunteer, O=Other
        type_map = {
            "full_time": "F",
            "part_time": "P",
            "contract": "C",
            "temporary": "T",
            "internship": "I",
            "volunteer": "V",
            "other": "O",
        }

        if job_types:
            type_codes = [type_map.get(jt.lower()) for jt in job_types if jt.lower() in type_map]
            if type_codes:
                self.params["f_JT"] = ",".join(type_codes)
        return self

    def set_remote_options(self, remote_types: list[str]) -> "LinkedInURLBuilder":
        """Set remote work options."""
        # Remote: 1=On-site, 2=Remote, 3=Hybrid
        remote_map = {"on_site": "1", "remote": "2", "hybrid": "3"}

        if remote_types:
            remote_codes = [remote_map.get(rt.lower()) for rt in remote_types if rt.lower() in remote_map]
            if remote_codes:
                self.params["f_WT"] = ",".join(remote_codes)
        return self

    def set_salary_range(self, min_salary: Optional[int] = None, max_salary: Optional[int] = None) -> "LinkedInURLBuilder":
        """Set salary range filter."""
        if min_salary or max_salary:
            # LinkedIn uses salary base codes
            # This is a simplified version - LinkedIn's actual salary filtering is more complex
            if min_salary:
                self.params["f_SB2"] = str(min_salary)
        return self

    def set_job_id(self, job_id: str) -> "LinkedInURLBuilder":
        """Set current job ID for tracking purposes."""
        if job_id:
            self.params["currentJobId"] = job_id
        return self

    def build_url(self) -> str:
        """Build the complete LinkedIn job search URL."""
        if not self.params:
            return self.BASE_URL

        # URL encode parameters
        query_string = urllib.parse.urlencode(self.params, quote_via=urllib.parse.quote)
        return f"{self.BASE_URL}?{query_string}"

    def get_params_summary(self) -> dict[str, str]:
        """Get a human-readable summary of current parameters."""
        summary = {}

        if "keywords" in self.params:
            summary["Keywords"] = self.params["keywords"]

        if "location" in self.params:
            summary["Location"] = self.params["location"]

        if "distance" in self.params:
            summary["Search Radius"] = f"{self.params['distance']} miles"

        if "f_TPR" in self.params:
            # Convert back from seconds to human readable
            seconds = int(self.params["f_TPR"][1:])  # Remove 'r' prefix
            for time_name, time_seconds in self.TIME_FILTERS.items():
                if time_seconds == seconds:
                    summary["Posted Within"] = time_name
                    break
            else:
                hours = seconds / 3600
                summary["Posted Within"] = f"{hours:.1f} hours"

        if "sortBy" in self.params:
            for sort_name, sort_code in self.SORT_OPTIONS.items():
                if sort_code == self.params["sortBy"]:
                    summary["Sort By"] = sort_name.replace("_", " ").title()
                    break

        return summary

    def reset(self) -> "LinkedInURLBuilder":
        """Reset all parameters."""
        self.params = {}
        return self

    def set_location_by_name(self, location_name: str) -> "LinkedInURLBuilder":
        """
        Set location using name. Now uses text location as fallback since geo IDs are unreliable.
        For best results, use the manual geo ID input field instead.
        """
        if not location_name:
            return self

        location_key = (
            location_name.lower()
            .replace(" ", "_")
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
            .replace("all", "")
            .strip("_")
        )

        # Special mappings for common variations
        location_mappings = {
            "turkey": "turkey",
            "turkey_all": "turkey",
            "türkiye": "turkey",
            "united_states": "united_states",
            "usa": "united_states",
            "us": "united_states",
        }

        # Use mapping if available, otherwise use direct key
        final_key = location_mappings.get(location_key, location_key)

        # Only use verified geo IDs to avoid wrong mappings
        if final_key in self.VERIFIED_GEO_IDS:
            self.set_geo_id(self.VERIFIED_GEO_IDS[final_key])
        else:
            # Use text location - more reliable than wrong geo IDs
            self.set_location(location_name)
        return self


def create_optimized_url(
    keywords: str,
    location: str = "",
    distance: int = 25,
    time_filter: str = "24 hours",
    sort_by: str = "date_posted",
    experience_levels: list[str] = None,
    job_types: list[str] = None,
    remote_options: list[str] = None,
) -> tuple[str, dict[str, str]]:
    """
    Create an optimized LinkedIn job search URL with common settings.

    Returns:
        tuple: (url, parameters_summary)
    """
    builder = LinkedInURLBuilder()

    url = (
        builder.set_keywords(keywords)
        .set_location(location)
        .set_distance(distance)
        .set_time_filter(time_filter)
        .set_sort_by(sort_by)
    )

    if experience_levels:
        url.set_experience_level(experience_levels)

    if job_types:
        url.set_job_type(job_types)

    if remote_options:
        url.set_remote_options(remote_options)

    return url.build_url(), url.get_params_summary()


if __name__ == "__main__":
    # Example usage
    builder = LinkedInURLBuilder()

    # Create a sample optimized URL
    url = (
        builder.set_keywords("python developer")
        .set_location("San Francisco")
        .set_distance(25)
        .set_time_filter("24 hours")
        .set_sort_by("date_posted")
        .set_experience_level(["mid_senior"])
        .set_job_type(["full_time"])
        .set_remote_options(["remote", "hybrid"])
        .build_url()
    )

    print("Generated LinkedIn Job Search URL:")
    print(url)
    print("\nParameters Summary:")
    for key, value in builder.get_params_summary().items():
        print(f"  {key}: {value}")
