# serializers.py

from rest_framework import serializers
from .models import Booking


class BookingWithDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        if instance.status == 'Done':
            return BookingWithDurationSerializer(instance, context=self.context).data
        return super().to_representation(instance)

