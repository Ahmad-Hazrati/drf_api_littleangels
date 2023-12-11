from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    API view for listing Profile instances.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('user__post', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'user__following__followed__profile',
        'user__followed__user__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'user__following__created_at',
        'user__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a specific Profile instance.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('user__post', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
