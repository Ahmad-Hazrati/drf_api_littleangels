from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_littleangels.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    API view for listing and creating Comment instances.
    This view allows users to:
    - Retrieve a list of comments.
    - Create a new comment instance.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post'
    ]

    def perform_create(self, serializer):
        """
        Method to associate the comment with the current request user upon creation.
        """
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Comment instance.
    This view allows users to:
    - Retrieve details of a specific comment.
    - Update the content of a specific comment.
    - Delete a specific comment instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
