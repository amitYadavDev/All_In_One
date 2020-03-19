from django.shortcuts import render
from django.http import HttpResponse

#Home page
def home(request):
    return render(request, 'home.html')



#login page
def login(request):
    return render(request, 'login.html')

# Create your views here.
