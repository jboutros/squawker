from django import forms
from django.forms import ModelForm
from models import Squawk
 
class AddSquawkForm(forms.Form):
    squawk = forms.CharField()
