from xss_scanner import scan_xss
from sqli_scanner import scan_sqli
from report_generator import generate_report

results = []

if scan_xss("http://127.0.0.1:5000/search"):
    results.append("[+] XSS Vulnerability Found")

if scan_sqli("http://127.0.0.1:5000/login"):
    results.append("[+] SQL Injection Found")

generate_report(results)

print(results)