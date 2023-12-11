from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Model representing a comment on a post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        """
        Meta class to define model-specific metadata.
        - ordering: List specifying the default ordering for comments based on the creation timestamp.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Method returning a string representation of the comment (used for display purposes).
        """
        return self.description
