from rest_framework import serializers
from datetime import date

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        car = data['car']
        start = data['start_date']
        end = data['end_date']

        # Check overlapping bookings
        if Booking.objects.filter(car=car, start_date__lte=end, end_date__gte=start).exists():
            raise serializers.ValidationError("This car is already booked for these dates.")
        return data
