from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Profile


def home(request):
    return render(request, 'myapp/home.html')

def profile(request):
    return render(request, 'myapp/profile.html')