from django import forms
from .models import startupModel
from django.contrib.auth.models import User

class startupModelForm(forms.ModelForm):

    class Meta:
        model = startupModel
        # fields = ['logo','name','description','founded','location','website']
        exclude = ['user']