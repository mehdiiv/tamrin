from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class NewsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='1223234')
        self.client = Client()
        self.client.login(username='test', password='1223234')
        
    def test_login_view(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
    
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))