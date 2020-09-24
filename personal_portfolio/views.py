from django.shortcuts import render
from .models import Project

def home(request):
    # single line of code to grab each and every data from the database
    # turns them into python objects and put it into list
    # gives all the objects
    projects = Project.objects.all()
    
    return render(request,'personal_portfolio/home.html',{'projects' : projects})
