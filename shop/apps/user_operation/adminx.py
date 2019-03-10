__author__ = 'xiao tang'
__date__ = '2019/1/26 15:34'

import xadmin

from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin:
    list_display = ['user', 'goods', 'add_time']
    search_fields = ['user', 'goods']
    list_filter = ['user', 'goods', 'add_time']


class UserLeavingMessageAdmin:
    list_display = ['user', 'msg_type', 'subject', 'message', 'file', 'add_time']
    search_fields = ['user', 'msg_type', 'subject', 'message', 'file']
    list_filter = ['user', 'msg_type', 'subject', 'message', 'file', 'add_time']


class UserAddressAdmin:
    list_display = ['user', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time']
    search_fields = ['user', 'district', 'address', 'signer_name', 'signer_mobile']
    list_filter = ['user', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time']


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
