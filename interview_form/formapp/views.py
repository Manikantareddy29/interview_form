from django.shortcuts import render
from formapp.models import Booking
from formapp.seiralizers import BookingSerializer, BookingWithDurationSerializer
from rest_framework import viewsets
from rest_framework import viewsets
from .models import Booking

from .models import Booking

class interviewViewSet(viewsets.ModelViewSet):
    queryset =Booking.objects.all()
    serializer_class = BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BookingSerializer
        elif self.action == 'create' or self.action == 'update':
            if self.request.data.get('status') == 'Done':
                return BookingWithDurationSerializer
            return BookingSerializer
