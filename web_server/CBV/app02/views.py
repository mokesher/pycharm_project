from django.shortcuts import render
from app01.models import *
from app01.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from .utils import TokenAuth, MyPagination


class AuthorView1(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorDetailView1(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AuthorView2(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers


class AuthorDetailView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers


def get_random_str(user):
    import hashlib, time
    ctime = str(time.time())
    md5 = hashlib.md5(bytes(user, encoding="utf8"))
    md5.update(bytes(ctime, encoding="utf8"))

    return md5.hexdigest()


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, reqeust):
        name = reqeust.POST.get("name")
        pwd = reqeust.POST.get("pwd")
        user_obj = UserInfo.objects.filter(name=name, pwd=pwd).first()
        res = {"state_code": 1000, "msg": None}
        if user_obj:
            random_md5 = get_random_str(user_obj.name)
            token = Token.objects.update_or_create(user=user_obj, defaults={"token": random_md5})
            res["msg"] = random_md5
        else:
            res["state_code"] = 1001
            res["msg"] = "用户名或者密码错误"

        import json
        return Response(json.dumps(res, ensure_ascii=False))

    def get(self, request):

        return render(request, "login.html")


class AuthorModelView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []  # 限制某个IP每分钟访问次数不能超过20次
    pagination_class = MyPagination
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers
    #
    # def list(self, request, *args, **kwargs):
    #     author_list = Author.objects.all()
    #
    #     pager = MyPagination()
    #     data = pager.paginate_queryset(queryset=author_list,request=request,view=self)
    #     bs = AuthorModelSerializers(data,many=True)
    #
    #     return pager.get_paginated_response(bs.data)

    from rest_framework.decorators import action

    @action(methods=['get'], detail=False)
    def test(self, request):
        temp = {}
        temp["path"] = request.path
        temp["path_info"] = request.path_info
        import json

        return Response(json.dumps(temp, ensure_ascii=False))
