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
            #Get html form IDs
            course_number = request.POST['course_number']
            name = request.POST['name']
            for course in classes:
                if course.course_number == int(course_number):
                    messages.error(request,'Course with {} course number already exsists'.format(course_number))
                    return redirect('index')
                elif course.name == name:
                    messages.error(request,'Course with name {} already exsists'.format(name.upper()))
                    return redirect('index')
            
            subject = request.POST['subject']
            min_hours = request.POST['min_hours']
            max_hours = request.POST['max_hours']
            fixed_hours = request.POST['fixed_hours']
            grad_type = request.POST['grad_type']

            # Add info into Model
            course = Classes(course_number=course_number, name=name,subject=subject,min_hours=min_hours,max_hours=max_hours,fixed_hours=fixed_hours,grad_type=grad_type)
            # Save info to Database
            course.save() 
            messages.success(request,'Course has been added!')
            
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