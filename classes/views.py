from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import forms

from .models import Classes

# Create your views here.
def index(request):
    # Check if user is logged in
    if request.user.is_authenticated:
        # Grab vars needed for context
        form = forms.testClass()
        classes = Classes.objects.all()
        # Check if POST method used
        if request.method == 'POST':
            for course in classes:
                if course.name == request.POST['name']:
                    messages.error(request,'There is already a course matching that course name')
                    return redirect('index')
                if course.course_number == int(request.POST['course_number']):
                    messages.error(request,'There is already a course number mathcing that course number')
                    return redirect('index')
            #Get html form IDs
            messages.success(request, 'Class has been added')
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


        
        CONTEXT = {
            'form': form,
            'classes': classes
        }
        # Render the dynamic html page
        return render(request, 'classes/classes.html',CONTEXT)
    else:
        messages.error(request,'You must be signed in to view page')
        return redirect('signin')