from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
#...
from books.models import book

# Create your views here.
def renderviewbook(request, book_id):
        c = Context();
        b = book.objects.get(pk=book_id)
        #needs to be pulled from db.
        #c['book_title'] = "Object-Oriented and Classical Software Engineering"
        #c['book_author'] = "Stephen R. Schach"
        #c['cover'] = "OOCnE.jpg"
        #c['alt_text'] = "OOCnE"
        #c['description'] = "				Object-Oriented Software Engineering is written for both the traditional one-semester and the newer two-semester software engineering curriculum. \
	#			Part I covers the underlying software engineering theory, \
	#			while Part II presents the more practical life cycle, workflow by workflow. \
	#			The text is intended for the substantial object-oriented segment of the software engineering market. \
	#			It focuses exclusively on object-oriented approaches to the development of large software systems that are the most widely used. \
	#			Text includes 2 running case studies, expanded coverage of agile processes and open-source development.."
        #c['details'] = "<ul> \
        #            <li>Lorem Ipsum</li> \
        #            <li>Dolor Sit Amet</li> \
        #            <li>Consectetur</li> \
        #            <li>Adipiscing Elit</li> \
        #        </ul>"
	
        c['book_title'] = b.book_title
        c['book_author'] = b.book_author
        c['cover'] = b.cover
        c['alt_text'] = b.alt_text
        c['description'] = b.description
        c['details'] = b.details
	return render_to_response("viewbook/viewbook.html", c)

