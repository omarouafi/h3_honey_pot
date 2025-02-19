"""
hacker_attacks_script.py
========================

This script simulates an automated hacker attack against the Flask login application.
It sends multiple login requests rapidly to the login endpoint. If a redirect is detected,
the script assumes that the server has redirected to the honeypot (fake login page)
and continues to send login attempts to that URL.

Key Features:
  - Sends rapid POST requests to the login endpoint.
  - Detects redirection via the "Location" header.
  - Constructs a full URL for the redirect if necessary.
  - Simulates further attack attempts on the redirected (honeypot) page.
  - Introduces a short delay between each attempt to mimic bot-like behavior.
"""

import requests
import time
from urllib.parse import urljoin

LOGIN_URL = "http://127.0.0.1:5000/login"
BASE_URL = "http://127.0.0.1:5000"
USERNAME = "hacker"
PASSWORD = "123456"
ATTACK_ATTEMPTS = 60

def simulate_attack():
    """
    Simulate the hacker attack by sending rapid login requests.
    
    If a redirect is detected in the response headers (indicating that the login attempt
    has been routed to the honeypot), the script constructs the absolute URL and sends
    an additional POST request to that URL.
    """
    session = requests.Session()
    print("[+] Starting automated attack...")
    for i in range(ATTACK_ATTEMPTS):
        data = {"username": USERNAME, "password": PASSWORD}
        response = session.post(LOGIN_URL, data=data, allow_redirects=False)
        if "Location" in response.headers:
            redirected_url = response.headers["Location"]
            full_redirected_url = urljoin(BASE_URL, redirected_url)
            print(f"[!] Redirect detected to {full_redirected_url} on attempt {i+1}")
            fake_response = session.post(full_redirected_url, data=data)
            print(f"[!] Sent fake login attempt {i+1} - Status Code: {fake_response.status_code}")
        else:
            print(f"[!] Sent login attempt {i+1} - Status Code: {response.status_code}")
        time.sleep(0.3)
    print("[+] Attack simulation completed.")

if __name__ == "__main__":
    simulate_attack()
