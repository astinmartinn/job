from django.shortcuts import render

# Create your views here.

def home(request):
	template='basicsite/home.html'
	return render(request,template)

def register(request):
	template='basicsite/register.html'
	return render(request,template)
	

def about(request):
	template='basicsite/about.html'
	return render(request,template)

def contact_us(request):
	template='basicsite/contact_us.html'
	return render(request,template)
