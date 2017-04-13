from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from .models import Courses

def index(request):
    context = {
     "courses": Courses.objects.all()
    }
    return render (request, "addcourses/index.html",context)

def courses(request):
    Courses.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def delete(request,id):
    Courses.objects.filter(id=id).delete()
    return redirect('/')

def show(request,id):
    context = {
        "courses": Courses.objects.filter(id=id)
    }
    return render (request, "addcourses/show.html",context)
