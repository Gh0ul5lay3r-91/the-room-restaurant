from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('customer', 'party_size', 'start_time', 'phone_number', 'email', 'date')
        