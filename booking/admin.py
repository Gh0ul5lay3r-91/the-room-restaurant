from django.contrib import admin
from .models import Booking, Table, Restaurant

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date', 'party_size')
    search_fields = ['name']
    ordering = ('-date', '-start_time')
    actions = ['delete_selected']
    filter_horizontal = (
        "table",
    )

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass
