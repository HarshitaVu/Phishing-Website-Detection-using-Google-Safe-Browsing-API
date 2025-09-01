import sys
import requests

# Paste Google Safe Browsing API key here
API_KEY = "key_api"  # Replace with your full key

if not API_KEY:
    print("❌ Missing API key. Please add it to the script.")
    sys.exit(1)

API_URL = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

def check_urls(urls):
    payload = {
        "client": {"clientId": "phishing-detector", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": u} for u in urls]
        }
    }
    r = requests.post(API_URL, json=payload, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    if len(sys.argv) < 2:
        print("Usage: python safe_check.py <url1> [url2 url3 ...]")
        sys.exit(2)

    urls = sys.argv[1:]
    try:
        result = check_urls(urls)
    except requests.RequestException as e:
        print(f"❌ Network/API error: {e}")
        sys.exit(3)

    matches = result.get("matches", [])
    if not matches:
        for u in urls:
            print(f"✅ SAFE: {u} not flagged.")
        return

    # Build a quick lookup: url -> threat types
    flagged = {}
    for m in matches:
        u = m.get("threat", {}).get("url", "")
        t = m.get("threatType", "UNKNOWN")
        flagged.setdefault(u, set()).add(t)

    for u in urls:
        if u in flagged:
            kinds = ", ".join(sorted(flagged[u]))
            print(f"⚠️ DANGEROUS: {u} → {kinds}")
        else:
            print(f"✅ SAFE: {u} not flagged.")

if __name__ == "__main__":
    main()
