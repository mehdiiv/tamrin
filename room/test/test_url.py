from django.test import SimpleTestCase
from room.views import (
    RoomDetailView, RoomListView,
   RoomCreateView,
)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):
    def test_room_list_url(self):
        url = reverse('rooms_list')
        self.assertEqual(resolve(url).func.view_class, RoomListView, pk = 1, room_pk =1)
    
    def test_room_create_url(self):
        url = reverse('room_create')
        self.assertEqual(resolve(url).func.view_class, RoomCreateView, pk = 1, room_pk =1)
    
    def test_room_detail_url(self):
        url = reverse('room_detail',pk = 1, room_pk =1)
        self.assertEqual(resolve(url).func.view_class, RoomDetailView)
    


