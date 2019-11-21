from api import models
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")
    class Meta:
        model = models.Course
        fields = ["title","course_img","level"]



class CourseDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="course.title")
    course_img = serializers.CharField(source="course.course_img")
    level = serializers.CharField(source="course.get_level_display")
    recommends = serializers.SerializerMethodField()
    capters = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ["title","course_img","level","slogon","why","recommends","capters"]

    def get_recommends(self,obj):
        return [{'id':row.id,'title':row.title} for row in obj.recommend_courses.all()]

    def get_capters(self,obj):
        queryset = obj.course.capter_set.all()

        return [{'id': row.id, 'name': row.name} for row in queryset]