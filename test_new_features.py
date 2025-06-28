"""
Test the new features: job ID and geo ID support
"""

from linkedin_url_builder import LinkedInURLBuilder


def test_new_features():
    """Test the new job ID and geo ID functionality."""
    print("Testing new LinkedIn URL Builder features...")

    # Test with job ID and geo ID
    builder = LinkedInURLBuilder()

    # Manually add job ID (like in the app)
    builder.params["currentJobId"] = "4185657072"

    url = (
        builder.set_keywords("director sales operations")
        .set_location("United States")
        .set_distance(25)
        .set_time_filter("1 hour")
        .set_geo_id("103644278")
        .build_url()
    )

    print("\nTest - URL with Job ID and Geo ID:")
    print(url)

    # Verify parameters are included
    assert "currentJobId=4185657072" in url
    assert "geoId=103644278" in url
    assert "f_TPR=r3600" in url  # 1 hour = 3600 seconds
    assert "keywords=director%20sales%20operations" in url

    print("✅ Job ID and Geo ID features work correctly!")

    # Test parameters summary
    summary = builder.get_params_summary()
    print(f"\nParameters summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")

    print("🎉 All new features tested successfully!")


if __name__ == "__main__":
    test_new_features()
