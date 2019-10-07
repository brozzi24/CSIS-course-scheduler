from django import forms 
from . import models


class roomClass(forms.ModelForm):
    class Meta:
        model = models.Rooms
        fields = ['room_number','room_type','capcity']
        widgets = {
            'room_number': forms.NumberInput(attrs={'placeholder': '350'}),
            'capcity': forms.NumberInput(attrs={'placeholder': '30'}),
        }

 
        