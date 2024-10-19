from django.db import models
from building.models import Building

class Room(models.Model):
    room_building = models.ForeignKey(Building, on_delete = models.CASCADE)
    room_name = models.CharField(max_length = 32)
    area = models.IntegerField()
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'room'