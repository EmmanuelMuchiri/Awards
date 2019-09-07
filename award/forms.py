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