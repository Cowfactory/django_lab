from django.forms import ModelForm, Form, CharField, PasswordInput, CheckboxSelectMultiple
from .models import Skill

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())
