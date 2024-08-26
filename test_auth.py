import unittest
from app import app, db
from models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.app.post('/api/register', json={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        user = User(username='testuser', password_hash='password123')
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/api/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
