import logging
from pythonjsonlogger import jsonlogger

def setup_logger():
    logger = logging.getLogger("honeypot_logger")
    logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler("honeypot.log")
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger

logger = setup_logger()

def log_attack(attacker_ip, method, details):
    logger.info({
        "attacker_ip": attacker_ip,
        "method": method,
        "details": details
    })
