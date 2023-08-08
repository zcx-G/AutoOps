from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号码')
    # upload_to 表示上传文件的存储子路由，需要在settings配置中，配置上传文件的支持
    avatar = models.ImageField(upload_to='avatar', verbose_name='用户头像', null=True, blank=True)

    class Meta:
        db_table = 'ao_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
