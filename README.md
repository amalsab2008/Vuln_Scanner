# Vuln_Scanner

A simple web vulnerability scanner written in Python designed to discover basic vulnerabilities like **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)** on target web applications. The project also contains a sample vulnerable application to test the scanner safely.

## Project Structure

```text
Vuln_scanner/
│
├── vulnerable_app/
│   └── vulnerable.py       # A Flask web application containing intentional vulnerabilities for testing.
│
├── crawler.py              # Crawls target pages and extracts links.
├── form_parser.py          # Parses forms from HTML pages.
├── sqli_scanner.py         # Performs basic SQL injection checks.
├── xss_scanner.py          # Performs basic XSS injection checks.
├── report_generator.py     # Writes scan results to a txt file.
├── scanner.py              # Main execution script to orchestrate scanners.
├── requirements.txt        # Python package dependencies.
└── README.md               # Project documentation.
```

## Features

- **XSS Scanning**: Tests target URL endpoints for reflected Cross-Site Scripting using a basic payload `<script>alert('XSS')</script>`.
- **SQL Injection (SQLi) Scanning**: Injects payloads (e.g. `' OR '1'='1`) into query parameters to check if the database engine returns error messages indicative of vulnerable inputs.
- **Crawling & Form Parsing**: Crawls standard links and parses form actions.
- **Reporting**: Stores findings inside a generated `report.txt` file.

## Setup and Installation

### Prerequisites

- Python 3.x
- pip

### Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## How to Run

### 1. Start the Vulnerable App
Run the test vulnerable Flask application on your local machine:

```bash
python vulnerable_app/vulnerable.py
```
This application starts on `http://127.0.0.1:5000/`.

### 2. Run the Vulnerability Scanner
While the vulnerable app is running, execute the scanner:

```bash
python scanner.py
```

After scanning completes, you should see the results in terminal output and a new `report.txt` file created in the project root:
```text
[+] XSS Vulnerability Found
[+] SQL Injection Found
```

## Disclaimer

This scanner is developed for educational and vulnerability demonstration purposes only. Do not scan websites or systems without explicit permission from their owners.
