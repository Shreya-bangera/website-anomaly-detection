# 🔎 Website Vulnerability Scanner

A simple Python-based Website Vulnerability Scanner that checks for common web security issues such as:

- SQL Injection
- Cross-Site Scripting (XSS)
- Insecure HTTP Headers
- Broken Authentication
- Phishing Risk Indicators
- HTML Form Detection

This project demonstrates basic web security testing techniques using Python.

---

## 🛠 Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- Regular Expressions (re)

---

## 📂 Project Structure

```
├── vulnerability_scanner.py
├── README.md
```

---

## ⚙️ Installation

### 1️⃣ Install Required Libraries

```bash
pip install requests
pip install beautifulsoup4
```

---

## 🚀 How to Run

```bash
python vulnerability_scanner.py
```

When prompted, enter a website URL:

Example:
```
https://example.com
```

---

## 🔍 Features & What It Checks

### 1️⃣ SQL Injection Detection

- Sends payload: `' OR '1'='1`
- Checks for database error messages in response
- Detects possible SQL syntax exposure

---

### 2️⃣ Cross-Site Scripting (XSS) Detection

- Sends JavaScript payload:
  ```
  <script>alert('XSS')</script>
  ```
- Checks if payload reflects back in response

---

### 3️⃣ Insecure HTTP Headers Check

Checks if the following security headers are missing:

- X-Content-Type-Options
- Content-Security-Policy
- Strict-Transport-Security

Missing headers may indicate weak security configuration.

---

### 4️⃣ Broken Authentication Check

- Attempts access to `/admin` endpoint
- If accessible without authentication → potential vulnerability

---

### 5️⃣ Phishing Risk Detection

- Checks URL for suspicious keywords:
  - login
  - secure
  - account
  - update
  - password

---

### 6️⃣ Form Detection

- Identifies HTML `<form>` elements on the webpage
- Displays form action URLs

---

## 🛑 Important Disclaimer

⚠️ This tool is created for educational purposes only.

Do NOT use this scanner on websites you do not own or do not have permission to test.

Unauthorized security testing may be illegal.

---

## 🚀 Future Improvements

- Add multithreading for faster scanning
- Add detailed vulnerability reports (PDF)
- Add port scanning feature
- Add CSRF detection
- Add SSL certificate validation
- GUI interface using Tkinter
- Add logging system
- Improve SQLi/XSS detection accuracy

---

## 🎯 Learning Outcomes

This project helps understand:

- Basic web vulnerability patterns
- HTTP request handling
- Response analysis
- Security headers importance
- Ethical hacking fundamentals

---

## 👩‍💻 Author

Shreya S  
Final Year – Information Science Engineering  

---

## 📜 License

This project is developed for educational and research purposes only.
