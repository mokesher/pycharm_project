from django.shortcuts import render, redirect, HttpResponse
from blog import models
from django.http import JsonResponse
import json,os
from django.db.models import F,Count
from django.conf import settings
from bs4 import BeautifulSoup
from django.views.generic import ListView,DetailView


def get_user(self):
    username = self.kwargs.get("username")
    user = models.UserInfo.objects.filter(username=username).first()
    return user


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = models.Article.objects.all()
        return article_list


class ArticleListView(IndexView):
    template_name = "blog/article_index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        return super(ArticleListView, self).get_queryset().filter(user=get_user(self))

    def get_context_data(self, **kwargs):
        kwargs['user'] = get_user(self)
        return super(ArticleListView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    template_name = "blog/article_detail.html"
    context_object_name = "article"
    model = models.Article
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        user = get_user(self)
        article_id = self.kwargs.get("article_id")
        if not user:
            return HttpResponse(404)
        comments = models.Comment.objects.filter(article_id=article_id)
        kwargs['comments'] = comments
        kwargs['user'] = user

        return super(ArticleDetailView, self).get_context_data(**kwargs)


def up_down(request):
    is_up = json.loads(request.POST.get("is_up"))
    article_id = request.POST.get("article_id")
    user = request.user
    response = {"state": True}
    try:
        models.ArticleUpDown.objects.create(user=user, article_id=article_id, is_up=is_up)
        if is_up:
            models.Article.objects.filter(pk=article_id).update(up_count=F("up_count") + 1)
        else:
            models.Article.objects.filter(pk=article_id).update(down_count=F("down_count")+1)
    except Exception as e:
        response["state"] = False
        response["fisrt_action"]=models.ArticleUpDown.objects.filter(user=user,article_id=article_id).first().is_up

    return JsonResponse(response)


def comment(request):
    content = request.POST.get("content")
    article_id = request.POST.get("article_id")
    pid = request.POST.get("pid")
    if not pid:
        comment_obj = models.Comment.objects.create(article_id=article_id,content=content,user_id=request.user.pk)
    else:
        comment_obj = models.Comment.objects.create(article_id=article_id, content=content, user_id=request.user.pk,parent_comment_id=pid)
    data= {}
    data["username"] = comment_obj.user.username
    data["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d %H:%M")
    data["content"] = comment_obj.content
    data["parent_commen_id"] = comment_obj.parent_comment_id
    data["pk"] = comment_obj.pk

    return JsonResponse(data)


def del_comment(request,username,article_id,del_id):
    models.Comment.objects.filter(pk=del_id).delete()
    return redirect(f"/blog/{username}/article/{article_id}")


def change_comment(request, pk):
    pass


def comment_tree(request,article_id):
    comment_list = list(models.Comment.objects.filter(article_id=article_id).values("pk","content","parent_comment_id","user__username","create_time"))
    for comment in comment_list:
        comment["create_time"] = comment["create_time"].strftime("%Y-%m-%d %H:%M")

    print(comment_list)
    return JsonResponse(comment_list, safe=False)


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        article_content = request.POST.get("article_content")
        soup = BeautifulSoup(article_content,"html.parser")
        desc = soup.text+"..."
        for tag in soup.find_all():
            if tag.name in ["script", "link"]:
                tag.decompose()

        article_obj = models.Article.objects.create(title=title,user=request.user,desc=desc[0:150])
        models.ArticleDetail.objects.create(content=soup.prettify(),article=article_obj)

        return HttpResponse("ok")
    return render(request, "blog/add_article.html")



def upload(request):
    obj = request.FILES.get("upload_img")
    print("name", obj.name)
    path = os.path.join(settings.MEDIA_ROOT, "article_img", obj.name)
    with open(path, "wb") as f:
        for line in obj:
            f.write(line)
    res = {
        "error": 0,
        "url": "/media/article_img/" + obj.name
    }
    return HttpResponse(json.dumps(res))





