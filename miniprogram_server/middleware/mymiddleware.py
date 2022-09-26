from django.utils.deprecation import MiddlewareMixin
from login.models import WebmasterStatistical as WS
from django.db.models import Count
from django.http.response import HttpResponse


class MyMW(MiddlewareMixin):

    def process_request(self, request):

        print('请求ID:', request.META['REMOTE_ADDR'], '|', '请求地址', request.path_info)
        print()
        remote_addr = request.META['REMOTE_ADDR']
        path_info = request.path_info
        # addr_times = WS.objects.filter(remote_addr=remote_addr)
        """if addr_times:
            addr_times_ann = addr_times.values('path_info').annotate(Count('path_info'))
            print('addr_times_ann',addr_times_ann)
            # /login 访问次数限制，如果超过次数，限制访问，未超过次数则添加一次访问次数
            for i in addr_times_ann:
                if i.get('path_info') == '/login' and i['path_info__count'] >= 5:
                    return HttpResponse('您超过了访问次数上限')
            else:
                print('request_ok')"""
        WS.objects.create(remote_addr=remote_addr, path_info=path_info)
