from django.test import SimpleTestCase
from room.views import (
    RoomDetailView, RoomsListView,
   RoomCreateView,RoomDeleteView,
   RoomUpdateView
)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):
    def test_room_list_url(self):
        url = reverse('rooms_list', kwargs={'pk': 1 })
        self.assertEqual(resolve(url).func.view_class, RoomsListView)

    def test_room_create_url(self):
        url = reverse('room_create',kwargs={'pk': 1 })
        self.assertEqual(resolve(url).func.view_class, RoomCreateView)

    def test_room_detail_url(self):
        url = reverse('room_detail',kwargs={'pk': 1,'room_pk' : 1 })
        self.assertEqual(resolve(url).func.view_class, RoomDetailView)

    def test_news_update_url(self):
        url = reverse('room_update', kwargs={'pk': 1,'room_pk' : 1 })
        self.assertEqual(resolve(url).func.view_class, RoomUpdateView)

    def test_news_delete_url(self):
        url = reverse('room_delete', kwargs={'pk': 1,'room_pk' : 1 })
        self.assertEqual(resolve(url).func.view_class, RoomDeleteView)
