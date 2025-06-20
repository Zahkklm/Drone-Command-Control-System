from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserRegistrationTest(APITestCase):
    def test_register(self):
        url = reverse('user_register')
        data = {'username': 'testuser', 'password': 'testpass', 'role': 'operator'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class UserLoginTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.profile.role = 'operator'
        self.user.profile.save()

    def test_login(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

class UserProfileTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.profile.role = 'operator'
        self.user.profile.save()
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'})
        self.token = response.data['access']

    def test_profile(self):
        url = reverse('user_profile')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['role'], 'operator')