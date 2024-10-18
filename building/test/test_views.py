from django.test import TestCase, Client
from django.urls import reverse
from building.models import Building
from django.contrib.auth.models import User

class NewsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='1223234')
        self.client = Client()
        self.client.login(username='test', password='1223234')

        self.building = Building.objects.create(creator = self.user, built_year = '1995-12-12',room_number = '25',area = '123',floors = '3',Colour = 'yellow')
        
    def test__list_view(self):
        response = self.client.get(reverse('building_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'building/list.html')
        self.assertContains(response, self.building.creator)
    
    def test_building_list_view_logout_auth_user(self):
        logout_client = Client()
        response = logout_client.get(reverse('building_list'))
        self.assertEqual(response.status_code, 302)
    
    def test_building_detail_view(self):
        response = self.client.get(reverse('building_detail', kwargs={ 'pk': self.building.id }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'building/detail.html')
        self.assertContains(response, self.building.creator)
    
    def test_building_detail_view_logout_auth_user(self):
        logout_client = Client()
        response = logout_client.get(reverse('building_detail', kwargs={ 'pk': self.building.id }))
        self.assertEqual(response.status_code, 302)
    
    def test_building_create_view(self):
        response = self.client.post(reverse('building_create'),{ 'built_year' : '1995-12-12', 'room_number' : '25' ,
                                                            'area' : '123' , 'floors' : '3', 'Colour' : 'yellow'

        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Building.objects.filter(built_year = '1995-12-12').exists())
    
    def test_new_update_view(self):
        response = self.client.post(reverse('building_update', kwargs={ 'pk': self.building.id }), { 'built_year' : '1995-12-12', 'room_number' : '69' ,
                                                            'area' : '123' , 'floors' : '3', 'Colour' : 'yellow'
            
        })
        self.assertEqual(response.status_code, 302)
        self.building.refresh_from_db()
        self.assertEqual(self.building.room_number, 69)
    
    def test_login_view(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
    
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))