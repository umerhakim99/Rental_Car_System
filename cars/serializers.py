from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    rent_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'rent_per_month', 'rent_formatted', 'image']

    def get_rent_formatted(self, obj):
        return f"SAR {obj.rent_per_month}"
