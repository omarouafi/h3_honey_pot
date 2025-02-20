import smtplib
from email.mime.text import MIMEText
from collections import defaultdict
from logger import logger
from config import EMAIL_CONFIG

attack_counts = defaultdict(int)

def detect_attack_patterns(attacker_ip, method, details):
    attack_counts[attacker_ip] += 1

    if attack_counts[attacker_ip] > EMAIL_CONFIG["alert_threshold"]:
        logger.warning(f"Repeated attack from {attacker_ip}")
        send_alert(attacker_ip, "Repeated Attack Detected")

def send_alert(attacker_ip, attack_type):
    sender_email = EMAIL_CONFIG["sender"]
    receiver_email = EMAIL_CONFIG["receiver"]
    password = EMAIL_CONFIG["password"]

    subject = f" Honeypot Alert: {attack_type}"
    message = f"Suspicious activity detected from {attacker_ip}: {attack_type}"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        logger.info(f"ALERT SENT : {attack_type} from {attacker_ip}")
    except Exception as e:
        logger.error(f"Failed to send alert: {e}")
