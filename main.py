"""
LinkedIn Job Searcher - Main Application Entry Point
"""

import argparse
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))


def main():
    parser = argparse.ArgumentParser(
        description="LinkedIn Job Search URL Builder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--mode",
        choices=["web", "cli"],
        default="web",
        help="Run mode: web (Streamlit UI) or cli (command line)",
    )

    parser.add_argument(
        "--port", type=int, default=8501, help="Port for web interface (default: 8501)"
    )

    # Parse known args to allow forwarding unknown args to CLI
    args, unknown = parser.parse_known_args()

    if args.mode == "web":
        print("Starting LinkedIn Job Searcher Web Interface...")
        print(f"Open your browser to: http://localhost:{args.port}")
        print("Press Ctrl+C to stop the server")

        import os
        import subprocess

        try:
            # Run Streamlit app
            cmd = [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                str(project_dir / "app.py"),
                "--server.port",
                str(args.port),
                "--server.headless",
                "true",
            ]
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print("\nShutting down...")
        except Exception as e:
            print(f"Error starting web interface: {e}")
            print("Make sure Streamlit is installed: pip install streamlit")

    elif args.mode == "cli":
        # Forward to CLI module
        from cli import main as cli_main

        # Reconstruct sys.argv for CLI
        sys.argv = ["cli.py"] + unknown
        cli_main()


if __name__ == "__main__":
    main()
