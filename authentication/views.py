from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	return render(request, 'authentication/index.html')


def signup(request):
	# Check if request is from a Form
	if request.method == 'POST':
		# Get Form Data
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		# Check if password and Confirm Password match
		if password1 == password2:
			# Create user by adding username(email), email and password Parameters
			user = User.objects.create_user(email, email, password1)
			# Check if user has been created
			if user.is_active:
				# Add first name and last name to User object.  
				user.first_name = first_name
				user.last_name = last_name
				user.save()
				# Redirect user to login page
				return HttpResponseRedirect('../login')
			else:
				# If user is not created return an error
				return HttpResponse("Error Creating User: " + first_name +".")
		else:
			# If Password don't Match return a Password Don't Match error
			return HttpResponse("Password and Confirm Password DO NOT Match.") 
	else:
		# If user request is not a form return a form view.
		return render(request, 'authentication/register.html')


def login_user(request):
	# Check if the user request is a form
	if request.method == 'POST':
		# Get form data 
		email = request.POST['email']
		password = request.POST['password']
		# Check if the username and password are correct
		user = authenticate(username=email, password=password)
		# Login the user if username and password is correct.
		if user is not None:
			login(request, user)
			# Redirect the user to the link require login
			try:
				return HttpResponseRedirect(''+request.POST['next'])
			except Exception:
				# Redirect user to home page if no previous link.
				return HttpResponseRedirect("../")
		else:
			# If Username and Password are wrong, send an error report 
			return HttpResponse("Invalid username or password")
	else:
		# If user request is not a form return a form view.
		return render(request, 'authentication/login.html')


@login_required(login_url='/login/')
def logout_user(request):
	# Logout user if login
	logout(request)
	# Redirect user to login page
	return HttpResponseRedirect('../login')


@login_required(login_url='/login/')
def new_password(request):
	# Check if user request is from a form 
	if request.method == 'POST':
		# Get form data
		old_password = request.POST['old_password']
		new_password = request.POST['new_password']
		confirm_password = request.POST['confirm_password']
		# Get User
		user = request.user
		# Check if old password is correct
		if user.check_password(old_password):
			# Check if new Password and Confirm password are matching
			if new_password == confirm_password:
				# Check if old password and new password do not match 
				if not new_password == old_password:
					# Set new password
					user.set_password(new_password)
					user.save()
					# Logout user
					logout(request)
					# Redirect user to the login page
					return HttpResponseRedirect('../login/')
				else:
					# Inform user new password and old password are the same
					return HttpResponse("The password has not changed!! Please enter a new password.")
			else:
				# Inform user that new password and confirm password do not match.
				return HttpResponse("The new password and confirm password do not match.")
		else:
			# Inform the user of incorrect password.
			return HttpResponse("Incorrect password. Enter the correct password to change.")
	else:	
		# Return change password view, if request is not from form.	
		return render(request, 'authentication/change-password.html')


def reset_password(request):
	# Check if user request is from a form 
	if request.method == 'POST':
		# get form data
		email = request.POST['email']
		
	else:
		# Return forgot-password view, if request is not from form.	
		return render(request, 'authentication/forgot-password.html')


def reset_password_done(request):
	return render(request, 'authentication/reset-password-done.html')