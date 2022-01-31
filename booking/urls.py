from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingView.as_view(), name='booking_form'),
    path('restaurant', views.RestaurantView.as_view(), name='restaurant_form')
]