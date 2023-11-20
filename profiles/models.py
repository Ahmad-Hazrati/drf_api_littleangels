from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    interest = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to = 'images/', default='../default_profile_mlzeil', blank=True
    )

    class Meta:
        ordering = ['-created_at']


def __str__(self):
    return f"{self.user}'s profile"