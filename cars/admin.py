from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'rent_per_month', 'available')
    search_fields = ('name', 'brand')

admin.site.register(Car, CarAdmin)
