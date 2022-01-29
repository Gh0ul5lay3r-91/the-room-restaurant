from django.shortcuts import render
from django.views import generic, View
from .models import Restaurant, Booking, Table

# Create your views here.
class create_booking(View):


    def get_booking(request):


        return render(request, 'booking.booking_form.html', context)