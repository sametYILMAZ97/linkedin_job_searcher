"""
Test to verify the correct Turkey geographic ID
"""

from linkedin_url_builder import LinkedInURLBuilder


def test_turkey_geo_id():
    """Test the Turkey geographic ID mapping."""
    print("🇹🇷 Testing Turkey Geographic ID Mapping")
    print("=" * 50)

    # Test Turkey mapping
    builder = LinkedInURLBuilder()

    # Test different Turkey variations
    test_cases = ["Turkey (All)", "turkey", "Turkey", "TURKEY", "Türkiye"]

    for location in test_cases:
        builder_test = LinkedInURLBuilder()
        url = (
            builder_test.set_keywords("Fullstack Developer")
            .set_location_by_name(location)
            .set_distance(100)
            .set_time_filter("12 hours")
            .set_remote_options(["on_site", "hybrid"])
            .build_url()
        )

        print(f"\nLocation: {location}")
        print(f"URL: {url}")

        # Check if it has the correct geoId
        if "geoId=90009706" in url:
            print("✅ Correct Turkey geoId found!")
        elif "geoId=105117694" in url:
            print("❌ Wrong geoId - this points to Sweden!")
        elif "location=" in url and "geoId=" not in url:
            print("⚠️  Using text location instead of geoId")
        else:
            print("❓ No location parameter found")

    print("\n" + "=" * 50)
    print("Turkey geoId should be: 90009706 (NOT 105117694 which is Sweden)")


if __name__ == "__main__":
    test_turkey_geo_id()
