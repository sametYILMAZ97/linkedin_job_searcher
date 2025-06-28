"""
Command Line Interface for LinkedIn Job Search URL Builder
"""

import argparse
import sys
from typing import List

from linkedin_url_builder import LinkedInURLBuilder


def parse_list_argument(value: str) -> List[str]:
    """Parse comma-separated list argument."""
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def main():
    parser = argparse.ArgumentParser(
        description="Generate optimized LinkedIn job search URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py "Python Developer" --location "San Francisco" --time "4 hours"
  python cli.py "Data Scientist" --distance 50 --experience mid_senior,director
  python cli.py "Remote Software Engineer" --remote remote,hybrid --sort date_posted

Time filter options:
  1 hour, 2 hours, 4 hours, 8 hours, 12 hours, 24 hours,
  3 days, 1 week, 2 weeks, 1 month

Experience levels:
  internship, entry, associate, mid_senior, director, executive

Job types:
  full_time, part_time, contract, temporary, internship

Remote options:
  on_site, remote, hybrid
        """,
    )

    # Required arguments
    parser.add_argument(
        "keywords", help='Job keywords or title (e.g., "Python Developer")'
    )

    # Optional arguments
    parser.add_argument(
        "--location",
        "-l",
        default="",
        help='Job location (e.g., "San Francisco", "Remote")',
    )

    parser.add_argument(
        "--distance",
        "-d",
        type=int,
        default=25,
        help="Search radius in miles (default: 25)",
    )

    parser.add_argument(
        "--time", "-t", default="24 hours", help='Time filter (default: "24 hours")'
    )

    parser.add_argument(
        "--custom-hours",
        type=float,
        help="Custom time filter in hours (overrides --time)",
    )

    parser.add_argument(
        "--sort",
        "-s",
        choices=["relevance", "date_posted"],
        default="date_posted",
        help="Sort order (default: date_posted)",
    )

    parser.add_argument(
        "--experience",
        "-e",
        type=parse_list_argument,
        default=[],
        help="Experience levels (comma-separated)",
    )

    parser.add_argument(
        "--job-types",
        "-j",
        type=parse_list_argument,
        default=[],
        help="Job types (comma-separated)",
    )

    parser.add_argument(
        "--remote",
        "-r",
        type=parse_list_argument,
        default=[],
        help="Remote work options (comma-separated)",
    )

    parser.add_argument("--geo-id", help="Geographic ID for precise location targeting")

    parser.add_argument(
        "--summary", action="store_true", help="Show parameters summary"
    )

    parser.add_argument(
        "--copy", action="store_true", help="Copy URL to clipboard (requires pyperclip)"
    )

    parser.add_argument("--job-id", help="Specific LinkedIn job ID to reference")

    args = parser.parse_args()

    # Validate time filter
    if args.time not in LinkedInURLBuilder.TIME_FILTERS and not args.custom_hours:
        print(f"Warning: '{args.time}' is not a recognized time filter.")
        print("Available options:", ", ".join(LinkedInURLBuilder.TIME_FILTERS.keys()))
        print("Using default: 24 hours")
        args.time = "24 hours"

    # Build URL
    try:
        builder = LinkedInURLBuilder()

        url_builder = (
            builder.set_keywords(args.keywords)
            .set_location_by_name(args.location)
            .set_distance(args.distance)
            .set_sort_by(args.sort)
        )

        # Set time filter
        if args.custom_hours:
            url_builder.set_custom_time_hours(args.custom_hours)
        else:
            url_builder.set_time_filter(args.time)

        # Set optional parameters
        if args.geo_id:
            url_builder.set_geo_id(args.geo_id)

        if args.job_id:
            url_builder.params["currentJobId"] = args.job_id

        if args.experience:
            url_builder.set_experience_level(args.experience)

        if args.job_types:
            url_builder.set_job_type(args.job_types)

        if args.remote:
            url_builder.set_remote_options(args.remote)

        # Generate URL
        final_url = url_builder.build_url()

        # Output
        print("LinkedIn Job Search URL:")
        print(final_url)

        if args.summary:
            params_summary = url_builder.get_params_summary()
            if params_summary:
                print("\nParameters Summary:")
                for param, value in params_summary.items():
                    print(f"  {param}: {value}")

        if args.copy:
            try:
                import pyperclip

                pyperclip.copy(final_url)
                print("\n✓ URL copied to clipboard!")
            except ImportError:
                print(
                    "\nNote: Install pyperclip to enable clipboard copying: pip install pyperclip"
                )
            except Exception as e:
                print(f"\nWarning: Could not copy to clipboard: {e}")

    except Exception as e:
        print(f"Error generating URL: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
