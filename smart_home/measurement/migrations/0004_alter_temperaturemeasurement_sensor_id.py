# Generated by Django 4.1.4 on 2023-01-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_rename_sensor_name_sensor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturemeasurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]