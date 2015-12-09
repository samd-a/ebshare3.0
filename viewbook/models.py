from django.db import models
from django.contrib.auth.models import User
from books.models import book
import os

class reader(models.Model):
    user = models.ForeignKey(User, db_column='user')
    book = models.ForeignKey(book)
    time_read = models.IntegerField(default=0)
    time_left = models.IntegerField(default=0)
    def __unicode__(self):
		return self.time_read
