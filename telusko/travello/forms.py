from django import forms
from .models import Destination
from django import forms

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
