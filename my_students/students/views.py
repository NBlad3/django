from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Student

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

def form(request):
    template = loader.get_template("form.html")
    return HttpResponse(template.render())

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, "students.html", context)