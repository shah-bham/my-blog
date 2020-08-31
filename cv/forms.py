from django import forms

from .models import CV

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('full_name', 'email', 'website', 'mobile_number', 'job_title', 'personal_profile', 'key_skills',)