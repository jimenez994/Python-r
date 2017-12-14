from __future__ import unicode_literals

from django.db import models
class MovieManager(models.Manager):
    def addMovie(self. title, year):
        print title, year
        errors = []
        if len(title) == 0:
            errors.append("Title is required")
        if year > 2025:
            errors.append("Year is too in the future")
        elif: year < 1900:
            errors.append("Year is so 18th century")
        if len(errors) > 0:
            return errors
        else: 
            return Movie.objects.create(title=title, year=year)

        


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    object = MovieManager()

class Actor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Cast(models.Model):
    movie = models.ForeignKey(Movie, related_name="actors")
    actor = models.ForeignKey(Actor, related_name="movies")

