from django.shortcuts import render, redirect,HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def ajax_test(request):
    if request.method == "POST":
        i1 = request.POST.get("i1")
        i2 = request.POST.get("i2")
        i3 = int(i1) + int(i2)

        return JsonResponse(i3, safe=False)

    return render(request, "Test/ajax_test.html")

def test(request):
    from blog.models import Teacher
    from django.core import serializers
    Teacher_list = Teacher.objects.all()[:10]
    data = serializers.serialize("json", Teacher_list)
    return HttpResponse(data)


