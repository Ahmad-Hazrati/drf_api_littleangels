from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    """
    Represents a category for events.
    """
    title = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the category.

        Returns:
        - str: The title of the category.
        """
        return self.title


class Event(models.Model):
    """
    Represents an event.
    """
    class EventObjects(models.Manager):
        """
        Custom manager for Event model to retrieve only published events.
        """
        def get_queryset(self):
            """
            Overrides the default queryset to filter only published events.

            Returns:
            - QuerySet: The queryset containing only published events.
            """
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_image = models.ImageField(
        upload_to='images/',
        default='../default_post_zmlkyd', blank=True)
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal')
    alt_tag = models.TextField(max_length=100)
    venue = models.CharField(max_length=250)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=options, default='published')
    # Field for the guest to bring the required items with them in the event
    eventobjects = models.TextField()
    available_seats = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        - ordering : List events based on the publication date.
        """
        ordering = ['-published']

    def __str__(self):
        """
        Returns a string representation of the event.

        Returns:
        - str: The title of the event.
        """
        return self.title
