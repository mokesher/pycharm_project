#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from blog import models
from django.contrib.auth.models import User
from django.http import HttpRequest


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'value': "test", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'value': "123", "class": "form-control"})


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="用户名:",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )

    email = forms.EmailField(
        label="email：",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
        }
    )

    def clean_username(self):
        reg_name = self.cleaned_data.get("username")
        if models.UserInfo.objects.filter(username=reg_name):
            self.add_error("username", ValidationError("用户名已存在"))
        else:
            return reg_name

    def clean_email(self):
        reg_email = self.cleaned_data.get("email")
        if models.UserInfo.objects.filter(email=reg_email):
            self.add_error("email", ValidationError("邮箱已注册"))
        else:
            return reg_email

    class Meta:
        model = models.UserInfo
        fields = ["username", "email", "pic"]


class SetpwdForm(ModelForm):
    old_password = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="旧密码：",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )
    new_password = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="新密码：",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )

    repeat_password = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="重复密码:",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )

    def clean(self):
        pwd = self.cleaned_data.get("new_password")
        re_pwd = self.cleaned_data.get("repeat_password")
        if pwd != re_pwd:
            self.add_error("repeat_password", ValidationError("两次密码不一致"))
        else:
            return self.cleaned_data


class SetInfoForm(ModelForm):
    email = forms.EmailField(
        label="email：",
        initial="",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
        }
    )

    class Meta:
        model = models.UserInfo
        fields = ["email", "pic"]
