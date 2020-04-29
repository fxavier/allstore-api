from django.test import TestCase
from django.contrib.auth import get_user_model
from ...core import models


# def sample_user(email='test@allstore.com', password='testpass'):
#     """Create a simple user"""
#     return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful """
        email = 'test@alstore.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized """
        email = 'test@ALLSTORE.COM'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email, password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'testsuper@allstore.com',
            'pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # def test_order_str(self):
    #     """Test the order string representation"""
    #     email = 'test@alstore.com'
    #     password = 'test123'
    #     order = models.Order.objects.create(
    #         user=get_user_model().objects.create_user(email, password),
    #         ordered=True
    #     )
    #
    #     self.assertEqual(str(order), order.user.email)
