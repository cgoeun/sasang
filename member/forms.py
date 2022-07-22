from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    # user_name = forms.CharField(label="이름")
    # user_birth = forms.DateField(label="생년월일")
    # user_gender = forms.IntegerField(label="성별")
    class Meta:
        model = User
        fields = ("username",)
