# Generated by Django 4.0.2 on 2022-03-06 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('value', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drivetrain',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GearType',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('value', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('value', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('horse_power', models.IntegerField()),
                ('seat_count', models.IntegerField()),
                ('milage', models.IntegerField(default=0)),
                ('engine_capacity', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('cargo_volume', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=2000)),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Power Steering', 'Power Steering'), ('AC', 'AC'), ('Alarm', 'Alarm'), ('Bluetooth', 'Bluetooth'), ('Heated Seats', 'Heated Seats'), ('Wifi', 'Wifi'), ('Cruise Control', 'Cruise Control'), ('Front Parking Sensor', 'Front Parking Sensor'), ('Rear Parking Sensor', 'Rear Parking Sensor'), ('Roof Rack', 'Roof Rack'), ('Power Window', 'Power Window'), ('Sunroof', 'Sunroof'), ('USB Port', 'USB Port'), ('Sound System', 'Sound System'), ('Memory Seat', 'Memory Seat'), ('Other', 'Other')], default='Other', max_length=178)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.brand')),
                ('brand_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.brandmodel')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.color')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.condition')),
                ('drivetrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.drivetrain')),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.fueltype')),
                ('gear_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.geartype')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=96)),
                ('location', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='./img/')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.vehicle')),
            ],
        ),
    ]
