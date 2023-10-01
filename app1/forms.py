from django.forms import ModelForm
from django import forms

from pyexpat import model
from dataclasses import fields

from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'email' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs = {'class' : 'form-control'}, render_value = True)
        }