from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
  response = HttpResponse()
  return redirect('myApp:login')

def welcome(request):
  return render(request, 'myApp/welcome.html')

def login(request):
  return render(request, 'myApp/login.html')

def user_login(request):
  #return render(request, 'myApp/welcome.html')
   return redirect('myApp:welcome')
