from django.shortcuts import render
from .forms import Registration, Login
from django.http import HttpResponseRedirect

def index(req):
    return render(req, 'index.html', context={'form': Registration, 'form1': Login})

def registartion(req):
    info = req.POST
    return render(req, 'registration.html', context={'info': info})

def login(req):
    info = req.POST
    if req.POST['name'] == 'Admin' and req.POST['password'] == "Admins":
        return render(req, 'login.html', context={'info':info})
    else:
        return HttpResponseRedirect('/')