from django.contrib import admin
from .models import Account
# Register your models here.


class AccountManager(admin.ModelAdmin):
    list_display = ['uid', 'nickname', 'upw']




admin.site.register(Account, AccountManager)