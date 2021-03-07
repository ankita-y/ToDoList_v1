from django import forms
from django.forms import ModelForm

from .models import Task

class ToDoForm(forms.ModelForm):
    title= forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Title'}),)
    desc= forms.CharField(required=False, widget= forms.Textarea(attrs={'placeholder':'Enter description here'}),)

    class Meta:
        model = Task
        #fields = ['title','desc','created']
        fields = "__all__"
    