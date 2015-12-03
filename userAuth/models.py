from django.db import models
from books.models import book
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
	# This line links userProfile to a Django User model instance.
	# The Django User model comes with five primary attributes:
	# Username, Password, First name, Last name
	user = models.OneToOneField(User)

	# The additional attribute we want to include.
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	# TODO:
	# bio =
	# 
	# Override the __unicode__() method to return something meaningful
	def __unicode__(self):
		return self.user.username
		

class review(models.Model):
	
	reviewTitle = models.CharField(max_length=30)
	reviewContent = models.CharField(max_length=150)
	user = models.ForeignKey(User)
	book = models.ForeignKey(book)

	def __unicode__(self):
		return self.reviewTitle