# Generated by Django 4.1.4 on 2023-01-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_name_sensor_sensor_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='sensor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='temperaturemeasurement',
            old_name='sensor_name',
            new_name='sensor_id',
        ),
    ]