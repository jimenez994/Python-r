from __future__ import unicode_literals
from django.db import models
class UserManager(models.Manager):
	def register(self,first,last,username,email,dob,password):
		response = {
			"valid":True,
			"errors":[],
			"user": None
		}
		if len(first) < 1:
			response["errors"].append("First name is required")
		if len(last) < 1:
			response["errors"].append("Last name is required")
		if len(Username) < 1:
			response["errors"].append("Username name is required")
		if len(email) < 1:
			response["errors"].append("Email is required")
		if len(dob) < 1:
			response["errors"].append("Birth date is required")
		if len(password) < 1:
			response["errors"].append("Password is required")
		if len(confirm) < 1:
			response["errors"].append("Confirm Password is required")


		pass
	def login(self,email,password):
		pass

class MessageManager(models.Manager):
	def sendMessage(self, content, sent_by, received_by):
		if len(content) > 0:
			message = Message.objects.create(
				content=content,
				sent_by_id=sent_by,
				received_by_id=received_by
			)
			return message
		else:
			return "Message cannot be blank!"

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Message(models.Model):
	content = models.TextField(max_length=1000)
	sent_by = models.ForeignKey(User, related_name="sent_messages")
	received_by = models.ForeignKey(User, related_name="received_messages")
	created_at = models.DateTimeField(auto_now_add=True)
	objects = MessageManager()
