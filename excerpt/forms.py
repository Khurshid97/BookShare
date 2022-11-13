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
    # ad_info = forms.CharField(max_length=300, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'type':"text",
    #         'id':"form7Example3",
    #         'style': 'height:100px'
    #     }
    # ))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'adres', 'numr']

