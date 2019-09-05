from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# Create your views here.
def index(request):
    date = dt.date.today()
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(username=current_user)
        print(current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
        
    return render(request,'index.html',{"profile":profile})
