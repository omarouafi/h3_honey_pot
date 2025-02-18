import requests
import time
from urllib.parse import urljoin

LOGIN_URL = "http://127.0.0.1:5000/login"
BASE_URL = "http://127.0.0.1:5000"
USERNAME = "hacker"
PASSWORD = "123456"
ATTACK_ATTEMPTS = 60 

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
