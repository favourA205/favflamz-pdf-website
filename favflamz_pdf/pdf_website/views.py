from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import RegistrationData
import time
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup

# Create your views here.


def home(request):

    return render(request, 'base.html')

def download_page(request):

    select1 = request.POST.get('search1')
    print(select1)

    context = {
        'form':RegistrationForm,
        'search1':select1



    }

    return render(request, 'download page.html',context)

def addUser(request):
    register = RegistrationForm(request.POST)

    if register.is_valid():
        myregister = RegistrationData(full_name = register.cleaned_data['full_name'],
                                    password=register.cleaned_data['password'],
                                    Email=register.cleaned_data['Email'],
                                    Phone_number=register.cleaned_data['phone_number'],
                                    name_of_subject=register.cleaned_data['name_of_subject'],
                                    )
        myregister.save()


    return redirect('interjection page')

def interjection_page(request):
    
    select1 = request.POST.get('search1')
    print(select1)


    context = {
        'search1': select1,

    }

    return render(request, 'interjection page.html',context)



