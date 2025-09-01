
# 🛡️ Phishing Website Detection using Google Safe Browsing API

This project implements a phishing website detection system using the **Google Safe Browsing API**.
The Python script submits URLs to Google Safe Browsing, which checks them against its database of unsafe URLs.
It then reports whether a website is **Safe ✅** or **Dangerous ⚠️** (phishing, malware, or unwanted software).
---

## 📌 Features

* Integration with **Google Safe Browsing API v4** for real-time URL scanning
* Automated classification of websites into **Safe ✅** or **Dangerous ⚠️**
* JSON-based results including threat types: `MALWARE`, `SOCIAL_ENGINEERING`, `UNWANTED_SOFTWARE`
* Example test cases with both safe (Google, CBIT) and phishing/malicious URLs
* Easy-to-use Python script with minimal dependencies
---

## 📂 Repository Structure

Phishing-Website-Detection-using-Google-Safe-Browsing-API/
│
├── safe_check.py       # Main Python script
├── urls.txt            # Sample test URLs (safe + phishing)
├── Outputs/            # Screenshots of results
│   ├── safe.png        # Example of a safe website result
│   ├── malicious.png   # Example of a flagged website result
├── report/
│   ├── PhishingDetection_Report.pdf  # Final 2-page project report
└── README.md           # Documentation

---
## 🚀 How to Run

1. Clone this repository:
   bash
   git clone https://github.com/HarshitaVu/Phishing-Website-Detection-using-Google-Safe-Browsing-API.git
   cd Phishing-Website-Detection-using-Google-Safe-Browsing-API
2. Install dependencies:
   bash
   pip install requests
3. Open `safe_check.py` and replace the `API_KEY` variable with your personal **Google Safe Browsing API key**.
4. Run the script with URLs:
   bash
   python safe_check.py http://testsafebrowsing.appspot.com/s/phishing.html https://example.com

## 📊 Results

| URL                                                                                                        | Result    | Outcome     |
| ---------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| google.com                                                                                                 | safe      | ✅ Safe      |
| cbit.ac.in                                                                                                 | safe      | ✅ Safe      |
| [http://testsafebrowsing.appspot.com/s/phishing.html](http://testsafebrowsing.appspot.com/s/phishing.html) | dangerous | ⚠️ Phishing |
| [http://malicious-example.com](http://malicious-example.com)                                               | dangerous | ⚠️ Phishing |

Outputs are stored in the `Outputs/` folder as screenshots (`safe.png`, `malicious.png`).
---
## 👩‍💻 Author
Harshita Vuthaluru
B.Tech IT-2, CBIT


