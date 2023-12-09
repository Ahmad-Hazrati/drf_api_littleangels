from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Category.objects.all()


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        booking_count=Count('bookings', distinct=True),
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        booking_count=Count('bookings', distinct=True),
    ).order_by('-created_at')
