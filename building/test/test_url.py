from django.test import SimpleTestCase
from building.views import (
    BuildingDetailView, BuildingListView,
    BuildingUpdateView, BuildingDeleteView,
   BuildingCreateView, SendEmailView
)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):
    def test_building_list_url(self):
        url = reverse('building_list')
        self.assertEqual(resolve(url).func.view_class, BuildingListView)
    
    def test_building_create_url(self):
        url = reverse('building_create')
        self.assertEqual(resolve(url).func.view_class, BuildingCreateView)
    
    def test_building_detail_url(self):
        url = reverse('building_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, BuildingDetailView)
    
    def test_building_update_url(self):
        url = reverse('building_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, BuildingUpdateView)
    
    def test_building_delete_url(self):
        url = reverse('building_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, BuildingDeleteView)

