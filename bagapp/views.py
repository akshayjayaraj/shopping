from django.shortcuts import render
from bagapp.models import*

# Create your views here.

def index(request):
	return render(request,'index.html')


def about(request):
	return render(request,'about.html')	


def coming(request):
	return render(request,'coming.html')


def contact(request):
	return render(request,'contact.html')


def login(request):
	return render(request,'login.html')	


def register(request):
	return render(request,'register.html')


def shop(request):
	return render(request,'shop.html')


def single(request):
	return render(request,'single.html')