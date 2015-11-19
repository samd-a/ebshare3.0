from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def renderviewbook(request, book_id):	
	return render_to_response("viewbook/viewbook.html")

