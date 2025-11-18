from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    total_rent = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'car', 'start_date', 'end_date', 'total_rent', 'status']

    def get_total_rent(self, obj):
        months = max(1, (obj.end_date.year - obj.start_date.year) * 12 + (obj.end_date.month - obj.start_date.month))
        return f"SAR {obj.car.rent_per_month * months}"

    def validate(self, data):
        car = data['car']
        start = data['start_date']
        end = data['end_date']

        # Prevent overlapping bookings
        if Booking.objects.filter(car=car, start_date__lte=end, end_date__gte=start).exists():
            raise serializers.ValidationError("This car is already booked for these dates.")
        return data
