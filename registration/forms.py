from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from registration.models import *


class RegistrationForm(ModelForm):
    state_code = forms.CharField(max_length=12, label=u'STATE CODE')
    first_name = forms.CharField(max_length=200, label=u'FIRST NAME')
    last_name = forms.CharField(max_length=200, label=u'LAST NAME')
    email = forms.EmailField(null=True, label=u'Email')
    password = forms.CharField(label=u'PASSWORD', widget=forms.PasswordInput(render_value=False))
    re_password = forms.CharField(label=u'CONFIRM PASSWORD', widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Registration
        exclude = 'corper'

    def clean_state_code(self):
        state_code = self.cleaned_data['state_code']
        try:
            User.objects.get(username=state_code)
        except User.DoesNotExist:
            return state_code
        raise forms.ValidationError("Please Enter you real state code.")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("That email is already taken, please select another.")

    def clean_password1(self):
        if self.cleaned_data["password"] != self.cleaned_data["password1"]:
            raise forms.ValidationError("The passwords did not match or password is too short")
        elif len(self.cleaned_data["password"]) <= 6:
            raise forms.ValidationError("The password is too short")
        return self.cleaned_data
