from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Booking
from .serializers import BookingSerializer


class BookingList(generics.ListCreateAPIView):
    """
    API view for listing and creating Booking instances.

    This view allows users to:
    - Retrieve a list of all bookings.
    - Create a new booking instance.
    """
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
        """
        Method to associate the comment with the current request user upon creation.
        """
        serializer.save(user=self.request.user)


class BookingDetail(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a specific Booking instance.

    This view allows users to:
    - Retrieve details of a specific booking.
    - Delete a specific booking instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
