from email.policy import default
from django.shortcuts import render, HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def login_views(request):

    if request.method == "GET":
        return render(request, "login/html/login.html") 

    elif request.method == "POST":
        try:
            uid = Account.objects.get(uid=request.POST.get('uid'))
            upw = Account.objects.get(upw=request.POST.get('upw'))
        except ObjectDoesNotExist:
            return HttpResponse("账号或密码错误%s %s" % (request.POST.get('uid'), request.POST.get('upw')))

        print('test', uid, " ", upw)
        return render(request, "login/html/login.html")
