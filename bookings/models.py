from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE)
    # number_of_people = models.IntegerField()
    # add_to_guest = models.IntegerField(null=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        # Check available seats logic here
        if self.event.available_seats:
        #     total_registered = self.event.registered_seats.count()
        #     requested_guests = int(self.number_of_people)
        #     if self.add_to_guest:
        #         total_registered += requested_guests
        #     else:
        #         total_registered = requested_guests
        #     available_seats = int(self.event.max_guests) - total_registered
        #     if available_seats >= 0:
        #         super().save(*args, **kwargs)
        #     else:
        #         raise ValueError("Not enough available seats for this event")
        # else:
        #     # If no maximum guest limit is set, allow booking
            super().save(*args, **kwargs)
        else:
            raise ValueError("Sorry booking was closed already")
