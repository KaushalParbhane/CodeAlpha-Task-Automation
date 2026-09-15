"""
Task Automation Suite - Main Interactive Runner
Provides a friendly CLI interface to choose and run any of the task automation scripts.
"""

import sys
import os

from file_organizer import move_jpg_files
from email_extractor import extract_emails
from web_scraper import scrape_webpage_title


def print_banner():
    print("=" * 60)
    print("      PYTHON TASK AUTOMATION SUITE - CODEALPHA TASK 3      ")
    print("=" * 60)
    print("Key Concepts Used: os, shutil, re, requests, file handling")
    print("-" * 60)


def menu_file_organizer():
    print("\n--- [Option 1] Move JPG Files ---")
    source = input("Enter source folder path: ").strip()
    dest = input("Enter destination folder path: ").strip()
    action_type = input("Do you want to (M)ove or (C)opy files? [Default: M]: ").strip().lower()
    copy_instead = (action_type == 'c')

    try:
        count = move_jpg_files(source, dest, copy_instead=copy_instead)
        print(f"\n[+] Success! Processed {count} file(s).")
    except Exception as err:
        print(f"\n[-] Error: {err}")


def menu_email_extractor():
    print("\n--- [Option 2] Extract Emails from Text File ---")
    input_file = input("Enter input .txt file path: ").strip()
    output_file = input("Enter output file path to save emails: ").strip()

    try:
        emails = extract_emails(input_file, output_file)
        print(f"\n[+] Success! Extracted {len(emails)} email(s) into '{output_file}':")
        for email in emails:
            print(f"    - {email}")
    except Exception as err:
        print(f"\n[-] Error: {err}")


def menu_web_scraper():
    print("\n--- [Option 3] Scrape Webpage Title ---")
    url = input("Enter webpage URL (e.g. https://python.org): ").strip()
    output_file = input("Enter output file path to save title log [Press Enter for 'scraped_titles.txt']: ").strip()
    if not output_file:
        output_file = "scraped_titles.txt"

    try:
        title = scrape_webpage_title(url, output_file)
        print(f"\n[+] Success! Webpage Title: {title}")
        print(f"    Title logged in '{output_file}'")
    except Exception as err:
        print(f"\n[-] Error: {err}")


def menu_run_demo():
    print("\n--- [Option 4] Running Full Automated Demo ---")
    import demo
    demo.run_all_demos()


def main():
    while True:
        print_banner()
        print("Select an automation task to run:")
        print("  1. Move all .jpg files from a folder to a new folder (os, shutil)")
        print("  2. Extract all email addresses from a .txt file (re, file handling)")
        print("  3. Scrape the title of a webpage and save it (requests, re)")
        print("  4. Run Full Automated Demo & Test Suite")
        print("  5. Exit")
        print("-" * 60)

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            menu_file_organizer()
        elif choice == '2':
            menu_email_extractor()
        elif choice == '3':
            menu_web_scraper()
        elif choice == '4':
            menu_run_demo()
        elif choice == '5':
            print("\nThank you for using Python Task Automation Suite. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice! Please select 1, 2, 3, 4, or 5.\n")

        input("\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main()
