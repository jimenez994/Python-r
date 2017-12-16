from __future__ import unicode_literals

from django.db import models
class  CourseManager(models.Manager):
    def register(self,course_name,course_decs):
        response = {
            "valid": True,
            "errors":[],
            "course": None
        }
        if len(course_name) < 1:
            response["errors"].append("Name is required")
        elif len(course_name) < 5:
            response["errors"].append("Name must be 5 characters or longer")
        if len(course_decs) < 1:
            response["errors"].append("Name is required")
        elif len(course_decs) < 15:
            response["errors"].append("Name must be 5 characters or longer")
        if len(response["errors"]) > 0:
            response["valid"] = False
        else:
            response["course"] = Course.objects.create(
                name = course_name,
                description = course_decs
            )
        return response
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
