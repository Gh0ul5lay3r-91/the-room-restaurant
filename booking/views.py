from django.shortcuts import render
from django.views import generic, View
from .models import Restaurant, Booking, Table
from .forms import BookingForm, RestaurantForm

# Create your views here.
class BookingView(View):

    def get(self, request):
        form = BookingForm()

        context = {'form': form}

        return render(request, 'booking/booking_form.html', context)

  
    def post(self, request):
        booking = Booking.objects.get()
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():

            form.save()

        context = {'form': form}

        return render(request, 'booking/booking_form.html', context)


class RestaurantView(View):

    def get(self, request):
        form = RestaurantForm()

        context = {'form': form}

        return render(request, 'booking/restaurant_form.html', context)

    
    def post(self, request):
        restaurant = Restaurant.objects.get()
        form = RestaurantForm(request.POST, instance=restaurant)

        if form.is_valid():

            form.save()

        context = {'form': form}

        return render(request, 'booking/restaurant_form.html', context)