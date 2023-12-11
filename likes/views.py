from rest_framework import generics, permissions
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    API view for listing and creating Like instances.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        Custom method to set the user field when creating a new Like instance.

        Args:
        - serializer: The LikeSerializer instance used for creating the Like.

        Returns:
        - None
        """
        serializer.save(user=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a specific Like instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
