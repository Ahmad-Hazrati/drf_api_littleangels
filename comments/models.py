from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description
