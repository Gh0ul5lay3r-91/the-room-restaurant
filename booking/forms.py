from django import forms
from django.forms import ModelForm
from .models import Booking, Restaurant

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('customer', 'party_size', 'start_time', 'phone_number', 'email', 'date')


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'opening_time', 'closing_time', 'menu')