import unittest
from unittest.mock import patch, MagicMock
from twisted.web.test.requesthelper import DummyRequest
from honeypot_http import HoneypotHTTP

class TestHoneypotHTTP(unittest.TestCase):

    def setUp(self):
        self.honeypot = HoneypotHTTP()

    @patch('honeypot_http.log_attack')
    @patch('honeypot_http.send_to_elasticsearch')
    @patch('honeypot_http.detect_attack_patterns')
    def test_render_GET_default_page(self, mock_detect, mock_elastic, mock_log):
        request = DummyRequest([b'/'])
        request.client = b'127.0.0.1'

        response = self.honeypot.render_GET(request)

        self.assertIn(b"Welcome to the vulnerable site", response)
        mock_log.assert_called_with('127.0.0.1', 'GET', '/')
        mock_elastic.assert_called_with('127.0.0.1', 'GET', '/')
        mock_detect.assert_called_with('127.0.0.1', 'GET', '/')

    @patch('honeypot_http.log_attack')
    @patch('honeypot_http.send_to_elasticsearch')
    @patch('honeypot_http.detect_attack_patterns')
    def test_render_GET_admin_page(self, mock_detect, mock_elastic, mock_log):
        request = DummyRequest([b'/admin'])
        request.client = b'127.0.0.1'

        response = self.honeypot.render_GET(request)

        self.assertIn(b"Admin Login", response)
        mock_log.assert_called_with('127.0.0.1', 'GET', '/admin')
        mock_elastic.assert_called_with('127.0.0.1', 'GET', '/admin')
        mock_detect.assert_called_with('127.0.0.1', 'GET', '/admin')

    @patch('honeypot_http.log_attack')
    @patch('honeypot_http.send_to_elasticsearch')
    @patch('honeypot_http.detect_attack_patterns')
    def test_render_POST(self, mock_detect, mock_elastic, mock_log):
        request = DummyRequest([b'/submit'])
        request.client = b'127.0.0.1'
        request.content.write(b'user=admin&pass=1234')
        request.content.seek(0)

        response = self.honeypot.render_POST(request)

        self.assertIn(b"Thank you for your submission", response)
        mock_log.assert_called_with('127.0.0.1', 'POST', 'user=admin&pass=1234')
        mock_elastic.assert_called_with('127.0.0.1', 'POST', 'user=admin&pass=1234')
        mock_detect.assert_called_with('127.0.0.1', 'POST', 'user=admin&pass=1234')

if __name__ == '__main__':
    unittest.main()
