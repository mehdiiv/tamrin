from django.test import TestCase, Client
from django.urls import reverse
from building.models import Building
from django.contrib.auth.models import User
from room.views import Room

class RoomViewTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='test', password='1223234')
    self.client = Client()
    self.client.login(username='test', password='1223234')
    self.building = Building.objects.create(creator = self.user, built_year = '1995-12-12',room_number = '25',area = '123',floors = '3',Colour = 'yellow')
    self.room = Room.objects.create(building = self.building, area = '12', capacity = '53', room_name = 'testroom' )


  def test__list_view(self):
    response = self.client.get(reverse('rooms_list', kwargs={ 'pk': self.building.id }))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'room/list.html')
    self.assertContains(response, self.room.building)

  def test_room_list_view_logout_auth_user(self):
    logout_client = Client()
    response = logout_client.get(reverse('rooms_list', kwargs={ 'pk': self.building.id}))
    self.assertEqual(response.status_code, 302)

  def test_room_detail_view(self):
    response = self.client.get(reverse('room_create', kwargs= { 'pk': self.building.id }))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'room/form.html')
    self.assertContains(response, self.building.creator)

  def test_room_detail_view_logout_auth_user(self):
    logout_client = Client()
    response = logout_client.get(reverse('room_detail', kwargs={ 'pk': self.building.id ,'room_pk' : self.room.id }))
    self.assertEqual(response.status_code, 302)

  def test_room_create_view(self):
    response = self.client.post(reverse('room_create', kwargs= { 'pk': self.building.id }), { 'area' : '12' ,'capacity' : '53','room_name' : 'testroom'})
    self.assertEqual(response.status_code, 302)

  def test_room_update_view(self):
        response = self.client.post(reverse('room_update', kwargs={ 'pk': self.building.id ,'room_pk' : self.room.id }), { 'area' : '12' ,'capacity' : '53','room_name' : 'updateroom'})
        self.assertEqual(response.status_code, 302)
        self.room.refresh_from_db()
        self.assertEqual(self.room.room_name, 'updateroom')
