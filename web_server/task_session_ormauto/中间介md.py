#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin


class M1(MiddlewareMixin):
    def process_request(self, request):
        print("M1.process_request")
        # return request

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("M1.process_view")
        response = callback(request, *callback_args, **callback_kwargs)
        return response

    def process_response(selfs, request, response):
        print("M1.process_response")
        return response


class M2(MiddlewareMixin):

    def process_request(self, request):
        print("M2.process_request")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("M2.process_view")

    def process_response(selfs, request, response):
        print("M2.process_response")
        return response
