# Generated by Django 4.0.2 on 2022-03-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_vehicle_cargo_volume_vehicle_engine_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
