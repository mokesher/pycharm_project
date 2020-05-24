from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from app02.views import TokenAuth


class PublishView(APIView):
    authentication_classes = [TokenAuth, ]

    def get(self, request):
        publish_list = Publish.objects.all()
        bs = PublishModelSerializers(publish_list, many=True)
        return HttpResponse(bs.data)

    def post(self, request):
        ps = PublishModelSerializers(data=request.data)
        if ps.is_valid():
            print(ps.validated_data)
            ps.save()  # create方法
            return Response(ps.data)
        else:
            return Response(ps.errors)


class PublishDetailView(APIView):
    def get(self, request, pk):
        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish)
        return Response(ps.data)

    def put(self, request, pk):
        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)

    def delete(self, request, pk):
        Publish.objects.filter(pk=pk).delete()

        return Response()


class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        bs = BookModelSerializers(book_list, many=True)
        print("bs", bs)
        return Response(bs.data)

    def post(self, request):
        # post请求的数据
        bs = BookModelSerializers(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)


class BookDetailView(APIView):

    def get(self, request, pk):

        book = Book.objects.filter(pk=pk).first()
        bs = BookModelSerializers(book, context={'request': request})
        return Response(bs.data)

    def put(self, request, pk):
        book = Book.objects.filter(pk=pk).first()
        bs = BookModelSerializers(book, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, pk):
        Book.objects.filter(pk=pk).delete()
        return Response()
