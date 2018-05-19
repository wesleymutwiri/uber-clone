from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth.decorators import login_required
import datetime as dt 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import login, authenticate
import requests
# Create your views here.
def driver(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' %ip_address)
    geodata = response.json()
    data = {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyDl-4iWCTsY4LCY4q3BgkJyZ_dzd5K-1aw',
    }
    return render(request, 'driver/driver.html', data)

def driver_signup(request):
    # form = SignUpForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('driver')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
            
def driver_login(request):
    form = LoginForm()
    return render(request,'registration/login.html',{"form":form})