from django.test import TestCase
from building.models import Building
from room.models import Room
from django.contrib.auth.models import User

class RoomModelTest(TestCase):
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
        self.room = Room.objects.create(
            building = self.building,
            room_name = 'testroom',
            area = '15',
            capacity = '1'
        )

    def test_room_creation(self):
        self.assertEqual(self.room.building, self.building)
        self.assertEqual(self.room.area, '15')
        self.assertEqual(self.room.room_name, 'testroom')
        self.assertEqual(self.room.capacity, '1')

    def test_building_table_name(self):
        self.assertEqual(self.room._meta.db_table, 'rooms')
