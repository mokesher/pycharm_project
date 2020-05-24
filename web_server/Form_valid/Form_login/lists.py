from django.shortcuts import render, HttpResponse, redirect
from django.forms import Form
from django.forms import fields
from django.forms import widgets
from Form_login import models


class ClassForm(Form):
    title = fields.RegexField('全栈\d+')


class StudentForm(Form):
    name = fields.CharField(
        max_length=16,
        widget=widgets.TextInput(attrs={"class": "form-control"}),
    )
    age = fields.IntegerField(
        min_value=0,
        widget=widgets.TextInput(attrs={"class": "form-control"}),
    )
    cls_id = fields.IntegerField(
        widget=widgets.Select(attrs={"class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields["cls_id"].widget.choices = models.Classes.objects.values_list('id', 'title')


def class_list(request):
    cls_list = models.Classes.objects.all()

    return render(request, "list/class_list.html", {"cls_list": cls_list})


def add_class(request):
    if request.method == "GET":
        obj = ClassForm()

        return render(request, "list/add_class.html", {"obj": obj})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            # obj.cleaned_data
            models.Classes.objects.create(**obj.cleaned_data)
            return redirect('/class_list/')

        return render(request, "list/add_class.html", {"obj": obj})


def edit_class(request, nid):
    if request.method == "GET":
        class_obj = models.Classes.objects.filter(id=nid).first()
        obj = ClassForm(initial={"title": class_obj.title})

        return render(request, "list/edit_class.html", {"obj": obj, "nid": nid})

    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/class_list/')
        else:
            return render(request, "list/edit_class.html", {"obj": obj, "nid": nid})


def student_list(request):
    stu_list = models.Student.objects.all()

    return render(request, "list/student_list.html", {"stu_list": stu_list})


def add_student(request):
    if request.method == "GET":
        obj = StudentForm()

        return render(request, "list/add_student.html", {"obj": obj})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            # obj.cleaned_data
            models.Student.objects.create(**obj.cleaned_data)
            return redirect('/student_list/')
        else:
            return render(request, "list/add_student.html", {"obj": obj})


def edit_student(request, nid):
    if request.method == "GET":
        student_obj = models.Student.objects.filter(id=nid).first()
        obj = StudentForm(
            initial={
                "name": student_obj.name,
                "age": student_obj.age,
                "cls_id": student_obj.cls_id,
            })

        return render(request, "list/edit_student.html", {"obj": obj, "nid": nid})

    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/student_list/')

        else:
            return render(request, "list/edit_student.html", {"obj": obj, "nid": nid})
