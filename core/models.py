from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	wave = models.CharField(max_length=100)
