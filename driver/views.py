from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
import datetime as dt 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def driver(request):
    return render(request, 'driver/driver.html')

def driver_signup(request):
    # if request.method
    pass