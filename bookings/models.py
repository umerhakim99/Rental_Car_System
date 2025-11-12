from django.db import models
from django.conf import settings
from cars.models import Car

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_rent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate total rent
        months = max(1, ((self.end_date.year - self.start_date.year) * 12 + self.end_date.month - self.start_date.month))
        self.total_rent = months * self.car.rent_per_month
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} booking {self.car.name}"
