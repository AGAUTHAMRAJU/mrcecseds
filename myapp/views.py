from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    return render (request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')
    
        


