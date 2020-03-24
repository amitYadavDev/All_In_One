from django.shortcuts import render

# Create your views here.
#login page
def login(request):
    return render(request, 'login.html')



# register page
def register(request):
    return render(request, 'regist.html')