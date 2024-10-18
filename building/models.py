from django.db import models
from django.contrib.auth.models import User


class Building(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    built_year = models.DateField()
    room_number = models.IntegerField()
    area = models.FloatField()
    floors = models.IntegerField()
    Colour = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'building'