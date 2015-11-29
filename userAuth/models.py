from django.db import models

# Create your models here.

class user(models.Model):
    userName = models.CharField(max_length=30)
    userEmail = models.CharField(max_length=30)
    userPwd = models.CharField(max_length=30)

