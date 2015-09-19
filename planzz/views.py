from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    return render_to_response('index.html')
def signup(request):
    return render_to_response('signup.html')
def login(request):
    return render_to_response('login.html')
def schedule(request):
    return render_to_response('schedule.html')
