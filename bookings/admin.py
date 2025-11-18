from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'total_rent', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('user__email', 'car__name')
