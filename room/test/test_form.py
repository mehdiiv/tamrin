from room.forms import RoomForm
from django.test import TestCase

class RoomFormTest(TestCase):
    def test_room_form_valid_data(self):
        form = RoomForm(
            {'area' : 123,
            'capacity' : 53,
            'room_name' : 'bath',
        })
        self.assertTrue(form.is_valid())

    def test_Building_form_invalid_data_without_area(self):
        form = RoomForm(
            {'capacity' : 53,
            'room_name' : 'bath',
        })
        self.assertFalse(form.is_valid())
    
    def test_Building_form_invalid_data_without_capacity(self):
        form = RoomForm(
            {'area' : 123,
            'room_name' : 'bath',
        })
        self.assertFalse(form.is_valid())
    
    def test_Building_form_invalid_data_without_room_name(self):
        form = RoomForm(
            {'area' : 123,
            'capacity' : 53,
        })
        self.assertFalse(form.is_valid())