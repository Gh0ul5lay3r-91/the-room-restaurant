# Generated by Django 3.2 on 2022-01-25 12:18

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_time', models.TimeField(default=datetime.time(11, 0))),
                ('closing_time', models.TimeField(default=datetime.time(10, 0))),
                ('menu', cloudinary.models.CloudinaryField(default='placeholder', help_text='image of restaurants menu', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(choices=[(2, 'Table of 2'), (3, 'Table of 3'), (4, 'Table of 4'), (5, 'Table of 5'), (6, 'Table of 6')])),
                ('restaurant_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to='booking.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=6, unique=True)),
                ('party_size', models.IntegerField(choices=[(1, '1 person'), (2, '2 persons'), (3, '3 persons'), (4, '4 persons'), (5, '5 persons'), (6, '6 persons')], default=2)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('start_time', models.TimeField(default=datetime.time(12, 0))),
                ('end_time', models.TimeField()),
                ('phone_number', models.IntegerField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('date', models.DateField(default=datetime.date.today)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to=settings.AUTH_USER_MODEL)),
                ('table_number', models.ManyToManyField(related_name='number', to='booking.Table')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]