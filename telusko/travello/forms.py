from django import forms
from .models import Destination
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
