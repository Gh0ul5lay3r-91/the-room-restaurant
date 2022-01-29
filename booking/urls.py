from . import views
from django.urls import path

urlpatterns = [
    path('create_booking/', views.create_booking.as_view(), name='create_booking')
]