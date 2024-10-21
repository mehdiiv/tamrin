from django.test import SimpleTestCase
from room.views import (
    RoomDetailView, RoomListView,
   RoomCreateView,
)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):
    def test_room_list_url(self):
        url = reverse('rooms_list', kwargs={'pk': 1 })
        self.assertEqual(resolve(url).func.view_class, RoomListView)
    
    def test_room_create_url(self):
        url = reverse('room_create',kwargs={'pk': 1 })
        self.assertEqual(resolve(url).func.view_class, RoomCreateView)
    
    def test_room_detail_url(self):
        url = reverse('room_detail',kwargs={'pk': 1,'room_pk' : 1 })
        self.assertEqual(resolve(url).func.view_class, RoomDetailView)
    


