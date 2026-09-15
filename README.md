# 🐍 Task Automation with Python Scripts

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Internship Task](https://img.shields.io/badge/CodeAlpha-Task%203-orange.svg)](https://codealpha.tech/)

A modular Python task automation toolkit built for **CodeAlpha Internship (Task 3)**. This repository contains scripts that automate common real-life repetitive tasks using core Python libraries and standard programming practices.

---

## 💡 Automated Tasks Included

This repository implements **all three** task automation ideas:

1. **📷 JPG File Organizer (`file_organizer.py`)**
   - Automatically scans a folder for `.jpg` and `.jpeg` files.
   - Moves or copies them into a dedicated destination folder using Python's `os` and `shutil` modules.

2. **✉️ Email Address Extractor (`email_extractor.py`)**
   - Reads any `.txt` file and extracts all valid email addresses using regular expressions (`re`).
   - Deduplicates and saves extracted emails to a clean output text file using standard file handling (`open`, `write`).

3. **🌐 Webpage Title Scraper (`web_scraper.py`)**
   - Sends HTTP GET requests to a specified URL using `requests`.
   - Extracts the `<title>` tag using `re` and logs the scraped title with timestamps to a file.

4. **🖥️ Interactive CLI & Demo Suite (`main.py` & `demo.py`)**
   - Interactive terminal menu to easily select and execute any script.
   - Automated demo script with dummy test file generation for instant end-to-end verification.

---

## 🛠️ Key Concepts Used

- **`os`**: Directory traversal, path manipulation, checking file existence, creating target folders (`os.makedirs`).
- **`shutil`**: Moving (`shutil.move`) and copying (`shutil.copy2`) files across directories.
- **`re`**: Pattern matching for RFC-compliant email matching (`EMAIL_REGEX`) and HTML tag parsing (`<title>`).
- **`requests`**: Fetching webpage content over HTTP with headers and timeout configurations.
- **File Handling**: Reading and writing text files (`open`, `read`, `write`) with UTF-8 encoding.

---

## 📂 Project Structure

```text
Task-Automation-Python/
│── file_organizer.py    # JPG file organizer module (os, shutil)
│── email_extractor.py   # Regex email extractor module (re, file handling)
│── web_scraper.py       # Web title scraper module (requests, re)
│── main.py              # Interactive CLI menu runner
│── demo.py              # Automated test & verification suite
│── requirements.txt     # Python dependencies
│── .gitignore           # Ignored files and folders
└── README.md            # Documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8 or higher installed on your system.

### 2. Installation
Clone the repository and install required dependencies:
```bash
git clone https://github.com/YOUR_USERNAME/task-automation-python.git
cd task-automation-python
pip install -r requirements.txt
```

---

## 🎯 Usage

### Option A: Interactive CLI Menu (Recommended)
Launch the unified interactive runner:
```bash
python main.py
```

### Option B: Run Automated Test Suite
Test all three automation modules with generated dummy data:
```bash
python demo.py
```

### Option C: Standalone Script Execution

#### 1. Move JPG Files
```bash
python file_organizer.py --source "./my_photos" --destination "./jpg_folder"
```
*Optional flag `--copy` to copy files instead of moving them.*

#### 2. Extract Emails from Text File
```bash
python email_extractor.py --input "document.txt" --output "extracted_emails.txt"
```

#### 3. Scrape Webpage Title
```bash
python web_scraper.py --url "https://python.org" --output "scraped_titles.txt"
```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

Developed for **CodeAlpha Internship - Task 3**.
