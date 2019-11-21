#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.forms import Form,fields,widgets
from django.core.exceptions import ValidationError
from blog import models
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.views import View


class LoginForm(Form):
    username = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="用户名:",
        initial="test",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )

    password = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="密码：",
        initial="123",
        widget=widgets.TextInput(
            attrs={"class": "form-control", "type": "password"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短2位"
        }
    )


class RegForm(Form):
    username = fields.CharField(
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

    password = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        label="密码：",
        widget=widgets.TextInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短2位"
        }
    )

    email = fields.EmailField(
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


class SetpwdForm(Form):

    old_password = fields.CharField(
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
    new_password = fields.CharField(
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

    repeat_password = fields.CharField(
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


class SetInfoForm(Form):
    email = fields.EmailField(
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

    # pic = fields.ImageField(
    #     label="头像：",
    #     widget=widgets.FileInput(
    #         attrs={"class": "form-control"}
    #     ),
    #     error_messages={
    #         "required": "不能为空",
    #     }
    #
    # )
