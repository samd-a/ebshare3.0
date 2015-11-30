from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def renderHome(request):
	context = RequestContext(request)
	# No context variables to pass to the template system, hence the 
	# blank dictionary object
	return render_to_response('homePage/home.html', {}, context)
