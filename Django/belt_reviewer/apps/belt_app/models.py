from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def register(self, first, last, username, email, dob, password, confirm):
        response = {
            "valid": True,
            "errors": [],
            "user": None
        }
        if len(first) < 1:
            response["errors"].append("First name is required")
        elif len(first) < 2:
            response["errors"].append("First name must be longer")

        if len(last) < 1:
            response["errors"].append("Last name is required")
        elif len(last) < 2:
            response["errors"].append("Last name must be longer")

        if len(first) < 1:
            response["errors"].append("Username is required")
        elif len(first) < 3:
            response["errors"].append("Username must be longer")

        if len(email) < 1:
            response["errors"].append("Email is required")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid Email")
        else:
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) > 0:
                response["errors"].append("Email is already in use")

        if len(dob) < 1:
            response["errors"].append("Date of Birth is required")
        else:
            date = datetime.strptime(dob, '%Y-%m-%d')
            today = datetime.now()
            if date > today:
                response["errors"].append("Date of Birth must be in the past")

        if len(password) < 1:
            response["errors"].append("Password is required")
        elif len(password) < 8:
            response["errors"].append(
                "Password must be 8 characters or longer")

        if len(confirm) < 1:
            response["errors"].append("Confirm Password is required")
        elif confirm != password:
            response["errors"].append("Confirm Password must match Password")

        if len(response["errors"]) > 0:
            response["valid"] = False
        else:
            response["user"] = User.objects.create(
                first_name=first,
                last_name=last,
                username=username,
                email=email.lower(),
                dob=date,
                password=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            )
        return response

    def login(self, email, password):
		response = {
			"valid": True,
			"errors": [],
			"user": None
		}

		if len(email) < 1:
			response["errors"].append("Email is required")
		elif not EMAIL_REGEX.match(email):
			response["errors"].append("Invalid Email")
		else:
			email_list = User.objects.filter(email=email.lower())
			if len(email_list) == 0:
				response["errors"].append("Unknown email")

		if len(password) < 1:
			response["errors"].append("Password is required")
		elif len(password) < 8:
			response["errors"].append("Password must be 8 characters or longer")

		if len(response["errors"]) == 0:
			hashed_pw = email_list[0].password
			if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
				response["user"] = email_list[0]
			else:
				response["errors"].append("Incorrect Password")

		if len(response["errors"]) > 0:
			response["valid"] = False

		return response
class BookManager(models.Manager):
    def book(self, name, desc,user_id):
        response = {
            "valid": True,
            "errors": [],
            "book": None
        }
        if len(name) < 1:
            response["errors"].append("Name is required")
        elif len(name) < 2:
            response["errors"].append("Name must be longer")
        
        if len(desc) < 1:
            response["errors"].append("Description is required")
        elif len(desc) < 5:
            response["errors"].append("Description must be longer")
        
        if len(response["errors"]) > 0:
            response["valid"] = False
        else:
            response["book"] = Book.objects.create(
                name=name,
                desc=desc,
                user_id=user_id,
            )
        return response

class ReviewManager(models.Manager):
    def review(self, content, rating,user_id,book_id):
        response = {
            "valid": True,
            "errors": [],
            "book": None
        }
        if len(content) < 1:
            response["errors"].append("Name is required")
        elif len(content) < 2:
            response["errors"].append("Name must be longer")
        
        if len(response["errors"]) > 0:
            response["valid"] = False
        else:
            response["book"] = Review.objects.create(
                review=content,
                rating=rating,
                user_id=user_id,
                book_id=book_id,
            )
        return response



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="books")
    objects = BookManager()

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name="review_books")
    book = models.ForeignKey(Book,related_name="users")
    objects = ReviewManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, related_name="authors")


