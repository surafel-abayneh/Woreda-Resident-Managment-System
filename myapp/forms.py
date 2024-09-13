from django import forms
from .models import PersonalInformation

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = '__all__'
