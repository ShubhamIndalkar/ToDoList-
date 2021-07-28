
from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    Title = forms.CharField(widget=forms.TextInput({"placeholder":"Enetr Title"}))
    Description = forms.CharField(widget=forms.TextInput({"placeholder":"Enter Description"}))
    
