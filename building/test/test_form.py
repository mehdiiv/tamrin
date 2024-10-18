from building.forms import BuildingForm
from django.test import TestCase

class BuildingFormTest(TestCase):
    def test_Building_form_valid_data(self):
        form = BuildingForm(
            {'built_year' : '1995-12-12',
            'room_number' : 6,
            'area' : 123,
            'floors' : 53,
            'Colour' : 'blue',
        })
        self.assertTrue(form.is_valid())

    def test_Building_form_invalid_data(self):
        form = BuildingForm(
            {
            'built_year' : '1995-12-12',
            'area' : 123,
            'floors' : 53,
            'Colour' : 'blue',
        })
        self.assertFalse(form.is_valid())

    def test_Building_form_invalid_data(self):
        form = BuildingForm(
            {'room_number' : 6,
            'area' : 123,
            'floors' : 53,
            'Colour' : 'blue',
        })
        self.assertFalse(form.is_valid())

    def test_Building_form_invalid_data(self):
        form = BuildingForm(
            {'room_number' : 6,
            'built_year' : '1995-12-12',
            'floors' : 53,
            'Colour' : 'blue',
        })
        self.assertFalse(form.is_valid())
    
    def test_Building_form_invalid_data(self):
        form = BuildingForm(
            {'room_number' : 6,
            'built_year' : '1995-12-12',
            'area' : 123,
            'Colour' : 'blue',
        })
        self.assertFalse(form.is_valid())
    
    def test_Building_form_invalid_data(self):
        form = BuildingForm(
            {'room_number' : 6,
            'built_year' : '1995-12-12',
            'area' : 123,
            'floors' : 53,
        })
        self.assertFalse(form.is_valid())