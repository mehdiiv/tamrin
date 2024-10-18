from django.test import TestCase
from building.models import Building
from django.contrib.auth.models import User

class BuildingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',  email = 'test@gmail.com', password='12345')
        self.building = Building.objects.create(
                creator_id = self.user.id ,
                built_year = '1995-12-12',
                room_number = '25',
                area = '123',
                floors = '3',
                Colour = 'yellow',                 
        )
        
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@gmail.com')      
            
    def test_building_creation(self):
        self.assertEqual(self.building.creator_id, self.user.id)
        self.assertEqual(self.building.built_year, '1995-12-12')
        self.assertEqual(self.building.room_number, '25')
        self.assertEqual(self.building.area, '123')
        self.assertEqual(self.building.floors, '3')
        self.assertEqual(self.building.Colour, 'yellow')
        
    def test_building_table_name(self):
        self.assertEqual(self.building._meta.db_table, 'building')