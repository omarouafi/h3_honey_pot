from twisted.web import server, resource
from twisted.internet import reactor
from logger import setup_logger, log_attack
from elastic_client import send_to_elasticsearch
from alert import detect_attack_patterns, send_alert
from config import SERVER_PORT

logger = setup_logger()

class HoneypotHTTP(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        # Use getClientAddress() for reliability
        attacker_ip = request.getClientAddress().host
        request_uri = request.uri.decode("utf-8")

        logger.info(f"GET request from {attacker_ip} to {request_uri}")
        log_attack(attacker_ip, "GET", request_uri)
        send_to_elasticsearch(attacker_ip, "GET", request_uri)
        detect_attack_patterns(attacker_ip, "GET", request_uri)

        # Fake Admin Page to attract attackers
        if "/admin" in request_uri:
            return b"""
            <html><body>
                <h2>Admin Login</h2>
                <form method='POST' action='/admin'>
                    <input type='text' name='user' placeholder='Username'><br>
                    <input type='password' name='pass' placeholder='Password'><br>
                    <button type='submit'>Login</button>
                </form>
            </body></html>
            """

        # Default Page
        return b"<html><body><h1>Welcome to the vulnerable site! Find the secret admin page if you can.</h1></body></html>"

    def render_POST(self, request):
        attacker_ip = request.getClientAddress().host
        post_data = request.content.read().decode("utf-8")

        logger.info(f"POST request from {attacker_ip}: {post_data}")
        log_attack(attacker_ip, "POST", post_data)
        send_to_elasticsearch(attacker_ip, "POST", post_data)
        detect_attack_patterns(attacker_ip, "POST", post_data)

        return b"<html><body><h1>Thank you for your submission!</h1></body></html>"

if __name__ == "__main__":
    try:
        site = server.Site(HoneypotHTTP())
        reactor.listenTCP(SERVER_PORT, site)
        logger.info(f"Honeypot HTTP server running on port {SERVER_PORT}...")
        reactor.run()
    except Exception as e:
        logger.error(f"Failed to start honeypot: {e}")
