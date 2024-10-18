from django.test import SimpleTestCase
from account.views import (LogoutView ,LoginView)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)
    
    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)
