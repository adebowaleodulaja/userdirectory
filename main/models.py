from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, verbose_name = "Name:")
    email_address = models.EmailField(max_length=254, verbose_name= "Email Address:")
    date_added = models.DateTimeField(default=timezone.now)