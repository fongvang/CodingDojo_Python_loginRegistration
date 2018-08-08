from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if 'message' in request.session:
        request.session.clear()
    return render(request, 'index.html')

def register(request):
    users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['register_email'],
        password = request.POST['register_password'])

    if 'user' not in request.session:
        request.session['first_name'] = request.POST['first_name']

# CHECK ERRORS
    errors = users.objects.basic_validator(request.POST)
    if len(errors):
        request.session['messages'] = errors
        return redirect('/')
    return redirect('/success')



def success(request):
    return render(request, "success.html")

def login(request):
    print("in the login route")
    # return redirect('/')
    user = users.objects.filter(email = request.POST['login_email'])
    errors = users.objects.login_validator(request.POST)
    if len(errors):
        request.session['messages'] = errors
        return redirect('/')
    # user = users.objects.filter(email = request.POST['login_email'])
    if 'user' in request.session:
        request.session['first_name'] = ""
    request.session['first_name'] = user[0].first_name
    return redirect('/success')



