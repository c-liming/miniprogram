from email.policy import default
from hashlib import new
import re
from urllib import response
from django.shortcuts import render, HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


# Create your views here.


def login_views(request):

    if request.method == "GET":
        # 分页练习
        page_num = request.GET.get('page_num', 1)
        wms = WebmasterStatistical.objects.all().values()
        paginator = Paginator(wms, 10)
        now_page = paginator.page(int(page_num))
        if request.GET.get('load_now_page', 0):
            # 下载分页数据
            import csv
            res = HttpResponse(content_type='text/csv')
            res['content-Disposition'] = 'attachment;filename="wmsinfo-page-%s.csv"' % now_page.number
            res.charset = 'utf-8-sig'
            w = csv.writer(res)
            w.writerow(['IP地址', '浏览地址', '浏览时间'])
            for i in now_page:
                w.writerow([i.get('remote_addr'), i.get('path_info'), i.get('ctime')])
            return res
        return render(request, "login/html/login.html", locals()) 

    elif request.method == "POST":
        try:
            uid = Account.objects.get(uid=request.POST.get('uid'))
            upw = Account.objects.get(upw=request.POST.get('upw'))
        except ObjectDoesNotExist:
            return HttpResponse("账号或密码错误%s %s" % (request.POST.get('uid'), request.POST.get('upw')))

        print('test', uid, " ", upw)
        return render(request, "login/html/login.html")



def load_wmsinfo(request):
    import csv
    wms = WebmasterStatistical.objects.all()
    res = HttpResponse(content_type='text/csv')
    res['content-Disposition'] = 'attachment;filename="wmsinfo.csv"'
    res.charset = 'utf-8-sig'
    w = csv.writer(res)
    w.writerow(['IP地址', '浏览地址', '浏览时间'])

    for i in wms:
        w.writerow([i.remote_addr, i.path_info, i.ctime])

    return res



def reg_acc(request):
    if request.method == "GET":
        return render(request, 'login/html/reg_acc.html')

    if request.method == 'POST':
        uid = request.POST.get('uid')
        upw = request.POST.get('upw')
        upw_again = request.POST.get('upw_again')
        nickname = request.POST.get('nickname')
        head_portrait = request.FILES.get('head_portrait')
        try:
            Account.objects.get(uid=uid)
            return HttpResponse('账号已被注册')
        except:
            if upw == upw_again and len(upw) >= 5:
                new_acc = Account(uid=uid, upw=upw)
                if len(nickname) > 8:
                    return HttpResponse('昵称太长了')
                new_acc.nickname = nickname
                new_acc.head_portrait = head_portrait
                new_acc.save()
                return HttpResponse('注册成功' )
            else:
                return HttpResponse('注册失败，密码太短')

