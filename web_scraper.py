"""
Web Scraper Script
Scrapes the title tag (<title>...</title>) of a specified webpage using HTTP requests
and extracts/saves the title to a text file using regular expressions (re) and file handling.
"""

import os
import re
import html
import datetime
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Regular expression to extract <title> tag content
TITLE_REGEX = r'<title[^>]*>(.*?)</title>'


def scrape_webpage_title(url: str, output_filepath: str = None, timeout: int = 10) -> str:
    """
    Fetches the HTML content of a URL, extracts the <title> tag, and optionally saves it to a file.

    :param url: Webpage URL to scrape.
    :param output_filepath: Optional path to save the scraped title.
    :param timeout: HTTP request timeout in seconds (default: 10).
    :return: Extracted webpage title.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TaskAutomationScraper/1.0'
    }

    logging.info(f"Sending HTTP GET request to: '{url}'")
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as req_err:
        logging.error(f"HTTP request failed: {req_err}")
        raise RuntimeError(f"Failed to fetch URL '{url}': {req_err}")

    # Extract title using regex
    match = re.search(TITLE_REGEX, response.text, re.IGNORECASE | re.DOTALL)
    if match:
        raw_title = match.group(1).strip()
        # Unescape HTML entities (e.g., &amp; -> &) and clean up whitespace
        clean_title = re.sub(r'\s+', ' ', html.unescape(raw_title))
    else:
        clean_title = "No <title> tag found"
        logging.warning("No <title> tag matching regular expression was found in webpage response.")

    logging.info(f"Successfully scraped title: '{clean_title}'")

    # Save to file if output_filepath is specified
    if output_filepath:
        output_dir = os.path.dirname(output_filepath)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(output_filepath, 'a', encoding='utf-8') as outfile:
            outfile.write(f"[{timestamp}] URL: {url}\nTitle: {clean_title}\n{'-'*60}\n")
        logging.info(f"Saved title log to: '{output_filepath}'")

    return clean_title


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scrape the title of a webpage and save it to a file.")
    parser.add_argument("-u", "--url", required=True, help="Webpage URL to scrape")
    parser.add_argument("-o", "--output", help="Output text file path to save the title log")

    args = parser.parse_args()

    try:
        title = scrape_webpage_title(args.url, args.output)
        print(f"\n[SUCCESS] Webpage Title: {title}")
    except Exception as err:
        print(f"\n[ERROR] {err}")
