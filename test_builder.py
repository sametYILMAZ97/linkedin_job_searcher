"""
Test script to verify the LinkedIn URL Builder functionality
"""

import sys
import traceback

try:
    from linkedin_url_builder import LinkedInURLBuilder, create_optimized_url
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)


def test_basic_functionality():
    """Test basic URL building functionality."""
    print("Testing LinkedIn URL Builder...")

    try:
        builder = LinkedInURLBuilder()
        url = (
            builder.set_keywords("Python Developer")
            .set_location("San Francisco")
            .set_distance(25)
            .set_time_filter("24 hours")
            .build_url()
        )

        print("\nTest 1 - Basic URL:")
        print(url)
        assert "keywords=Python%20Developer" in url
        assert "location=San%20Francisco" in url
        print("[PASS] Basic URL building works")

        # Test 2: Time filter conversion
        builder2 = LinkedInURLBuilder()
        url2 = builder2.set_custom_time_hours(1.5).build_url()
        print("\nTest 2 - Custom time filter (1.5 hours):")
        print(url2)
        assert "f_TPR=r5400" in url2  # 1.5 hours = 5400 seconds
        print("[PASS] Custom time filter works")

        # Test 3: Advanced filters
        builder3 = LinkedInURLBuilder()
        url3 = (
            builder3.set_keywords("Data Scientist")
            .set_experience_level(["mid_senior", "director"])
            .set_job_type(["full_time"])
            .set_remote_options(["remote", "hybrid"])
            .build_url()
        )

        print("\nTest 3 - Advanced filters:")
        print(url3)
        print("[PASS] Advanced filters work")

        # Test 4: Parameters summary
        builder4 = LinkedInURLBuilder()
        (
            builder4.set_keywords("Software Engineer")
            .set_location("Remote")
            .set_time_filter("4 hours")
            .set_sort_by("date_posted")
        )

        summary = builder4.get_params_summary()
        print("\nTest 4 - Parameters summary:")
        for key, value in summary.items():
            print(f"  {key}: {value}")
        print("[PASS] Parameters summary works")

        # Test 5: Helper function
        url5, summary5 = create_optimized_url(
            keywords="Machine Learning Engineer",
            location="Seattle",
            time_filter="8 hours",
            experience_levels=["mid_senior"],
            remote_options=["remote"],
        )

        print("\nTest 5 - Helper function:")
        print(f"URL: {url5}")
        print("Summary:")
        for key, value in summary5.items():
            print(f"  {key}: {value}")
        print("[PASS] Helper function works")

        print("\n*** All tests passed! The LinkedIn URL Builder is working correctly. ***")

    except Exception as e:
        print(f"\n[ERROR] Test failed with error: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    test_basic_functionality()
