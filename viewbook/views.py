from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.db.models import Q
from django.db.models import F
from books.models import book
from viewbook.models import reader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def renderviewbook(request, book_id):


        c = RequestContext(request);
        b = book.objects.get(pk=book_id)
        r = reader.objects.filter(Q(book=b) & Q(user=request.user.id))
        #get books with same genre or author
        #remove this one from list
        related = book.objects.filter(Q(book_author__contains=b.book_author) | Q(genre__contains=b.genre)).exclude(pk=book_id)
	
        
        if r.count() > 0:
            c['time_left'] = r[0].time_left
        else:
            c['time_left'] = 0

        #combine book details and related books into Context
        c['book_title'] = b.book_title
        c['book_author'] = b.book_author
        c['book_cover'] = b.book_cover
        c['book_points'] = b.book_points
        c['alt_text'] = b.alt_text
        c['description'] = b.description
        c['details'] = b.details
        c['related'] = related
        c['id'] = book_id

	return render_to_response("viewbook/viewbook.html", c)

def renderreader(request, book_id):
        c = RequestContext(request);
        b = book.objects.get(pk=book_id)
        r = reader.objects.filter(Q(book=b) & Q(user=request.user.id))
        #b = book.objects.get(pk=book_id)
        #get books with same genre or author
        #remove this one from list
	
        #combine book details and related books into Context
        if r.count() > 0:
            c['time_left'] = r[0].time_left
        else:
            c['time_left'] = 0
        c['book_text'] = b.description

        
        c['id'] = book_id
        return render_to_response("viewbook/reader.html", c)

def purchasebook(request, book_id, price, seconds):
        b = book.objects.get(pk=book_id)
        readerEntry, created = reader.objects.get_or_create(user=request.user.id, book=b)
        if not created:
            readerEntry.time_left = F('time_left') + seconds
            readerEntry.save()
        
        return renderreader(request, book_id)

@csrf_exempt
def updatetime(request, book_id, seconds):
        b = book.objects.get(pk=book_id)
        readerEntry, created = reader.objects.get_or_create(user=request.user.id, book=b)
        if not created:
            readerEntry.time_left = seconds
            readerEntry.save()
        
        return HTTPResponse();

