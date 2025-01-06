import requests
from bs4 import BeautifulSoup
import re

def phishing_detection(url):
    """Check if the URL is part of a phishing campaign."""
    suspicious_keywords = ["login", "secure", "account", "update", "password"]
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        print(f"[!] Phishing detected: {url}")
    else:
        print("no phishing risks found")

def scan_broken_authentication(url):
    """Detect broken authentication mechanisms."""
    # Try accessing a page without proper login (simulating unauthenticated access to restricted pages)
    restricted_url = f"{url}/admin"
    response = requests.get(restricted_url)
    if response.status_code == 200:
        print("[!] Broken Authentication Detected! Unauthorized access is possible.")
    else:
         print("No broken authentication detected")

def scan_sql_injection(url):
    """Check for SQL Injection vulnerabilities."""
    payload = "' OR '1'='1"
    test_url = f"{url}?id={payload}"
    response = requests.get(test_url)
    if "error" in response.text.lower() or "mysql" in response.text.lower() or "syntax" in response.text.lower():
        print("[!] Potential SQL Injection vulnerability found!")
    else:
        print("[+] No SQL Injection vulnerability detected.")

def scan_xss(url):
    """Check for XSS vulnerabilities."""
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?search={payload}"
    response = requests.get(test_url)
    if payload in response.text:
        print("[!] Potential XSS vulnerability found!")
    else:
        print("[+] No XSS vulnerability detected.")

def scan_insecure_headers(url):
    """Check for insecure headers."""
    response = requests.get(url)
    headers = response.headers
    missing_headers = []
    if "X-Content-Type-Options" not in headers:
        missing_headers.append("X-Content-Type-Options")
    if "Content-Security-Policy" not in headers:
        missing_headers.append("Content-Security-Policy")
    if "Strict-Transport-Security" not in headers:
        missing_headers.append("Strict-Transport-Security")
    
    if missing_headers:
        print("[!] Missing secure headers:")
        for header in missing_headers:
            print(f"    - {header}")
    else:
        print("[+] All secure headers are present.")

def find_forms(url):
    """Check for forms on the webpage."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")
    if forms:
        print(f"[+] Found {len(forms)} forms on the page:")
        for i, form in enumerate(forms, 1):
            print(f"    Form {i}: {form.get('action')}")
    else:
        print("[-] No forms found on the page.")

def main():
    print("Website Vulnerability Scanner")
    url = input("Enter the website URL (e.g., https://example.com): ").strip()

    print("\n[1] Scanning for SQL Injection...")
    scan_sql_injection(url)

    print("\n[2] Scanning for XSS...")
    scan_xss(url)

    print("\n[3] Scanning for insecure headers...")
    scan_insecure_headers(url)

    print("\n[4] Searching for forms on the page...")
    find_forms(url)

    print("\n[5] Checking for phishing risks...")
    phishing_detection(url)

    print("\n[6] Scanning for broken authentication...")
    scan_broken_authentication(url)

    print("\nScan complete!")

if __name__ == "__main__":
    main()