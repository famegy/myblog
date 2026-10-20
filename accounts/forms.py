from django import forms 
from . models import Profile 

class ProfileAdmin(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avator']
        