from django.shortcuts import render , redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('signin')

    return render(request,'login/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('signin')