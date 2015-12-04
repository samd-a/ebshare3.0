from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class book(models.Model):
    # Book Attributes
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=60)
    cover = models.CharField(max_length=20)
    alt_text = models.CharField(max_length=20)
    description = models.CharField(max_length=750)
    details = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    # User who uploaded it
    #user = models.ForeignKey(User, default=001)

    
    #ideally, these would 1 non-array field with the paragraph text
    #current error: "need more than 1 value to unpack"
    #description = ArrayField(models.CharField(max_length=500))
    #details = ArrayField(models.CharField(max_length=200))

    def __unicode__(self):
		return self.book.book_title

#class txtbook(book):
#    fixtures = ['books.json']
