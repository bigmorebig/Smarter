from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True,max_length=50,default='')
    user = models.CharField(max_length=20,verbose_name='用户名')
    phone_num = models.CharField(max_length=20,verbose_name='手机号')
    passwd = models.CharField(max_length=20,verbose_name='登录密码')
    confirm_passwd = models.CharField(max_length=20,verbose_name='确认密码')
    verfication_code = models.CharField(max_length=6,verbose_name='验证码')

    class Meta:
        verbose_name = '注册新用户'
        # db_table = 'user_message'   #指定表的名字
        # ordering = 'object_id'      #指定根据object_id字段排序
        verbose_name_plural = verbose_name