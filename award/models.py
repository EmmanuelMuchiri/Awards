from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.
class Profile(models.Model):
    profpic = models.ImageField(upload_to='profpics/')
    bio = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    # function working
    def save_profile(self):
        self.save()


class Project(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='projects/', blank=True)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    average_score = models.IntegerField(blank=True,default=0)

    @classmethod
    def print_all(cls):
        project = Project.objects.all().order_by('-pub_date')
        return project
    
    def save_project(self):
        self.save()

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    
class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_rating = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)



class Subscribers(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()