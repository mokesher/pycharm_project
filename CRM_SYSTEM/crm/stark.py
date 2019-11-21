from stark.service.stark import site,ModelStark
from .models import *
from django.utils.safestring import mark_safe
from django.shortcuts import render,redirect
from django.urls import re_path



class UserConfig(ModelStark):
    list_display = ["name","email","depart"]

site.register(UserInfo,UserConfig)
site.register(School)


class ClassConfig(ModelStark):

    def display_classname(self,obj=None,header=False):
        if header:
            return "班级名称"
        return f"{obj.course.name}({str(obj.semester)})"

    list_display = [display_classname,"tutor","teachers"]

site.register(ClassList,ClassConfig)
site.register(Department)
site.register(Course)

class CustomerConfig(ModelStark):

    def display_course(self,obj=None,header=False):
        if header:
            return "课程"
        temp = []
        for course in obj.course.all():
            s = f"<a href='/stark/crm/customer/cancel_course/{obj.pk}/{course.pk}' style='border:1px solid #369;padding:3px 6px'><span>{course.name}</span></a>&nbsp;"
            temp.append(s)
        return mark_safe("".join(temp))

    def cancel_course(self, request, customer_id, course_id):
        print(customer_id, course_id)
        obj = Customer.objects.filter(pk=customer_id).first()
        obj.course.remove(course_id)

        return redirect(self.get_change_url("list"))

    def extra_url(self):
        temp = []
        temp.append(re_path(r"cancel_course/(\d+)/(\d+)", self.cancel_course))
        return temp

    list_display = ["name","gender",display_course,"consultant"]

site.register(Customer,CustomerConfig)


class ConsultConfig(ModelStark):
    list_display = ["customer","consultant","date","note"]

site.register(ConsultRecord,ConsultConfig)


class CourseRecordConfig(ModelStark):
    def score(self, request, course_record_id):
        if request.method == "POST":
            print(request.POST)
            data = {}
            for key, value in request.POST.items():
                if key == "csrfmiddlewaretoken": continue
                field, pk = key.rsplit("_", 1)
                if pk in data:
                    data[pk][field] = value
                else:
                    data[pk] = {field: value}  # data  {4:{"score":90}}
            print("data", data)

            for pk, update_data in data.items():
                StudyRecord.objects.filter(pk=pk).update(**update_data)
            return redirect(request.path)
        else:
            study_record_list = StudyRecord.objects.filter(course_record=course_record_id)
            score_choices = StudyRecord.score_choices
            return render(request, "score.html", locals())

    def extra_url(self):
        temp = []
        temp.append(re_path(r"record_score/(\d+)", self.score))
        return temp

    def record(self, obj=None, header=False):
        if header:
            return "考勤"
        return mark_safe("<a href='/stark/crm/studyrecord/?course_record=%s'>记录</a>" % obj.pk)

    def record_score(self, obj=None, header=False):
        if header:
            return "录入成绩"
        return mark_safe("<a href='record_score/%s'>录入成绩</a>" % obj.pk)

    list_display = ["class_obj", "day_num", "teacher", record, record_score]


site.register(CourseRecord,CourseRecordConfig)


class StudyConfig(ModelStark):
    list_display = ["student", "course_record", "record", "score"]

    def patch_late(self, request, queryset):
        queryset.update(record="late")

    patch_late.short_description = "迟到"
    actions = [patch_late]


site.register(StudyRecord,StudyConfig)


class StudentConfig(ModelStark):
    list_display = ["customer", "class_list"]
    list_display_links = ["customer"]

site.register(Student,StudentConfig)


