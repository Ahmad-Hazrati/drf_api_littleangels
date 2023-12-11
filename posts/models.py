from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a post in a Django model.
    """

    image_filter_choices = [
        ('1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="admin")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_zmlkyd', blank=True)
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices, default='normal')

    class Meta:
        """
        Meta class for defining additional model-level properties.

        Attributes:
        - ordering: Specifies the default ordering for queries.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the Post instance.
        """
        return f"{self.id}{self.title}"
