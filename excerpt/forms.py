from tkinter.ttk import Style
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FavoriteForm(forms.Form):
    favorite = forms.ChoiceField()

class CreatingUserForm(UserCreationForm):
    adres = forms.CharField()
    numr = forms.DecimalField()
    pochta = forms.DecimalField()
    ad_info = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type':"text",
            'id':"form7Example3",
            'style': 'height:100px'
        }
    ))
    class Meta:
        model = User
        fields = ['last_name', 'username', 'email', 'password1', 'password2', 'adres', 'numr', 'pochta', 'ad_info']





class CustomerUserForm(UserCreationForm):
    adres = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type':"text",
            'id':"form7Example3"
        }
    ))
    numr = forms.DecimalField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type':"number",
            'id':"form7Example4"
        }
    ))
    pochta = forms.DecimalField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type':"number",
            'id':"form7Example6"
        }
    ))
    ad_info = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id':"form7Example7"
        }
    ))
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2', 'adres', 'numr','pochta','ad_info']
        #'numr','pochta','ad_info',