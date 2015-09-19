from django.shortcuts import render

# Create your views here.

def index(request):
    return render_to_response('/static/index.html')

def friends(request):
    return render_to_response('/static/friends.html')

def profile(request):
    return render_to_response('/static/profile.html')
