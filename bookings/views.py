from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Booking
from .serializers import BookingSerializer


class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Booking.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'event'
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
