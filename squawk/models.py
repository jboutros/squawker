from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Squawk(models.Model):
    text = models.CharField(max_length=141)
    user = models.ForeignKey(User)