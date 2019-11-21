#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from rest_framework import serializers
from.models import *


class PublishModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"


class BookModelSerializers(serializers.ModelSerializer):
    # title=serializers.CharField(max_length=32)
    # price=serializers.IntegerField()
    # publish=serializers.CharField(source="publish.name")
    # # authors=serializers.CharField(source="authors.all")
    # authors = serializers.SerializerMethodField()
    # def get_authors(self,obj):
    #     temp = []
    #     for obj in obj.authors.all():
    #         temp.append(obj.name)
    #     return temp
    class Meta:
        model = Book
        fields = "__all__"


class AuthorModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
