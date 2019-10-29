from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    #ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Welcome' in response.data)

    #ensure login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
        '/login',
        data=dict(username="admin",password="admin"),
        follow_redirects = True
        )
        self.assertIn(b'Title', response.data)

    #ensure login behaves correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
        '/login',
        data=dict(username="admin1",password="admin"),
        follow_redirects = True
        )
        self.assertIn(b'Invalid Credentials. Please try again.', response.data)
    #ensure login behaves correctly given the correct credentials
    
if __name__ == '__main__':
    unittest.main()