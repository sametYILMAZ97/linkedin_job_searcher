"""
Modern pytest-based tests for LinkedIn URL Builder
"""

import pytest

from linkedin_url_builder import LinkedInURLBuilder, create_optimized_url


class TestLinkedInURLBuilder:
    """Test cases for the LinkedIn URL Builder class."""

    def test_basic_url_building(self):
        """Test basic URL building functionality."""
        builder = LinkedInURLBuilder()
        url = (
            builder.set_keywords("Python Developer")
            .set_location("San Francisco")
            .set_distance(25)
            .set_time_filter("24 hours")
            .build_url()
        )

        assert "keywords=Python%20Developer" in url
        assert "location=San%20Francisco" in url
        assert "distance=25" in url
        assert "f_TPR=r86400" in url  # 24 hours = 86400 seconds

    def test_custom_time_filter(self):
        """Test custom time filter conversion."""
        builder = LinkedInURLBuilder()
        url = builder.set_custom_time_hours(1.5).build_url()

        assert "f_TPR=r5400" in url  # 1.5 hours = 5400 seconds

    def test_advanced_filters(self):
        """Test advanced filtering options."""
        builder = LinkedInURLBuilder()
        url = (
            builder.set_keywords("Data Scientist")
            .set_experience_level(["mid_senior", "director"])
            .set_job_type(["full_time"])
            .set_remote_options(["remote", "hybrid"])
            .build_url()
        )

        assert "keywords=Data%20Scientist" in url
        assert "f_E=" in url  # Experience level
        assert "f_JT=" in url  # Job type
        assert "f_WT=" in url  # Work type

    def test_parameters_summary(self):
        """Test parameters summary functionality."""
        builder = LinkedInURLBuilder()
        builder.set_keywords("Software Engineer").set_location("Remote").set_time_filter("4 hours")

        summary = builder.get_params_summary()

        assert "Keywords" in summary
        assert summary["Keywords"] == "Software Engineer"
        assert summary["Location"] == "Remote"
        assert "4 hours" in summary["Posted Within"]

    def test_helper_function(self):
        """Test the helper function for creating optimized URLs."""
        url, summary = create_optimized_url(
            keywords="Machine Learning Engineer",
            location="Seattle",
            time_filter="8 hours",
            experience_levels=["mid_senior"],
            remote_options=["remote"],
        )

        assert "Machine%20Learning%20Engineer" in url
        assert "Seattle" in url
        assert "f_TPR=r28800" in url  # 8 hours = 28800 seconds
        assert isinstance(summary, dict)
        assert "Keywords" in summary

    @pytest.mark.parametrize(
        "time_filter,expected_seconds",
        [
            ("1 hour", 3600),
            ("4 hours", 14400),
            ("24 hours", 86400),
            ("1 week", 604800),
        ],
    )
    def test_time_filter_conversion(self, time_filter, expected_seconds):
        """Test various time filter conversions."""
        builder = LinkedInURLBuilder()
        url = builder.set_time_filter(time_filter).build_url()

        assert f"f_TPR=r{expected_seconds}" in url

    def test_job_id_and_geo_id(self):
        """Test job ID and geographic ID functionality."""
        builder = LinkedInURLBuilder()
        url = (
            builder.set_job_id("4185657072")
            .set_keywords("director sales operations")
            .set_geo_id("103644278")
            .set_time_filter("1 hour")
            .build_url()
        )

        assert "currentJobId=4185657072" in url
        assert "geoId=103644278" in url
        assert "f_TPR=r3600" in url

    def test_invalid_inputs(self):
        """Test handling of invalid inputs."""
        builder = LinkedInURLBuilder()

        # Test with empty strings - should not break
        url = builder.set_keywords("").set_location("").build_url()
        assert LinkedInURLBuilder.BASE_URL in url

        # Test with None values - should not break
        url = builder.set_keywords(None).set_location(None).build_url()
        assert LinkedInURLBuilder.BASE_URL in url

    def test_url_encoding(self):
        """Test proper URL encoding of special characters."""
        builder = LinkedInURLBuilder()
        url = builder.set_keywords("C++ Developer").set_location("São Paulo").build_url()

        assert "C%2B%2B" in url  # + should be encoded
        assert "S%C3%A3o" in url  # ã should be encoded
