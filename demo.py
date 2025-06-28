"""
Comprehensive test of LinkedIn Job Searcher with all new features
"""

from linkedin_url_builder import LinkedInURLBuilder


def demo_all_features():
    """Demonstrate all LinkedIn URL Builder features including new ones."""
    print("🚀 LinkedIn Job Searcher - Complete Feature Demo")
    print("=" * 60)

    # Test 1: Basic search with new time precision
    print("\n1. Basic Search with Precise Timing:")
    builder1 = LinkedInURLBuilder()
    url1 = (builder1
           .set_keywords("Python Developer")
           .set_location("San Francisco")
           .set_custom_time_hours(0.5)  # 30 minutes
           .set_distance(25)
           .set_sort_by("date_posted")
           .build_url())
    print(f"   30-minute fresh jobs: {url1}")

    # Test 2: Advanced search with all filters
    print("\n2. Advanced Search with All Filters:")
    builder2 = LinkedInURLBuilder()
    url2 = (builder2
           .set_keywords("Senior Data Scientist")
           .set_location("Remote")
           .set_time_filter("4 hours")
           .set_experience_level(['mid_senior', 'director'])
           .set_job_type(['full_time'])
           .set_remote_options(['remote', 'hybrid'])
           .build_url())
    print(f"   Multi-filter search: {url2}")

    # Test 3: Job tracking with ID and geographic precision
    print("\n3. Job Tracking with ID and Geographic Targeting:")
    builder3 = LinkedInURLBuilder()
    builder3.params['currentJobId'] = '4185657072'  # Manual job ID
    url3 = (builder3
           .set_keywords("director sales operations")
           .set_location("United States")
           .set_distance(25)
           .set_time_filter("1 hour")
           .set_geo_id("103644278")
           .build_url())
    print(f"   Targeted tracking: {url3}")

    # Test 4: Ultra-fresh job hunting
    print("\n4. Ultra-Fresh Job Hunting (15 minutes):")
    builder4 = LinkedInURLBuilder()
    url4 = (builder4
           .set_keywords("DevOps Engineer")
           .set_location("Seattle")
           .set_custom_time_hours(0.25)  # 15 minutes
           .set_sort_by("date_posted")
           .build_url())
    print(f"   15-minute window: {url4}")

    # Test 5: Parameters summary demo
    print("\n5. Parameters Summary:")
    summary = builder3.get_params_summary()
    for param, value in summary.items():
        print(f"   {param}: {value}")

    print("\n" + "=" * 60)
    print("✅ All features demonstrated successfully!")
    print("📱 Web interface running at: http://localhost:8502")
    print("💻 Use CLI with: python cli.py --help for full options")
    print("🎯 Perfect for catching fresh job postings before competition!")


if __name__ == "__main__":
    demo_all_features()
