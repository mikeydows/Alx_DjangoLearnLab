from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        # Profile is automatically created via signal, no need to add manually
        self.client.login(username="tester", password="password")

    def test_profile_update(self):
        resp = self.client.post(reverse('profile'), {
            'username': 'updater',
            'email': 'new@example.com',
            'bio': 'Hello',
        }, follow=True)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updater')
        self.assertEqual(self.user.profile.bio, 'Hello')
