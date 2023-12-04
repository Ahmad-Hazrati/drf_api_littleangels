from rest_framework import generics, permissions
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Booking
from .serializers import BookingSerializer


class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Booking.objects.all()


class BookingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
