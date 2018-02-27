from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_to = models.ForeignKey(Post, on_delete=models.CASCADE)


