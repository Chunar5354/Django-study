from django import forms

from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

class UserRegisterForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	password2 = forms.CharField()
	email = forms.CharField()

