from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from rest_framework.viewsets import GenericViewSet,ViewSetMixin,ModelViewSet
from api.serializers.course import CourseSerializer,CourseDetailSerializer
from api.auth.auth import TokenAuth


class CourseView(ModelViewSet):
    def list(self, request, *args, **kwargs):

        ret = {'code':1000,'data':None}

        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset,many=True)
            ret["data"] = ser.data
        except Exception as e:
            ret["code"] = 1001
            ret["data"] = "error:" + str(e)

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get("pk")
            print(pk)
            queryset = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializer(instance=queryset,many=False)
            ret["data"] = ser.data
        except Exception as e:
            ret["code"] = 1001
            ret["data"] = "error:" + str(e)

        return Response(ret)









