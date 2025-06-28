#!/usr/bin/env python3
"""
Run all tests locally to verify CI/CD will pass
"""
import subprocess
import sys


def run_test(test_name, command):
    """Run a single test and report results."""
    print(f"\n{'='*50}")
    print(f"[TEST] Running {test_name}...")
    print(f"{'='*50}")

    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, timeout=30)

        if result.returncode == 0:
            print(f"[PASS] {test_name} PASSED")
            if result.stdout.strip():
                print("Output:")
                print(result.stdout)
            return True
        else:
            print(f"[FAIL] {test_name} FAILED")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False

    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] {test_name} TIMED OUT")
        return False
    except Exception as e:
        print(f"[ERROR] {test_name} ERROR: {e}")
        return False


def main():
    """Run all tests."""
    print("[TEST] Running LinkedIn Job Searcher Test Suite")
    print("=" * 60)

    # Python executable path
    python_exe = "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe"

    tests = [
        ("Core Functionality", f"{python_exe} test_builder.py"),
        ("New Features", f"{python_exe} test_new_features.py"),
        ("LinkedIn Format", f"{python_exe} test_linkedin_format.py"),
        ("Turkey GeoID", f"{python_exe} test_turkey_geoid.py"),
        ("CLI Interface", f'{python_exe} cli.py "Test Job" --location "Test Location" --time "1 hour" --summary'),
        ("Demo Script", f"{python_exe} demo.py"),
    ]

    passed = 0
    total = len(tests)

    for test_name, command in tests:
        if run_test(test_name, command):
            passed += 1

    print(f"\n{'='*60}")
    print(f"[RESULTS] TEST RESULTS: {passed}/{total} tests passed")
    print(f"{'='*60}")

    if passed == total:
        print("[SUCCESS] ALL TESTS PASSED! CI/CD should work correctly.")
        sys.exit(0)
    else:
        print(f"[FAILED] {total - passed} tests failed. Please fix before pushing.")
        sys.exit(1)


if __name__ == "__main__":
    main()
