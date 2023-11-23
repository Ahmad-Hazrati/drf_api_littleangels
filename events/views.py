from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Category.objects.all()


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.eventobjects.annotate(
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]


class EventCreate(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]
