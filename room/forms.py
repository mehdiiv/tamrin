from django import forms
from room.models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'area', 'capacity',]