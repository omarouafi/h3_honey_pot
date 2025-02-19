from elasticsearch import Elasticsearch
from logger import logger

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

def send_to_elasticsearch(attacker_ip, method, details):
    doc = {
        "attacker_ip": attacker_ip,
        "method": method,
        "details": details
    }
    try:
        es.index(index="honeypot-logs", body=doc)
        logger.info(f"Logged to Elasticsearch: {doc}")
    except Exception as e:
        logger.error(f"Failed to log to Elasticsearch: {e}")
