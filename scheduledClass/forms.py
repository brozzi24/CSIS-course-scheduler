

from django import forms 
from .models import Scheduled
from rooms.models import Rooms
from django.forms import ModelChoiceField

from rooms import models 



class roomForm(forms.Form):
    M = forms.BooleanField(required=False)
    t = forms.BooleanField(required=False)
    w = forms.BooleanField(required=False)
    h = forms.BooleanField(required=False)
    f = forms.BooleanField(required=False)
    web = forms.BooleanField(required=False)
    test = forms.ChoiceField(choices=[(Rooms.room_number, Rooms.room_number) for room in Rooms.objects.all()])
    
    
        


    