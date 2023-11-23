from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from events.models import Event



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='event_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'post', 'event']

    def __str__(self):
        return f"{self.user}{self.post}{self.event}"
