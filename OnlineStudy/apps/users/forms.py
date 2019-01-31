__author__ = 'xiao tang'
__date__ = '2019/1/30 20:17'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)