from django import forms
from django.forms import ModelForm
from registration.models import *


class RegistrationForm(ModelForm):
    state_code = forms.CharField(max_length=12, label=u'State Code')
    first_name = forms.CharField(max_length=200, label=u'First Name')
    last_name = forms.CharField(max_length=200, label=u'Last Name')
    email = forms.EmailField(null=True, label=u'Email')
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput(render_value=False))
    re_password = forms.CharField(label=u'Confirm Password', widget=forms.PasswordInput(render_value=False))

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
        if self.cleaned_data["password"] != self.cleaned_data["re_password"]:
            raise forms.ValidationError("The passwords did not match")
        elif len(self.cleaned_data["password"]) <= 6:
            raise forms.ValidationError("The password is too short, it must be more than 6")
        return self.cleaned_data


class LoginForm(forms.Form):
    state_code = forms.CharField(label=u'State Code')
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput(render_value=False))
