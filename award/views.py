from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(username=current_user)
        projects = Project.print_all()
        print(current_user)
    except ObjectDoesNotExist:
        return redirect('new-profile')

    return render(request,'index.html',{"profile":profile,"projects":projects})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'profile.html',{"profile":profile})
    
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('index')
    else:
        form=ProfileForm()

    return render(request,'new_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"projects/projects.html", {"project":project})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = current_user
            project.save()
        return redirect('Projects')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def project_site(request,project_site_id):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    try:
        project = Project.objects.get(id=project_site_id)
    except:
        raise ObjectDoesNotExist()

    try:
        rates = Rating.objects.filter(project_id=project_site_id)
        design = Rating.objects.filter(project_id=project_site_id).values_list('design',flat=True)
        usability = Rating.objects.filter(project_id=project_site_id).values_list('usability',flat=True)
        content = Rating.objects.filter(project_id=project_site_id).values_list('content',flat=True)
        totals_for_design=0
        totals_for_usability=0
        totals_for_content = 0
        print(design)
        for rate in design:
            totals_for_design+=rate
        print(totals_for_design)

        for rate in usability:
            totals_for_usability+=rate
        print(totals_for_usability)

        for rate in content:
            totals_for_content+=rate
        print(totals_for_content)

        average_score=(totals_for_design+totals_for_usability+totals_for_content)/3

        print(average_score)

        project.design = totals_for_design
        project.usability = totals_for_usability
        project.content = totals_for_content
        project.overall_rating = average_score

        project.save()

    except:
        return None

    if request.method =='POST':
        form = RatesForm(request.POST,request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project= project
            rating.profile = profile
            rating.average_score = (rating.design+rating.usability+rating.content)/3
            rating.save()
    else:
        form = RatesForm()

    return render(request,"projects/project_site.html",{"project":project,"profile":profile,"rates":rates,"form":form})



