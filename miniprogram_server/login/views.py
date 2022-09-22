from email.policy import default
from django.shortcuts import render, HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def login_views(request):

    if request.method == "GET":
        # 测试
        import time
        t = time.time()
        print(t)
        test = {
            'time': t,
            'a': 'aaa',
            "ccc": 'aaaaaaaaaa'
        }
        return render(request, "login/html/login.html", test) 

    elif request.method == "POST":
        try:
            uid = Account.objects.get(uid=request.POST.get('uid'))
            upw = Account.objects.get(upw=request.POST.get('upw'))
        except ObjectDoesNotExist:
            return HttpResponse("账号或密码错误%s %s" % (request.POST.get('uid'), request.POST.get('upw')))

        print('test', uid, " ", upw)
        return render(request, "login/html/login.html")
