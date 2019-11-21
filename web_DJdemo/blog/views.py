from django.shortcuts import HttpResponse, render, redirect
from blog import models
from django.urls import reverse
from django.core.paginator import Page,Paginator


class PageInfo(object):
    def __init__(self,current_page,all_count,per_page=4,show_page=7,base_url="/blog/custom/"):
        try:
            self.current_page = int(current_page)
        except:
            self.current_page = 1
        self.per_page = per_page
        a, b = divmod(all_count, per_page)
        if b:
            a += 1
        self.all_page = a
        self.base_url = base_url
        self.show_page = show_page

    def start(self):
        return (self.current_page-1)*self.per_page

    def end(self):
        return self.current_page*self.per_page

    def page(self):
        page_list = []
        half = int((self.show_page - 1) / 2)
        if self.all_page < self.show_page:
            begin = 1
            stop = self.all_page + 1
            # 如果数据总页数 > 11
        else:
            # 如果当前页 <=5,永远显示1,11
            if self.current_page <= half:
                begin = 1
                stop = self.show_page + 1
            else:
                if self.current_page + half > self.all_page:
                    begin = self.all_page - self.show_page + 1
                    stop = self.all_page + 1
                else:
                    begin = self.current_page - half
                    stop = self.current_page + half + 1

        if self.current_page <= 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='%s?page=%s'>上一页</a></li>" % (self.base_url, self.current_page - 1,)
        page_list.append(prev)

        for i in range(begin, stop):
            if i == self.current_page:
                temp = "<li class='active'><a  href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            page_list.append(temp)

        if self.current_page >= self.all_page:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='%s?page=%s'>下一页</a></li>" % (self.base_url, self.current_page + 1,)
        page_list.append(nex)

        res = " ".join(page_list)
        return res


def custom(request):
    all_count = models.Teacher.objects.all().count()
    page_info = PageInfo(request.GET.get("page"),all_count)
    user_list = models.Teacher.objects.all()[page_info.start():page_info.end()]

    return render(request, "blog/custom.html", {"pages": user_list,"page_info": page_info})


def teacher_list(request):
    current_page = request.GET.get("page")
    ret = models.Teacher.objects.all()
    paginator = Paginator(ret, 10)
    pages = paginator.page(current_page)

# 跨表
    #正向
    # t1 = models.Teacher.objects.all().first()       #1对象object
    # print("#1",t1.id,t1.teacher,t1.theclass_id)
    # t2 = models.Teacher.objects.filter(id=1).values("id","teacher","theclass__class_name")  #queryset [字典]
    # print("#2",t2)
    # t3 = models.Teacher.objects.values_list("id", "teacher", "theclass__class_name")  #queryset [元组]
    # print("#3", t3)

    #反向
    obj1 = models.Classes.objects.all().first()     #obj
    # obj = obj1.teacher_set.all()
    c1 = obj1.teacher_set.values()
    print("c1",c1)
    # print("obj1",[ (i.teacher,i.theclass_id) for i in obj ])

    c2 = models.Classes.objects.filter(class_name="一班").values("class_name","teacher__id","teacher__teacher")
    print("c2",c2)

    return render(request, "blog/teacher_list.html", {"pages": pages})



def orm(request):
    # 排序
    # teacher_list = models.Teacher.objects.all().order_by('-id', "-teacher")
    # print(teacher_list)
    #分组
    # from django.db.models import Count, Sum, Max, Min
    # group = models.Teacher.objects.values("theclass_id").annotate(num=Count('teacher'))
    # print(group)

    # 高级操作
    # F获取上次值，进行更新
    from django.db.models import F, Q
    # obj = models.UserInfo.objects.all().update(age=F("age")+8)
    # Q 复杂条件
    # condition = {
    #     'id':1,
    #     'age':23,
    # }
    # obj = models.UserInfo.objects.filter(id=1, age=23)
    # obj = models.UserInfo.objects.filter(**condition)
    # models.UserInfo.objects.filter(Q(id=1) | Q(id=2))   #or
    # models.UserInfo.objects.filter(Q(id=1) & Q(age=23))   #and
    # extra
    # obj = models.Teacher.objects.all().extra(
    #     select={
    #         "num":"select count(1) from blog_teacher where id<%s and id>%s"},
    #         select_params=(15,2))
    # for i in obj:
    #     print(i.teacher,i.num)
    # result = models.Teacher.objects.all().extra(
    #     where=['blog_userinfo.id < %s '],
    #     params=[20, ],
    #     tables = ['blog_userinfo'],
    #     select = {'n':"select count(1) from blog_userinfo"}
    # )
    # print(result)
    # 原生sql
    # from django.db import connection, connections
    # cursor = connection.cursor()
    # # cursor = connections['db2'].cursor()
    # cursor.execute("select * from blog_teacher where id>%s", [2])
    # row = cursor.fetchall()
    # print(row)

    return HttpResponse("ok")


def many(request):
    models.U2U.objects.create(b_id=1,g_id=3)
    models.U2U.objects.create(b_id=2,g_id=3)
    models.U2U.objects.create(b_id=2,g_id=9)
    models.U2U.objects.create(b_id=1,g_id=4)

    # boy = models.UserInfo.objects.filter(gender=1,id=1).first()
    # girl = models.UserInfo.objects.filter(gender=2,id=3).first()
    # models.U2U.objects.create(b=boy,g=girl)

    # x = models.UserInfo.objects.filter(id=1).first()
    # result = x.girls.all()
    # for u in result:
    #     print(u.g.student)
    return render(request, "many.html")