"""
Streamlit Web Interface for LinkedIn Job Search URL Builder
"""

import streamlit as st
from linkedin_url_builder import LinkedInURLBuilder, create_optimized_url


def main():
    st.set_page_config(
        page_title="LinkedIn Job Search URL Builder",
        page_icon="🔍",
        layout="wide"
    )

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
            help="Enter job title, skills, or keywords to search for"
        )

        location = st.text_input(
            "Location",
            placeholder="e.g., San Francisco, Remote, New York",
            help="City, state, country, or 'Remote' for remote positions"
        )

        distance = st.selectbox(
            "Search Radius (miles)",
            options=[5, 10, 25, 50, 75, 100],
            index=2,
            help="How far from the location to search for jobs"
        )

        # Geographic ID (optional)
        geo_id = st.text_input(
            "Geographic ID (Optional)",
            placeholder="e.g., 103644278 for specific region targeting",
            help="Optional: LinkedIn's internal geographic ID for precise location targeting"
        )

        # Job ID (optional)
        job_id = st.text_input(
            "Specific Job ID (Optional)",
            placeholder="e.g., 4185657072",
            help="Optional: Enter a specific LinkedIn job ID to track or reference"
        )

        # Time filter
        st.subheader("⏰ Time Filter")
        time_option = st.radio(
            "Posted within:",
            options=["Preset times", "Custom hours"],
            horizontal=True
        )

        if time_option == "Preset times":
            time_filter = st.selectbox(
                "Time period",
                options=list(LinkedInURLBuilder.TIME_FILTERS.keys()),
                index=5,  # Default to 24 hours
                help="Show jobs posted within this time period"
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
                help="Custom time in hours (e.g., 1.5 for 1.5 hours)"
            )

        # Sort options
        sort_by = st.selectbox(
            "Sort by",
            options=["date_posted", "relevance"],
            format_func=lambda x: "Most Recent" if x == "date_posted" else "Most Relevant",
            help="How to sort the search results"
        )

    with col2:
        st.header("Advanced Filters")

        # Experience level
        st.subheader("Experience Level")
        experience_levels = st.multiselect(
            "Select experience levels",
            options=['internship', 'entry', 'associate', 'mid_senior', 'director', 'executive'],
            format_func=lambda x: {
                'internship': 'Internship',
                'entry': 'Entry Level',
                'associate': 'Associate',
                'mid_senior': 'Mid-Senior Level',
                'director': 'Director',
                'executive': 'Executive'
            }[x],
            help="Filter by required experience level"
        )

        # Job type
        st.subheader("Job Type")
        job_types = st.multiselect(
            "Select job types",
            options=['full_time', 'part_time', 'contract', 'temporary', 'internship'],
            format_func=lambda x: {
                'full_time': 'Full-time',
                'part_time': 'Part-time',
                'contract': 'Contract',
                'temporary': 'Temporary',
                'internship': 'Internship'
            }[x],
            help="Filter by employment type"
        )

        # Remote options
        st.subheader("Work Location")
        remote_options = st.multiselect(
            "Select work arrangements",
            options=['on_site', 'remote', 'hybrid'],
            format_func=lambda x: {
                'on_site': 'On-site',
                'remote': 'Remote',
                'hybrid': 'Hybrid'
            }[x],
            help="Filter by work location arrangement"
        )

    # Build URL button
    st.markdown("---")

    # Custom CSS for button styling
    st.markdown("""
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
    """, unsafe_allow_html=True)

    if st.button("🔗 Generate LinkedIn Search URL", use_container_width=True):
        if not keywords:
            st.error("Please enter keywords or job title")
        else:
            try:
                # Build the URL
                builder = LinkedInURLBuilder()
                url_builder = (builder
                              .set_keywords(keywords)
                              .set_location(location)
                              .set_distance(distance)
                              .set_sort_by(sort_by))

                # Set time filter
                if time_filter:
                    url_builder.set_time_filter(time_filter)
                elif custom_hours:
                    url_builder.set_custom_time_hours(custom_hours)

                # Set optional parameters
                if geo_id:
                    url_builder.set_geo_id(geo_id)

                if job_id:
                    url_builder.params['currentJobId'] = job_id
                if experience_levels:
                    url_builder.set_experience_level(experience_levels)

                if job_types:
                    url_builder.set_job_type(job_types)

                if remote_options:
                    url_builder.set_remote_options(remote_options)

                # Generate URL
                final_url = url_builder.build_url()
                params_summary = url_builder.get_params_summary()

                # Display results
                st.success("✅ LinkedIn search URL generated successfully!")

                # URL display and copy
                st.subheader("🔗 Generated URL")
                st.code(final_url, language=None)

                # Create columns for copy button and status
                col1, col2 = st.columns([1, 3])

                with col1:
                    # Enhanced copy button with session state
                    if 'url_copied' not in st.session_state:
                        st.session_state.url_copied = False

                    if st.button("📋 Copy URL", key="copy_url_btn"):
                        try:
                            import pyperclip
                            pyperclip.copy(final_url)
                            st.session_state.url_copied = True
                            st.rerun()
                        except ImportError:
                            st.error("⚠️ pyperclip not installed. Install with: pip install pyperclip")
                        except Exception as e:
                            st.error(f"⚠️ Copy failed: {str(e)}")

                with col2:
                    if st.session_state.url_copied:
                        st.success("✅ URL copied to clipboard!")
                        # Reset the state after showing success
                        if st.button("🔄 Reset", key="reset_copy"):
                            st.session_state.url_copied = False
                            st.rerun()

                # Alternative copy method
                st.info("💡 **Alternative**: Click and drag to select the URL above, then Ctrl+C to copy")

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
        st.markdown("""
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
        """)


if __name__ == "__main__":
    main()
