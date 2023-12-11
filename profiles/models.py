from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    Represents a user profile associated with a Django User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    interests = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_mlzeil', blank=True
    )

    class Meta:
        """
        Meta class for defining additional model-level properties.

        Attributes:
        - ordering: Specifies the default ordering for queries.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the Profile instance.
        """
        return f"{self.user}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler function to create a user profile
    when a new User is created.

    Args:
    - sender: The sender of the signal (User model).
    - instance: The User instance being created.
    - created: True if a new User instance is created, False otherwise.
    - kwargs: Additional keyword arguments.

    Returns:
    - None
    """
    if created:
        Profile.objects.create(user=instance)


# Connect the create_profile signal to the post_save signal of the User model
post_save.connect(create_profile, sender=User)
