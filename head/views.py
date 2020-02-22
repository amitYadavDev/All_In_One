from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'log.html')

# Create your views here.
