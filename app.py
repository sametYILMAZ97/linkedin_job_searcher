"""
Streamlit Web Interface for LinkedIn Job Search URL Builder
"""

import streamlit as st

from linkedin_url_builder import LinkedInURLBuilder


def main():
    st.set_page_config(page_title="LinkedIn Job Search URL Builder", page_icon="🔍", layout="wide")

    st.title("🔍 LinkedIn Job Search URL Builder")
    st.markdown("Create optimized LinkedIn job search URLs with advanced filtering options")

    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("Search Parameters")

        # Basic search parameters
        keywords = st.text_input(
            "Keywords/Job Title",
            placeholder="e.g., Python Developer, Data Scientist, Product Manager",
            help="Enter job title, skills, or keywords to search for",
        )

        # Location selection
        st.subheader("📍 Location")

        location_method = st.radio(
            "Location Method",
            options=["Common Locations", "Custom Location", "Geographic ID"],
            horizontal=True,
            help="Choose how to specify the job location",
        )

        if location_method == "Common Locations":
            common_locations = {
                "Turkey (All)": "turkey",
                "Ankara, Turkey": "ankara",
                "Istanbul, Turkey": "istanbul",
                "Izmir, Turkey": "izmir",
                "Antalya, Turkey": "antalya",
                "United States (All)": "united_states",
                "New York, USA": "new_york",
                "San Francisco, USA": "san_francisco",
                "Los Angeles, USA": "los_angeles",
                "London, UK": "london",
                "Berlin, Germany": "berlin",
                "Paris, France": "paris",
                "Remote": "remote",
            }

            selected_location = st.selectbox(
                "Select Location",
                options=list(common_locations.keys()),
                help="Choose from common locations with precise geo targeting",
            )
            location = common_locations[selected_location]
            geo_id = None

        elif location_method == "Custom Location":
            location = st.text_input(
                "Location",
                placeholder="e.g., San Francisco, Remote, New York",
                help="City, state, country, or 'Remote' for remote positions",
            )
            geo_id = None

        else:  # Geographic ID
            st.warning("⚠️ **Important**: Many pre-set geo IDs are incorrect and show wrong countries!")
            st.info(
                """
            🔍 **How to find your correct geo ID:**
            1. Go to LinkedIn Jobs in your browser
            2. Search for any job in your desired location
            3. Look at the URL and find `geoId=XXXXXX`
            4. Use that number below
            """
            )

            location = ""
            geo_id = st.text_input(
                "Geographic ID",
                placeholder="e.g., enter the exact number from LinkedIn URL",
                help="Find this number from LinkedIn URL: geoId=XXXXXX",
            )

            if geo_id:
                st.success(f"✅ Using geo ID: {geo_id}")
            else:
                st.info("💡 **Tip**: Text location is often more reliable than geo IDs")

        # Job ID (optional)
        job_id = st.text_input(
            "Specific Job ID (Optional)",
            placeholder="e.g., 4185657072",
            help="Optional: Enter a specific LinkedIn job ID to track or reference",
        )

        # Time filter
        st.subheader("⏰ Time Filter")
        time_option = st.radio("Posted within:", options=["Preset times", "Custom hours"], horizontal=True)

        if time_option == "Preset times":
            time_filter = st.selectbox(
                "Time period",
                options=list(LinkedInURLBuilder.TIME_FILTERS.keys()),
                index=5,  # Default to 24 hours
                help="Show jobs posted within this time period",
            )
            custom_hours = None
        else:
            time_filter = None
            custom_hours = st.number_input(
                "Hours",
                min_value=0.5,
                max_value=168.0,  # 1 week
                value=24.0,
                step=0.5,
                help="Custom time in hours (e.g., 1.5 for 1.5 hours)",
            )

        # Sort options
        sort_by = st.selectbox(
            "Sort by",
            options=["date_posted", "relevance"],
            format_func=lambda x: ("Most Recent" if x == "date_posted" else "Most Relevant"),
            help="How to sort the search results",
        )

        # Distance selector
        distance = st.selectbox(
            "Search Radius (miles)",
            options=[5, 10, 25, 50, 75, 100],
            index=2,
            help="How far from the location to search for jobs",
        )

    with col2:
        st.header("Advanced Filters")

        # Experience level
        st.subheader("Experience Level")
        experience_levels = st.multiselect(
            "Select experience levels",
            options=[
                "internship",
                "entry",
                "associate",
                "mid_senior",
                "director",
                "executive",
            ],
            format_func=lambda x: {
                "internship": "Internship",
                "entry": "Entry Level",
                "associate": "Associate",
                "mid_senior": "Mid-Senior Level",
                "director": "Director",
                "executive": "Executive",
            }[x],
            help="Filter by required experience level",
        )

        # Job type
        st.subheader("Job Type")
        job_types = st.multiselect(
            "Select job types",
            options=["full_time", "part_time", "contract", "temporary", "internship"],
            format_func=lambda x: {
                "full_time": "Full-time",
                "part_time": "Part-time",
                "contract": "Contract",
                "temporary": "Temporary",
                "internship": "Internship",
            }[x],
            help="Filter by employment type",
        )

        # Work location with checkboxes
        st.subheader("Work Location")
        st.write("Select work arrangements:")

        # Create columns for checkboxes
        col1, col2, col3 = st.columns(3)

        with col1:
            on_site = st.checkbox("🏢 On-site", value=True, help="Office-based positions")

        with col2:
            remote = st.checkbox("🏠 Remote", value=False, help="Work from home positions")

        with col3:
            hybrid = st.checkbox("🔄 Hybrid", value=True, help="Mix of office and remote work")

        # Build the remote options list based on checkboxes
        remote_options = []
        if on_site:
            remote_options.append("on_site")
        if remote:
            remote_options.append("remote")
        if hybrid:
            remote_options.append("hybrid")

    # Build URL button
    st.markdown("---")

    # Custom CSS for button styling
    st.markdown(
        """
    <style>
    .stButton > button {
        background: linear-gradient(90deg, #00d4ff 0%, #0099cc 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(0, 212, 255, 0.3) !important;
        transition: box-shadow 0.2s ease !important;
    }
    .stButton > button:hover {
        box-shadow: 0 6px 16px rgba(0, 212, 255, 0.4) !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    if st.button("🔗 Generate LinkedIn Search URL", use_container_width=True):
        if not keywords:
            st.error("Please enter keywords or job title")
        else:
            try:
                # Build the URL
                builder = LinkedInURLBuilder()
                url_builder = builder.set_keywords(keywords)

                # Handle location based on method
                if location_method == "Common Locations":
                    url_builder.set_location_by_name(location)
                elif location_method == "Custom Location" and location:
                    url_builder.set_location(location)
                elif location_method == "Geographic ID" and geo_id:
                    url_builder.set_geo_id(geo_id)

                url_builder = url_builder.set_distance(distance).set_sort_by(sort_by)

                # Set time filter
                if time_filter:
                    url_builder.set_time_filter(time_filter)
                elif custom_hours:
                    url_builder.set_custom_time_hours(custom_hours)

                # Set optional parameters
                if job_id:
                    url_builder.params["currentJobId"] = job_id
                if experience_levels:
                    url_builder.set_experience_level(experience_levels)

                if job_types:
                    url_builder.set_job_type(job_types)

                if remote_options:
                    url_builder.set_remote_options(remote_options)

                # Generate URL
                final_url = url_builder.build_url()
                params_summary = url_builder.get_params_summary()

                # Automatically copy URL to clipboard
                try:
                    import pyperclip

                    pyperclip.copy(final_url)
                    copy_status = "✅ URL generated and copied to clipboard!"
                except ImportError:
                    copy_status = "✅ URL generated! (Install pyperclip for auto-copy: pip install pyperclip)"
                except Exception:
                    copy_status = "✅ URL generated! (Copy manually from below)"

                # Display results
                st.success(copy_status)

                # URL display
                st.subheader("� Generated URL")
                st.code(final_url, language=None)

                # Manual copy instructions
                st.info(
                    "💡 **Tip**: The URL has been automatically copied to your clipboard. "
                    "You can also select and copy the URL above manually."
                )

                # Parameters summary
                if params_summary:
                    st.subheader("Search Parameters Summary")
                    for param, value in params_summary.items():
                        st.write(f"**{param}:** {value}")

                # Quick link
                st.subheader("Quick Access")
                st.markdown(f"[🚀 Open in LinkedIn]({final_url})", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error generating URL: {str(e)}")

    # Help section
    st.markdown("---")
    with st.expander("ℹ️ Help & Tips"):
        st.markdown(
            """
        ### How to use this tool:

        1. **Keywords**: Enter the job title, skills, or keywords you're looking for
        2. **Location**: Specify where you want to work (city, state, or "Remote")
        3. **Time Filter**: Choose how recent the job postings should be
        4. **Advanced Filters**: Narrow down by experience level, job type, and work arrangement

        ### Pro Tips:

        - Use specific keywords for better results (e.g., "Senior Python Developer" vs "Developer")
        - For remote work, try both location="Remote" and selecting "Remote" in work arrangements
        - Shorter time filters (1-4 hours) help you catch new postings quickly
        - Sort by "Most Recent" when using short time filters
        - Use multiple experience levels if you're open to different seniority levels

        ### Time Filter Shortcuts:

        - **1 hour**: Perfect for frequent checking throughout the day
        - **4-8 hours**: Good for checking twice daily
        - **24 hours**: Daily job hunting routine
        - **1 week**: Weekly comprehensive search

        ### URL Parameters Explained:

        The generated URL contains parameters that control the search:
        - `keywords`: Your search terms
        - `location`: Geographic location
        - `f_TPR`: Time filter (r3600 = 1 hour, r86400 = 24 hours)
        - `distance`: Search radius in miles
        - `sortBy`: Sorting method (DD = date, R = relevance)
        """
        )


if __name__ == "__main__":
    main()
