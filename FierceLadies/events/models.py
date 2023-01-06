from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    host = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name