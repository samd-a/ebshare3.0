from django.db import models
from books.models import book
from django.contrib.auth.models import User
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.username), filename)

class userProfile(models.Model):
	# This line links userProfile to a Django User model instance.
	# The Django User model comes with five primary attributes:
	# Username, Password, First name, Last name
	user = models.OneToOneField(User)

	# The additional attribute we want to include.
	username = models.CharField(max_length=50, primary_key=True)	
	picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	points = models.IntegerField(default=0)
	# TODO:
	# bio = 

	# 
	# Override the __unicode__() method to return something meaningful
	def __unicode__(self):
		return self.user.username
		

class review(models.Model):
	
	reviewTitle = models.CharField(max_length=30)
	reviewContent = models.CharField(max_length=150)
	user = models.ForeignKey(User, db_column='user')
	book = models.ForeignKey(book)

	def __unicode__(self):
		return self.reviewTitle

def add_profile_pic(user, picture):
	userProf = userProfile()
	userProf.user = user
	#userProf.username = user.username
	userProf.picture = picture
	userProf.save()

def add_user_book(user, cover, title, author, description, genre):
#def add_user_book(title, author, description, genre):
	Book = book()
	Book.book_cover = cover
	Book.book_title = title
	Book.book_author = author
	Book.description = description
	Book.genre = genre
	Book.user = user
	Book.save()