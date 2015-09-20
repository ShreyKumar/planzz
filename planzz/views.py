from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django import forms
from templates import forms

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render_to_response('index.html')
def signup(request):
    return render_to_response('signup.html')

def login(request):
    return render_to_response('login.html');

@csrf_exempt
def loginprocess(request):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    print(user)
    if (user is not None):
        return HttpResponse('Logged in')
    else:
        return HttpResponse('Username or Password incorrect.')
    return render_to_response('login.html')

@csrf_exempt
def signupprocess(request):
    form = forms.RegisterForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['password'] == form.cleaned_data['confirm']:
            form.save()
            return render_to_response('schedule.html')
    
    return render_to_response('signup.html')
    
    #print(email)
    #print(password)
    
    #student = Student()

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

def friends(request):
    return render_to_response('friends.html')
    
