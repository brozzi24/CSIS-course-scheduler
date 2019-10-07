from django import forms 
from . import models

class testClass(forms.ModelForm):

    
    class Meta:
        model = models.Classes
        fields = ['name','course_number','subject','min_hours','max_hours','special','grad_type','fixed_hours']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Programming'}),
            'course_number': forms.NumberInput(attrs={'placeholder': '2610'}),
            'min_hours': forms.NumberInput(attrs={'placeholder': '3'}),
            'max_hours': forms.NumberInput(attrs={'placeholder': '3'}),
        }
       
        