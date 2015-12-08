from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.db.models import Q
from books.models import book

# Create your views here.
def renderviewbook(request, book_id):


        c = RequestContext(request);
        b = book.objects.get(pk=book_id)
        #get books with same genre or author
        #remove this one from list
        related = book.objects.filter(Q(book_author__contains=b.book_author) | Q(genre__contains=b.genre)).exclude(pk=book_id)
	
        #combine book details and related books into Context
        c['book_title'] = b.book_title
        c['book_author'] = b.book_author
        c['book_cover'] = b.book_cover
        c['alt_text'] = b.alt_text
        c['description'] = b.description
        c['details'] = b.details
        c['related'] = related
        c['id'] = book_id

	return render_to_response("viewbook/viewbook.html", c)

def renderreader(request, book_id):
        c = RequestContext(request);
        b = book.objects.get(pk=book_id)
        #get books with same genre or author
        #remove this one from list
        related = book.objects.filter(Q(book_author__contains=b.book_author) | Q(genre__contains=b.genre)).exclude(pk=book_id)
	
        #combine book details and related books into Context
        c['book_title'] = b.book_title
        c['book_author'] = b.book_author
        c['book_cover'] = b.book_cover
        c['alt_text'] = b.alt_text
        c['description'] = b.description
        c['details'] = b.details
        c['related'] = related
        return render_to_response("viewbook/reader.html", c)
