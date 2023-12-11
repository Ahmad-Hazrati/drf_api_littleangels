from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Represents a follower relationship between users in a Django model.
    """
    user = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
        )
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for defining additional model-level properties.

        Attributes:
        - ordering: Specifies the default ordering for queries.
        - unique_together: Ensures uniqueness of the combination of 'user' and 'followed'.
        """
        ordering = ['-created_at']
        unique_together = ['user', 'followed']

    def __str__(self):
        """
        Returns a string representation of the Follower instance.
        """
        return f"{self.user}{self.followed}"
