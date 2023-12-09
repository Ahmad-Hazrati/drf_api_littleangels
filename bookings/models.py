from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(
        auto_now=True)
    event = models.ForeignKey(
        Event, related_name='bookings', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.event.available_seats:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Sorry booking was closed already")
