from django.db import models
from datetime import datetime, date, time, timedelta 
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Restaurant(models.Model):

    name = models.TextField(unique=True, null=True)
    opening_time = models.TimeField(default=time(11, 00))
    closing_time = models.TimeField(default=time(10, 00))
    menu = CloudinaryField('image', default='placeholder', use_filename=True, help_text='image of restaurants menu')

    def __str__(self):
        return self.name


class Table(models.Model):

    TABLE_SIZE = [
        (2, 'Table of 2'),
        (3, 'Table of 3'),
        (4, 'Table of 4'),
        (5, 'Table of 5'),
        (6, 'Table of 6'),
    ]

    number = models.IntegerField(default=0)
    size = models.IntegerField(choices=TABLE_SIZE)

    def __str__(self):
        return f"A table of {self.size} persons"


class Booking(models.Model):

    PARTY_SIZE = [
        (1, '1 person'),
        (2, '2 persons'),
        (3, '3 persons'),
        (4, '4 persons'),
        (5, '5 persons'),
        (6, '6 persons'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='customer')
    party_size = models.IntegerField(choices=PARTY_SIZE, default=2)
    created_on = models.DateTimeField(auto_now=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, default=time(12, 00))
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=250)
    date = models.DateField(default=date.today)
    updated_on = models.DateTimeField(auto_now=True)
    table = models.ManyToManyField(Table, related_name='tables')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_on']

    
    def created_end_time(self):
        end_time = (datetime.combine(date.today(), self.time)) + timedelta(hours=2)
        return end_time.time()
    

    def __str__(self):
        return f"A table of {self.party_size} on {datetime.strftime(self.date, '%d-%m-%y')}"