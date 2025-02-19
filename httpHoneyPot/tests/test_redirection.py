import unittest
import time
from flask import session
from login import app  # Your main application
from fakeLogin import app as fake_app

class RedirectionTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.fake_client = fake_app.test_client()

    def setUp(self):
        app.testing = False
        fake_app.testing = False
        app.secret_key = 'your_secret_key'
        fake_app.secret_key = 'your_secret_key'
        self.client.get('/')

    def test_redirect_to_fake_login_on_fast_login(self):
        "Test that a fast second login attempt triggers a redirect to /fake-login."
        self.client.post('/login', data={'username': 'user', 'password': 'wrongpassword'})
        response = self.client.post('/login', data={'username': 'user', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost:5003/fake-login')

    def test_redirect_after_logout(self):
        "Test that after logout, the user is redirected to the home page."
        self.client.post('/login', data={'username': 'user', 'password': 'password'})
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.endswith('/'))

    def test_fake_login_redirects(self):
        "Test that after multiple rapid failed login attempts, the user is redirected to /fake-login."
        for _ in range(3):
            self.client.post('/login', data={'username': 'user', 'password': 'wrongpassword'})
        response = self.client.post('/login', data={'username': 'user', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/fake-login', response.location)

if __name__ == "__main__":
    unittest.main()
