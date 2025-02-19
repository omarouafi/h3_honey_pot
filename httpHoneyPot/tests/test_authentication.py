import unittest
import time
from flask import session
from httpHoneyPot.login import app
from httpHoneyPot.fakeLogin import app as fake_app

class AuthenticationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        app.testing = True
        app.secret_key = 'your_secret_key'
        self.client.get('/')

    def test_valid_login(self):
        """Test valid login: should redirect to /dashboard."""
        response = self.client.post('/login', data={'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/dashboard')

    def test_invalid_login(self):
        "Test invalid login:."
        response = self.client.post('/login', data={'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')  
        with self.client.session_transaction() as sess:
            self.assertNotIn('username', sess)

    def test_logout(self):
        "Test logout functionality: after logout, user should be redirected to / and session cleared."
        with self.client:
            self.client.post('/login', data={'username': 'user', 'password': 'password'})
            response = self.client.get('/logout')
            self.assertEqual(response.status_code, 302) 
            self.assertEqual(response.location, '/')
            with self.client.session_transaction() as sess:
                self.assertNotIn('username', sess)

    def test_session_after_login(self):
        "Test that after login, accessing /dashboard returns 200 and contains a welcome message."
        self.client.post('/login', data={'username': 'user', 'password': 'password'})
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, user!', response.data)

    def test_fake_login_redirection(self):
        "Test that if we trigger the honeypot, the app would redirect to /fake-login."
        app.testing = False  
        self.client.post('/login', data={'username': 'wronguser', 'password': 'wrongpassword'})
        response = self.client.post('/login', data={'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost:5003/fake-login')
        app.testing = True

if __name__ == "__main__":
    unittest.main()
