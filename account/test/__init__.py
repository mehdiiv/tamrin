from account.forms import UserLogin 
from django.test import TestCase
  
class UserLoginFormTest(TestCase):
    
    def test_user_login_form_valid_data(self):
        form = UserLogin({'username' : 'samplpusername',
            'password' : '1231241',
        })
        self.assertTrue(form.is_valid())

    def test_news_login_form_invalid_data(self):
        form = UserLogin(
            {'username' : 'samplpusername',
        })
        self.assertFalse(form.is_valid())

    def test_news_login_form_invalid_data(self):
        form = UserLogin(
            {'password' : '1231241',
        })
        self.assertFalse(form.is_valid())

    def test_news_login_form_field_attributes(self):
        form = UserLogin()
        self.assertEqual(form.fields['username'].widget.attrs['class'], 'form-control')        
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'Username')
        self.assertEqual(form.fields['password'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['password'].widget.attrs['placeholder'], 'Password')