from __future__ import unicode_literals

from django.db import models
class MessageManager(models.Manager):
    def sendMessager(self, content, sent_by, received_by):
        if len(content) > 0:
            message = Message.objects.create(
                content = content,
                sent_by_id = sent_by,
                received_by_id=received_by
            )
            return message
        else:
            return "messa not"

class User (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    content = models.TextField(max_length=1000)
    sent_by = models.ForeignKey(User, related_name="sent_messages")
    received_by = models.ForeignKey(User, related_name="received_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    object = MessageManager()

