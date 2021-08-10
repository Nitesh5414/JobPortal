from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jobapp.models import ITjobs, MECHjobs, CIVILjobs, ImageTable

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model    = User
        fields   = ['username', 'email', 'password1', 'password2']


class AddITJobsForm(forms.ModelForm):
    class Meta:
        model     = ITjobs
        fields    = '__all__'

class AddMECHJobsForm(forms.ModelForm):
    class Meta:
        model     = MECHjobs
        fields    = '__all__'


class AddCIVILJobsForm(forms.ModelForm):
    class Meta:
        model     = CIVILjobs
        fields    = '__all__'

class UpdateITJobsForm(forms.ModelForm):
    class Meta:
        model     = ITjobs
        fields    = '__all__'

class UpdateMECHJobsForm(forms.ModelForm):
    class Meta:
        model     = ITjobs
        fields    = '__all__'

class UpdateCIVILJobsForm(forms.ModelForm):
    class Meta:
        model     = ITjobs
        fields    = '__all__'

class AddImageForm(forms.ModelForm):
    class Meta:
        model     = ImageTable
        fields    = '__all__'
