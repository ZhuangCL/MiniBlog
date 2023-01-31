from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    # name有規定寫法 否則讀不到
    username = forms.CharField(
        label = "帳號" ,
        widget = forms.TextInput(attrs={'placeholder' : 'user'})
    )

    email = forms.EmailField(
        label = "電子信箱",
        widget = forms.EmailInput(attrs={'placeholder' : 'email'})
    )

    password1 = forms.CharField(
        label = "密碼",
        widget = forms.PasswordInput(attrs={'placeholder' : 'password'})
    )

    password2 = forms.CharField(
        label = "密碼確認",
        widget = forms.PasswordInput(attrs={'placeholder' : 'password confirmation'})
    )

    class Meta: # 排序
        model = User
        fields = ('username', 'email', 'password1', 'password2') 