from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def index(request):
    return render(request, 'driver/driver.html')