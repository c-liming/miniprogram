from django.db import models

# Create your models here.



class Account(models.Model):
    # 账户

    uid = models.CharField('账号', max_length=11, unique=True)
    upw = models.CharField('密码', max_length=64)
    nickname = models.CharField('昵称', max_length=8, default="")

    def __str__(self):
        return '%s' % self.nickname
