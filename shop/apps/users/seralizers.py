__author__ = 'xiao tang'
__date__ = '2019/4/7 15:46'
from django.contrib.auth import get_user_model
from rest_framework import serializers
import re
from datetime import datetime, timedelta
from shop.settings import REGEX_MOBILE
from .models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validated_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """

        # 手机是否注册
        if User.object.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')

        # 验证码发送频率
        one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago, mobile=mobile).count():
            raise serializers.ValidationError('距离上一次发送未超过60秒')

        return mobile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        mobile = User
        fileds = ('username', 'code')