from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Represents a like on a post in a Django model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for defining additional model-level properties.

        Attributes:
        - ordering: Specifies the default ordering for queries.
        - unique_together: Ensures uniqueness of the combination
        of 'user' and 'post'.
        """
        ordering = ['-created_at']
        unique_together = ['user', 'post']

    def __str__(self):
        """
        Returns a string representation of the Like instance.
        """
        return f"{self.user}{self.post}"
