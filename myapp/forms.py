from django import forms
from .models import Employee, Project


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class Projectform(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
