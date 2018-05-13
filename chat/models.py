from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ChatMessage(models.Model):
    """
    Model to represent a chat message
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String to represent the message
        """
        return self.message
