from django import forms
from django.forms import ModelForm, TextInput

from .models import Student_store_model


# from . import forms

class student_Edit_form(ModelForm):
    class Meta:
        model = Student_store_model
        fields = ['Name', 'Email', 'Department']
        widgets = {
            'Name': TextInput(attrs={'class': 'form-control'}),
            'Email': TextInput(attrs={'class': 'form-control', 'placeholder': 'details'}),
            'Department': TextInput(attrs={'class': 'form-control', 'placeholder': 'details'}),

        }
