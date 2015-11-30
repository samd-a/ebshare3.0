from django.db import models

# Create your models here.

class book(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=60)
    cover = models.CharField(max_length=20)
    alt_text = models.CharField(max_length=20)
    
    #description = models.CharField(max_length=500)
    #details = models.CharField(max_length=200)
    
    #ideally, these would 1 non-array field with the paragraph text
    #current error: "need more than 1 value to unpack"
    description = ArrayField(models.CharField(max_length=500))
    details = ArrayField(models.CharField(max_length=200))

    def __unicode__(self):
+		return self.book.book_title
