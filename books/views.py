from django.shortcuts import render
from django.shortcuts import render_to_response

from books.models import book

# Create your views here.

def index(request):
    bookList = book.objects.all()
    context = {'bookList': bookList}
    return render(request, "books/bookshelf.html", context)


#class bookList(ListView):
#    model = book

#    def get_context_data(self):
#        context = super(bookList, self).get_context_data("*")
#        return context
def renderbookshelf(request):	
    return index(request)
#	return render_to_response("books/bookshelf.html")
