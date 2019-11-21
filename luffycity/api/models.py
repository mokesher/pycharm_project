from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class UserToken(models.Model):
    user = models.OneToOneField(to=UserInfo,on_delete=models.CASCADE)
    token = models.CharField(max_length=128)


class Course(models.Model):
    title = models.CharField(verbose_name="课程名称",max_length=32)
    course_img = models.CharField(verbose_name="课程图片",max_length=64)
    level_choice = (
        (1,"初级"),
        (2,"中级"),
        (3,"高级"),
    )
    level = models.IntegerField(verbose_name="课程难易程度",choices=level_choice,default=1)

    policy_list = GenericRelation("PricePolicy")

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    course = models.OneToOneField(to="Course",on_delete=models.CASCADE)
    slogon = models.CharField(verbose_name="口号",max_length=64)
    why = models.CharField(verbose_name="为什么学习？",max_length=64)
    recommend_courses = models.ManyToManyField(verbose_name="推荐课程",to="Course",related_name="rc")

    def __str__(self):
        return "课程详细："+self.course.title

class Capter(models.Model):
    num = models.IntegerField(verbose_name="章节")
    name = models.CharField(max_length=32)
    course = models.ForeignKey(verbose_name='所属课程', to='Course',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DegreeCourse(models.Model):
    title = models.CharField(max_length=32,unique=True)
    course_img = models.CharField(max_length=255)
    brief = models.TextField()


class PricePolicy(models.Model):
        content_type = models.ForeignKey(to=ContentType,on_delete=models.CASCADE)
        object_id = models.PositiveIntegerField()
        # 不会在数据库生成列，只用于帮助你进行添加和查询
        content_object = GenericForeignKey('content_type', 'object_id')

        valid_period_choices = (
            (1, '1天'),(3, '3天'),
            (7, '1周'), (14, '2周'),
            (30, '1个月'),(60, '2个月'),
            (90, '3个月'),(180, '6个月'), (210, '12个月'),
            (540, '18个月'), (720, '24个月'),
        )
        valid_period = models.SmallIntegerField(choices=valid_period_choices)
        price = models.FloatField()




