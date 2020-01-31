#  Name: Tommy Cao
#  Date: 10/22/17
#  Description: Django Todo with PostgreSQL.

from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField()