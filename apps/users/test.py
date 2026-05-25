from django.test import TestCase
from django.contrib.auth.models import User

class RegisterTestCase(TestCase):
    def test_register_user(self):
        response = self.client.post('/api/register/', {
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)