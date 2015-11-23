from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def renderSignup(request):
	return render_to_response("userAuth/signup.html")

def renderSignin(request):
	return render_to_response("userAuth/signin.html")


# From METSCAV

# # Create your views here.
# def login_user(request):
#     """
#     :param: HttpRequest
#     :rtype: HttpResponse
    
#     log a user into the website. This function takes the login information
#     such as the username and password from the user and pass the information
#     to **LogInForm**. The **LogInForm** has class method called **login_process()**
#     and this class method handles processing the login information.
#     """
#     title = "Log in"
#     args = {}
#     user = None

#     if request.method == "POST":
#         # The method should be post since it does not expose the user imformation on url.
#         # it should be get method since login does not change state of any user data.
#         form = LogInForm(request.POST)
#         # check the form validation.
#         if form.is_valid():

#             user = form.login_process(request)
#             if user is not None:
#                 args = {'user':user}
#                 args.update(csrf(request))
#                 return render_to_response('home/home.html', args)
#             else:
#                 args = {'title':'Username does not exist.'}
#                 args.update(csrf(request))
#                 return render_to_response('user_auth/login.html', args)
#     else:
#         form = LogInForm()


#     args = {'form':form, 'title':title}
#     args.update(csrf(request))
#     return render_to_response('user_auth/login.html', args)

# @login_required
# def logout_user(request):
#     """
#     :param: HttpRequest
#     :rtype: HttpResponse
#     This function handles log the user out from the website. 
#     """

#     logout(request)
#     return render_to_response('home/home.html', {})

# def register(request):
#     """
#     :param: HttpRequest
#     :rtype: HttpResponse
#     This method handles registering new users. All neccessary information is
#     taken from **register.html** page, and those information is passed into
#     **RegisterForm** and the class method **register_form()** will process 
#     the information.
#     """
#     user = None
#     # handles registering.
#     title = 'Register'
#     args = {}
#     if request.method == 'POST':
#         # it means that we received inputs from the user.
#         # Then, fill them out.
#         form = RegisterForm(request.POST)
#         # check if all inputs are valid.
#         if form.is_valid():
#             if_error = form.register_form()
#             if not if_error:
#                 args = {'title':'Username Exists', 'valid':False}
#                 return render_to_response('user_auth/register.html', args)
#             return HttpResponseRedirect('/')
#         else:
#             # form is not valid.
#             args = {'title':'Data is not valid', 'valid':False}
#             return render_to_response('user_auth/register.html', args)
#     else:
#         form = RegisterForm()

#     args = {'form' : form,
#             'title' : title,
#             'valid':True}
#     args.update(csrf(request)) # Guess passing csrf token to the template.
#     return render_to_response('user_auth/register.html', args)