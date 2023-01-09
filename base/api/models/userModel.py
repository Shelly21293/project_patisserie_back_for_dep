from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # avatar = models.CharField(max_length=50)
    # commerad = models.BooleanField(default=False)
    credit = models.CharField(max_length=4)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address