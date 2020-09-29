from django import forms
from .models import RegistrationData

class RegistrationForm(forms.Form):

    full_name =forms.CharField(max_length=120,
                               widget= forms.TextInput(attrs={
                                   'placeholder':'Enter full name'
                               }))



    password = forms.CharField(max_length=120,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter password'
                               }))

    Email = forms.EmailField(max_length=120,
                             widget=forms.EmailInput(attrs={
                                 'class':'form-control',
                                 'placeholder': 'Enter Email address'
                             }))

    phone_number = forms.CharField(max_length=120,
                                   widget=forms.NumberInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Enter phone number'
                                   }))

    name_of_subject = forms.CharField(max_length=120,
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control',

                                          'placeholder': 'Enter subject'
                                      }))



    