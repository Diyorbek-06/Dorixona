from django import forms
from .models import Dori

class DoriForm(forms.ModelForm):
    class Meta:
        model = Dori
        fields = '__all__'