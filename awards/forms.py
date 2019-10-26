from django import forms
from .models import Projects,Profile


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'profile','user_id']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }