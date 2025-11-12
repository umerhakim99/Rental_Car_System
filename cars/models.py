from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    rent_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"{self.brand} {self.name}"
