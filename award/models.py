from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profpic = models.ImageField(upload_to='profpics/')
    bio = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name