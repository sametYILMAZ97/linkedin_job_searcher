#!/usr/bin/env python3
"""
LinkedIn Job Searcher - Application Starter
Handles starting, stopping, and managing the Streamlit web application
"""
import argparse
import subprocess
import sys
import os
import time


def stop_streamlit():
    """Stop running Streamlit processes using taskkill on Windows."""
    if os.name == 'nt':  # Windows
        try:
            # Kill streamlit processes
            subprocess.run(['taskkill', '/F', '/IM', 'python.exe', 
                           '/FI', 'WINDOWTITLE eq streamlit*'], 
                          capture_output=True)
            subprocess.run(['taskkill', '/F', '/IM', 'python.exe', 
                           '/FI', 'COMMANDLINE eq *streamlit*'], 
                          capture_output=True)
            print("[STOP] Attempted to stop Streamlit processes.")
        except Exception as e:
            print(f"[ERROR] Failed to stop processes: {e}")
    else:  # Unix/Linux
        try:
            subprocess.run(['pkill', '-f', 'streamlit'], capture_output=True)
            print("[STOP] Attempted to stop Streamlit processes.")
        except Exception as e:
            print(f"[ERROR] Failed to stop processes: {e}")


def start_streamlit(background=False):
    """Start the Streamlit application."""
    # Prepare command
    python_exe = sys.executable
    cmd = [python_exe, "-m", "streamlit", "run", "app.py", "--server.port=8501"]

    print("[START] Starting LinkedIn Job Searcher...")
    print(f"[INFO] Command: {' '.join(cmd)}")

    try:
        if background:
            # Start in background
            if os.name == 'nt':  # Windows
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                )
            else:  # Unix/Linux
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    preexec_fn=os.setsid
                )
            print(f"[SUCCESS] Started in background (PID: {process.pid})")
            print("[WEB] Access at: http://localhost:8501")
            print("[STOP] Use 'python start_app.py --stop' to stop")
        else:
            # Start in foreground
            print("[WEB] Starting web interface at: http://localhost:8501")
            print("[INFO] Press Ctrl+C to stop")
            subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[STOP] Application stopped by user.")
    except Exception as e:
        print(f"[ERROR] Failed to start application: {e}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="LinkedIn Job Searcher - Application Manager")
    parser.add_argument("--background", action="store_true", help="Run in background")
    parser.add_argument("--stop", action="store_true", help="Stop running instances")
    
    args = parser.parse_args()
    
    if args.stop:
        stop_streamlit()
    else:
        start_streamlit(background=args.background)


if __name__ == "__main__":
    main()
