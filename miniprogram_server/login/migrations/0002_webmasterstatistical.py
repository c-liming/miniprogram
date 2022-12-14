# Generated by Django 3.2 on 2022-09-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebmasterStatistical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_addr', models.CharField(max_length=15, verbose_name='IPv4')),
                ('path_info', models.URLField(verbose_name='访问地址')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('atime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
    ]
