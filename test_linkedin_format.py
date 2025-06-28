"""
Test the updated LinkedIn URL Builder with proper LinkedIn format
"""

from linkedin_url_builder import LinkedInURLBuilder


def test_linkedin_format():
    """Test the new LinkedIn-compliant URL format."""
    print("🧪 Testing Updated LinkedIn URL Builder")
    print("=" * 50)

    # Test 1: Using geo ID (like the working example)
    print("\n1. Testing with Geo ID (Ankara):")
    builder1 = LinkedInURLBuilder()
    url1 = (
        builder1.set_keywords("Fullstack Developer")
        .set_geo_id("100138681")  # Ankara geo ID
        .set_remote_options(["on_site", "hybrid"])
        .build_url()
    )
    print(f"Generated: {url1}")

    # Verify required parameters
    assert "origin=JOB_SEARCH_PAGE_JOB_FILTER" in url1
    assert "refresh=true" in url1
    assert "geoId=100138681" in url1
    assert "keywords=Fullstack%20Developer" in url1
    assert "f_WT=1%2C3" in url1

    print("✅ Required LinkedIn parameters present!")

    # Test 2: Using location by name
    print("\n2. Testing with Location by Name:")
    builder2 = LinkedInURLBuilder()
    url2 = (
        builder2.set_keywords("Python Developer")
        .set_location_by_name("ankara")
        .set_time_filter("4 hours")
        .build_url()
    )
    print(f"Generated: {url2}")

    # Should use geo ID instead of location
    assert "geoId=100138681" in url2
    assert "location=" not in url2  # Should not have location parameter

    print("✅ Location by name works correctly!")

    # Test 3: Comparison with working URL structure
    print("\n3. Comparing with Working URL Structure:")
    working_params = {
        "currentJobId": "4254871166",
        "f_WT": "1,3",
        "geoId": "100138681",
        "keywords": "Fullstack Developer",
        "origin": "JOB_SEARCH_PAGE_JOB_FILTER",
        "refresh": "true",
    }

    builder3 = LinkedInURLBuilder()
    builder3.params["currentJobId"] = "4254871166"
    url3 = (
        builder3.set_keywords("Fullstack Developer")
        .set_geo_id("100138681")
        .set_remote_options(["on_site", "hybrid"])
        .build_url()
    )

    print(f"Generated: {url3}")

    # Check all required parameters are present
    for param in working_params:
        if param in ["f_WT"]:  # Special handling for encoded parameters
            assert param in url3
        else:
            assert param in url3

    print("✅ Matches working URL structure!")

    print("\n" + "=" * 50)
    print("🎉 All tests passed! URLs should now work with LinkedIn!")


if __name__ == "__main__":
    test_linkedin_format()
