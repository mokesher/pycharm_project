#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from rest_framework.authentication import BaseAuthentication
from app01.models import *
from rest_framework import exceptions
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
import time


class MyPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 3



class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("no token")
        else:
            return token_obj.user.name,token_obj.token


class SVIPPermission:
    message = "用户权限不够"
    def has_permission(self,request,view):
        username = request.user
        user_obj = UserInfo.objects.filter(name=username).first()
        if user_obj:
            user_type = user_obj.user_type

            if user_type == 3:
                return True
        else:
            return False

VISIT_RECORD = {}
class VisitRateThrottle:
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        """
        自定义频率限制60秒内只能访问三次
        """
        # 获取用户IP
        ip = request.META.get("REMOTE_ADDR")
        timestamp = time.time()
        if ip not in VISIT_RECORD:
            VISIT_RECORD[ip] = [timestamp, ]
            return True
        history = VISIT_RECORD[ip]
        self.history = history
        history.insert(0, timestamp)
        while history and history[-1] < timestamp - 60:
            history.pop()
        if len(history) > 3:
            return False
        else:
            return True

    def wait(self):
        """
        限制时间还剩多少
        """
        timestamp = time.time()
        return 60 - (timestamp - self.history[-1])



