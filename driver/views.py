from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
import datetime as dt 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def driver(request):
    return render(request, 'driver/driver.html')

def driver_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authentication(username=username, password=raw_password)
            login(request, user)
            return redirect('driver')
        else:
            form = SignUpForm()
            return render(request, 'registration/signup.html', {'form': form})
            
    