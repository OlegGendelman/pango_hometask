import os
import time
import subprocess
import sys
import webbrowser

import config


def run_pytest_with_html_report():
    """
    The function runs pytest with the specified arguments and generates an HTML report.
    """

    test_args = [
        "pytest",
        config.tests_path,
        "--headed",  # Optional: show browser
        "--slowmo=600", # Slow down each action by 500 ms
        "--browser", "chromium",  # Optional: specify browser
        "--disable-warnings",
        f"--html={config.report_path}",  # Generate HTML report
        "--self-contained-html"  # Embed CSS/JS in one file
    ]

    try:
        subprocess.run(test_args, check=False)
    except subprocess.CalledProcessError as e:
        print("Tests failed.")
        sys.exit(e.returncode)

    print(f"Report generated at: {config.report_path}")

    # Wait briefly to ensure a file is written
    time.sleep(1)

    if os.path.exists(config.report_path):
        try:
            # Attempt to an open-generated report in a new window
            webbrowser.open_new(config.report_path)
            print("Report opened in browser.")
        except Exception as e:
            print(f"Could not open report: {e}")
    else:
        print("Report file was not found.")


if __name__ == "__main__":
    run_pytest_with_html_report()