from django.db import models
from django.contrib.auth.models import User  # built-in Django user model

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User,                             # links each Task to a User
        on_delete = models.CASCADE,      # if the user is deleted, delete their tasks too
        null = True,                      # allows the field to be empty in the database
        blank = True                      # allows leaving it empty in forms
        )  
    title = models.CharField(max_length = 200)                 # title of the task
    description = models.TextField(null = True, blank = True)  # detailed description
    complete = models.BooleanField(default = False)            # whether the task is done
    created = models.DateTimeField(auto_now_add = True)        # timestamp when task is created


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']  # incomplete tasks appear before completed ones