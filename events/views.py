from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    API endpoint that allows listing and creation of categories.
    """
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Category.objects.all()


class EventList(generics.ListCreateAPIView):
    """
    API endpoint that allows listing and creation of events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        booking_count=Count('bookings', distinct=True),
    ).order_by('-created_at')

    def perform_create(self, serializer):
        """
        Overrides the default behavior to set the user field
        during event creation.

        Parameters:
        - serializer (EventSerializer): The serializer instance
        used for event creation.
        """
        serializer.save(user=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows retrieving, updating, and deleting
    individual events.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        booking_count=Count('bookings', distinct=True),
    ).order_by('-created_at')
