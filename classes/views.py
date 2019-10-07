from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import forms

from .models import Classes

# Create your views here.
def index(request):
    # Check if POST method used
    if request.method == 'POST':
        #Get html form IDs
        course_number = request.POST['course_number']
        name = request.POST['name']
        subject = request.POST['subject']
        min_hours = request.POST['min_hours']
        max_hours = request.POST['max_hours']
        fixed_hours = request.POST['fixed_hours']
        grad_type = request.POST['grad_type']

        # Add info into Model
        course = Classes(course_number=course_number, name=name,subject=subject,min_hours=min_hours,max_hours=max_hours,fixed_hours=fixed_hours,grad_type=grad_type)
        # Save info to Database
        course.save()
        # Return to Classes/Home page
        return redirect('index')


    # Grab vars needed for context
    form = forms.testClass()
    classes = Classes.objects.all()
    CONTEXT = {
        'form': form,
        'classes': classes
    }
    # Render the dynamic html page
    return render(request, 'classes/classes.html',CONTEXT)