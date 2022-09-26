from time import ctime
from django.db import models

# Create your models here.



class Account(models.Model):
    # 账户

    uid = models.CharField('账号', max_length=11, unique=True)
    upw = models.CharField('密码', max_length=64)
    nickname = models.CharField('昵称', max_length=8, default="")
    head_portrait = models.FileField('头像', upload_to='acc_head_portrait', null=True, default='')

    def __str__(self):
        return '%s' % self.nickname




class WebmasterStatistical(models.Model):

    # 站长统计

    remote_addr = models.CharField('IPv4', max_length=15)
    path_info = models.URLField('访问地址', max_length=200)
    ctime = models.DateTimeField('创建时间', auto_now_add=True)
    atime = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return 'IP:%s_addr:%s' % (self.remote_addr, self.path_info)
