"""
Automated Demo & Verification Script for Task Automation Suite
Creates test data, runs all 3 automation tasks, and verifies output results.
"""

import os
import shutil
from file_organizer import move_jpg_files
from email_extractor import extract_emails
from web_scraper import scrape_webpage_title


def setup_demo_environment(base_dir: str):
    """Creates temporary test files and folder structure."""
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    source_images_dir = os.path.join(base_dir, "source_images")
    os.makedirs(source_images_dir, exist_ok=True)

    # 1. Create dummy image files and a non-jpg file
    sample_files = ["photo_01.jpg", "vacation_shot.jpeg", "sunsets.JPG", "notes.txt", "document.pdf"]
    for filename in sample_files:
        filepath = os.path.join(source_images_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Dummy file content for {filename}")

    # 2. Create sample text file with emails embedded in text
    sample_text_path = os.path.join(base_dir, "sample_input.txt")
    sample_text_content = """
    Welcome to CodeAlpha Task Automation Demo!
    Here are some sample contact points:
    For support, reach out to support@codealpha.tech or helpdesk@example.com.
    You can also contact kaushal.dev@domain.org, or admin@company.co.in.
    Duplicate contact: support@codealpha.tech (should be deduplicated).
    Invalid emails to ignore: not_an_email, @missinguser.com, user@.com, test@domain.
    End of sample document.
    """
    with open(sample_text_path, "w", encoding="utf-8") as f:
        f.write(sample_text_content)

    print(f"[DEMO SETUP] Test directory created at '{base_dir}' with sample images and text.")


def run_all_demos():
    print("\n" + "=" * 60)
    print("        AUTOMATED TASK DEMO & VERIFICATION SUITE       ")
    print("=" * 60)

    base_dir = os.path.abspath("demo_workspace")
    setup_demo_environment(base_dir)

    # -------------------------------------------------------------
    # DEMO 1: File Organizer
    # -------------------------------------------------------------
    print("\n>>> [1/3] Running File Organizer (.jpg Move Test)...")
    source_dir = os.path.join(base_dir, "source_images")
    dest_dir = os.path.join(base_dir, "destination_images")

    moved_count = move_jpg_files(source_dir, dest_dir)
    dest_files = os.listdir(dest_dir) if os.path.exists(dest_dir) else []
    remaining_source_files = os.listdir(source_dir)

    print(f"    - Files moved to destination ({len(dest_files)}): {dest_files}")
    print(f"    - Files remaining in source: {remaining_source_files}")
    assert moved_count == 3, f"Expected 3 JPG files moved, got {moved_count}"
    assert "notes.txt" in remaining_source_files, "Non-JPG file 'notes.txt' should remain in source"
    print("    [OK] DEMO 1 PASSED: JPG files successfully filtered and moved!")

    # -------------------------------------------------------------
    # DEMO 2: Email Extractor
    # -------------------------------------------------------------
    print("\n>>> [2/3] Running Email Extractor (re & file handling)...")
    input_text = os.path.join(base_dir, "sample_input.txt")
    output_emails = os.path.join(base_dir, "extracted_emails.txt")

    emails = extract_emails(input_text, output_emails)
    print(f"    - Extracted Emails ({len(emails)}): {emails}")

    expected_emails = ["admin@company.co.in", "helpdesk@example.com", "kaushal.dev@domain.org", "support@codealpha.tech"]
    assert sorted(emails) == sorted(expected_emails), f"Expected {expected_emails}, got {emails}"
    assert os.path.exists(output_emails), "Output email text file was not created"
    print("    [OK] DEMO 2 PASSED: Emails successfully extracted, deduplicated, and saved!")

    # -------------------------------------------------------------
    # DEMO 3: Web Scraper
    # -------------------------------------------------------------
    print("\n>>> [3/3] Running Web Title Scraper (requests, re)...")
    target_url = "https://python.org"
    scraped_title_file = os.path.join(base_dir, "scraped_titles.txt")

    title = scrape_webpage_title(target_url, scraped_title_file)
    print(f"    - Scraped Title for '{target_url}': '{title}'")
    
    assert "Python" in title, f"Expected 'Python' in scraped title, got '{title}'"
    assert os.path.exists(scraped_title_file), "Scraped title log file was not created"
    
    with open(scraped_title_file, "r", encoding="utf-8") as f:
        log_content = f.read()
    print("    - Log File Snippet:")
    print("      " + "\n      ".join(log_content.strip().split("\n")))
    print("    [OK] DEMO 3 PASSED: Webpage title scraped and saved successfully!")

    print("\n" + "=" * 60)
    print(" [ALL DEMOS COMPLETED SUCCESSFULLY!] All 3 automation tasks verified.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_demos()
