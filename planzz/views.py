from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render_to_response('index.html')
def signup(request):
    return render_to_response('signup.html')
def login(request):
    return render_to_response('login.html')

@csrf_exempt
def signupprocess(request):
    email = request.POST['email']
    password = request.POST['password']

    return HttpResponse("ok")

def schedule(request):
    return render_to_response('schedule.html')

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/account/logedin/')
    else:
        return HttpResponseRedirect('/account/invalid/')

def profile(request):
    return render_to_response('registration/profile.html', {'username':request.user.username, 'user':request.user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/accounts/signup/success/')
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, RequestContext(request))

# def signup_success(request):
#     return render_to_response('registration/signup_success.html')

def invite(request):
    return render_to_response('invite.html');

def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = UserCreationForm()
    return render_to_response('index.html', {
        'form': form,
    }, RequestContext(request))
