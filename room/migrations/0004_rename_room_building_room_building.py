# Generated by Django 5.1.1 on 2024-10-20 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_room_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_building',
            new_name='building',
        ),
    ]