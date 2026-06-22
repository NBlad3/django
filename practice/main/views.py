from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def copy(request, name):
    return HttpResponse(f'Hello {name}')

def copy2(request, age):
    data = {
        'age': age
    }
    return render(request, 'copy2.html', data)

def points(request, math, english, physics):
    data = {
        'points': (math + english + physics) / 3,
        'subjects': ['Math', 'English', 'Physics']
    }
    return render(request, 'points.html', data)

def numbers(request, nums):
    return render(request, 'numbers.html', {'nums': range(1, nums + 1)})