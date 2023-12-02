from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Event(models.Model):

    class EventObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200, blank=True)
    description = models.TextField()
    event_image = CloudinaryField("image", default="placeholder")
    alt_tag = models.TextField(max_length=100)
    venue = models.CharField(max_length=250)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices = options, default='published')
    eventobjects = models.TextField() # Field for the guest to bring the required items with them in the event
    max_seats = models.IntegerField()
    registered_seats = models.IntegerField()
    available_seats = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    def check_availablte_seats(self, *args, **kwargs):
        """Check the number of guests registered,
        and set the already_registered"""
        return self.max_seats == registered_seats
