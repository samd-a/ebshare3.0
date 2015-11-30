from django.shortcuts import render
from django.shortcuts import render_to_response
from userAuth.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def renderSignup(request):
	return render_to_response("userAuth/signup.html")

def renderSignin(request):
	return render_to_response("userAuth/signin.html")

def register(request):
	context = RequestContext(request)

	# Boolean value for telling the template whether the registration was successful
	# Initially set to False. Changes to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provide a profile picture?
			# If so, we need to get it from the imput form and put it in the userProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

				# Now we save the userProfile model instance
				profile.save()

				# update our variable to tell the template registration was successful.
				registered = True

			# Invalid form or forms - mistakes or something
			# Print problems to the terminal and show them to user.
			else:
				print user_form.errors, profile_form.errors
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank waiting for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render_to_response('userAuth/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
		context)

def user_login(request):
	# We obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the Login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a user object, the details are correct.
		# If None, no user with matching credentials was found.
		if user:
			# If the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in (using Django machinery).
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				# An inactive account was used - no logging in
				return HttpResponse("Your account is disabled.")
		else:
			# Bad login details were provided. Don't log the user in.
			# TODO: create an html page to redirect to with a login fail message
			print "Invalid Login details"
			return HttpResponse("Invalid login details was used")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET
	else:
		# No context variables to pass to the template system, hence the 
		# blank dictionary object
		return render_to_response('userAuth/login.html', {}, context)