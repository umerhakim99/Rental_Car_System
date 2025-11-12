from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'total_rent')
    search_fields = ('user__email', 'car__name')

admin.site.register(Booking, BookingAdmin)
