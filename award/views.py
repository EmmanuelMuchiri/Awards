from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()

    return render(request,'new_profile.html',{"form":form})

