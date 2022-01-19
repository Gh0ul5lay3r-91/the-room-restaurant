from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):

    TABLE_SIZE = [
        (2, 'Table of 2'),
        (3, 'Table of 3'),
        (4, 'Table of 4'),
        (5, 'Table of 5'),
        (6, 'Table of 6'),
    ]

    table_number = models.IntergerField(max_length=20)
    size = models.IntergerField(choices=TABLE_SIZE)
    resturant_name = models.CharField(max_length=50)

    def __str__(self):
        return


class Booking(models.Model):

    PARTY_SIZE = [
        (1, '1 person'),
        (2, '2 persons'),
        (3, '3 persons'),
        (4, '4 persons'),
        (5, '5 persons'),
        (6, '6 persons').
    ]

    booking_id = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=20, uniques=False)
    party_size = models.IntergerField(choices=PARTY_SIZE, default=2)
    created_on = models.DateTimeField(auto_now=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, default=time(12, 00))
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    phone_number = models.IntergerField(max_length=15, unique=True)
    email = models.EmailField(max_length=250)
    date = models.DateField(default=date.today)
    updated_on = models.DateTimeField(auto_now=True)
    table_number = models.ManyToManyField()

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return