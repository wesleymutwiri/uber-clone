from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def passenger(request):
    return render(request, 'passenger/passenger.html')

def passenger_signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authentication(username=username, password=raw_password)
            login(request, user)
            return redirect('passenger')
        else:
            form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def passenger_login(request):
    form = LoginForm()
    return render(request,'registration/login.html',{"form":form})