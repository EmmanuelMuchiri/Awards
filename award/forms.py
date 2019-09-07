from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']
    
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'pub_date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class RatesForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['average_score','profile','project']
    

class SubscriptionForm(forms.Form):
    your_name = forms.CharField(label="Enter Your First Name",max_length=30)
    email = forms.EmailField(label="Enter your Email Address")