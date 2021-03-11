from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Tesing creating a new user with an email: successful"""
        email = 'testemail@thisisatest.com'
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

def test_new_user_email_normalized(self):
    """test the email for a new user, normalized"""
    email = 'testemail@THISISTEST.COM'
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email.lower())