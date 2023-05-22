# Import necessary libraries
import unittest
from app import app

# Define test cases

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the MathGPT Webapp', response.data)

    def test_add(self):
        response = self.app.post('/add', data=dict(num1=2, num2=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'5', response.data)

    def test_subtract(self):
        response = self.app.post('/subtract', data=dict(num1=5, num2=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2', response.data)

    def test_multiply(self):
        response = self.app.post('/multiply', data=dict(num1=2, num2=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'6', response.data)

    def test_divide(self):
        response = self.app.post('/divide', data=dict(num1=6, num2=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2.0', response.data)

        response = self.app.post('/divide', data=dict(num1=6, num2=0))
        self.assertIn(b'Error: Division by zero', response.data)

# Run tests
if __name__ == '__main__':
    unittest.main()