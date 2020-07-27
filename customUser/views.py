from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Messages


## TRYING WHATSAPP MESSAGE
# import os
# from twilio.rest import Client
# auth_token = '33a3dfa60c52cc7e52f0877421c59343'
# account_sid = 'ACe5c1b1ebc45b9158edbe05e5f173bbfe'
# client = Client(account_sid,auth_token)


## JUST TRYING 
"""from geopy.distance import geodesic
from geopy.geocoders import Nominatim
locator = Nominatim(user_agent = "myGeocoder")
"""
##


## FAST 2 SMS API USE 
# import requests, json

# def send_sms(number, message):
# 	url = 'https://www.fast2sms.com/dev/bulk'
# 	params = {
# 		'authorization' : '9inWm8qQp6Os12DgwxrR4yZkhajoVNYbtF50BLMdcATKGEfeXPotOgyPHXnA7vE2frUMscT13iNe8IRh',
# 		'sender_id' : 'FSTSMS',
# 		'message' : message,
# 		'numbers' : number,
# 		'route' : 'p'
# 	}
# 	requests.get(url, params = params)




## SIGN UP VIEW FOR THE SIGN UP PAGE.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm # CUSTOM FORM CREATED FOR THE EXTRA FIELDS.
    success_url = reverse_lazy('login') # reverse_lazy finds the url for the 'login' page. ["login" is a keyword that is automatically recognised by django.]
    template_name = 'signup.html'


@login_required(login_url="/users/login") # ITS JUST LIKE AN IF STATEMENT, i.e. only users which are logged in can use this function , no one else/
def edit_profile(request):
	if request.method == "POST":
		form = CustomUserChangeForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return HttpResponse('something is not right! (look again at the code)')
	elif request.method == "GET":
		form = CustomUserChangeForm(instance = request.user)
		context = {'form' : form }
		return render(request, 'edit_form.html', context)

#@login_required(login_url="/users/login")
def pass_change(request):
	#return HttpResponse("<h2> <kbd> password change page - under constuction.</kbd></h2> <br>")
	return render(request, 'password_reset.html')



def show_nearby_donors(request):
	you = request.user
	you_address = you.locality + ',' + you.city
	#your_location = locator.geocode(you_address)
	donors = CustomUser.objects.filter(city = you.city)
	return render(request, 'show_donors.html', {'you' : you, 'donors' : donors})


def main_page(request): ## TEMPORARY FIX
	# message = Messages.objects.filter(reciever = request.user)
	return render(request, 'home.html')


@login_required(login_url="/users/login")
def updateResources(request,emailid): # WHEN A REQUEST IS MADE BY THE RECIEVER, IT REDIRECTS HERE, to UPDATE THE RECIVER AND THE DONOR TO WHICH REQUEST IS MADE, THE NOTIFICATION LOGIC WOULD BE PRESENT HERE> JUST BEFORE REDIRECTING IT BACK TO THE PAGE.
	you = request.user
	req = 0
	them = CustomUser.objects.get(email = emailid)
	if them.resources < you.resources:
		you.resources -= them.resources
		req = them.resources
		them.resources = 0
	else:
		them.resources-=you.resources
		req = you.resources
		you.resources = 0

	# HERE WE SHOULD SEND MESSAGE TO THE SENDER ABOUT THE REQUEST.
	if req > 0:
		message = 'Hey there!!, I need resources for - ' + str(req) + ' people.'
		sendRequest = Messages(sender = you, reciever = them, message = message)
		sendRequest.save()
	#SEE ASSUMPTIONS IN README.MD!
	them.save()
	you.save()
	return redirect("showNearbyDonors")
	#+14155238886

@login_required(login_url = '/users/login')
def seeNotifications(request):
	message = Messages.objects.filter(reciever = request.user)
	context = { 'messages' : message }
	return render(request, 'notification.html', context)

@login_required(login_url = '/users/login')
def deleteNotification(request, pk):
	message = Messages.objects.get(pk = pk)
	message.delete()
	# message = Messages.objects.filter(reciever = request.user)
	# context = { 'messages' : message }
	# return render(request, 'notification.html', context)
	return render(request, 'home.html')

@login_required(login_url = '/users/login')
def readMessage(request, pk):
	message = Messages.objects.get(pk = pk)
	message.read_unread = True
	message.save()
	return render(request, 'home.html')






 