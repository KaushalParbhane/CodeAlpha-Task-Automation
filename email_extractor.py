"""
Email Extractor Script
Extracts all email addresses from a text file using regular expressions (re)
and saves them to a destination text file using Python file handling.
"""

import os
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Standard RFC-compliant regex for matching email addresses
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


def extract_emails(input_filepath: str, output_filepath: str, sort_results: bool = True) -> list:
    """
    Reads a text file, extracts unique email addresses, and saves them to an output file.

    :param input_filepath: Path to the source text file.
    :param output_filepath: Path to save the extracted emails.
    :param sort_results: If True, sorts emails alphabetically before saving.
    :return: List of unique extracted email addresses.
    """
    if not os.path.exists(input_filepath):
        logging.error(f"Input file not found: '{input_filepath}'")
        raise FileNotFoundError(f"Input file '{input_filepath}' does not exist.")

    logging.info(f"Reading file: '{input_filepath}'")
    
    with open(input_filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        content = infile.read()

    # Find all matches using regex
    raw_matches = re.findall(EMAIL_REGEX, content)
    
    # Normalize to lowercase and remove duplicates preserving order or sorted
    unique_emails = list(dict.fromkeys(email.lower() for email in raw_matches))
    if sort_results:
        unique_emails.sort()

    logging.info(f"Found {len(unique_emails)} unique email address(es).")

    # Ensure parent output directory exists
    output_dir = os.path.dirname(output_filepath)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Save to output file
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        for email in unique_emails:
            outfile.write(email + '\n')

    logging.info(f"Successfully saved emails to: '{output_filepath}'")
    return unique_emails


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract email addresses from a text file.")
    parser.add_argument("-i", "--input", required=True, help="Input text file path")
    parser.add_argument("-o", "--output", required=True, help="Output text file path")

    args = parser.parse_args()

    try:
        emails = extract_emails(args.input, args.output)
        print(f"\n[SUCCESS] Extracted {len(emails)} email(s):")
        for e in emails:
            print(f"  - {e}")
    except Exception as err:
        print(f"\n[ERROR] {err}")
