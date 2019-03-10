__author__ = 'xiao tang'
__date__ = '2019/1/26 15:34'

import xadmin

from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin:
    list_display = ['user', 'goods', 'goods_num', 'add_time']
    search_fields = ['user', 'goods', 'goods_num']
    list_filter = ['user', 'goods', 'goods_num', 'add_time']


class OrderInfoAdmin:
    list_display = ['user', 'order_sn', 'trade_no', 'pay_status', 'post_script', 'order_mount', 'pay_time', 'address',
                    'signer_name', 'signer_mobile', 'add_time']
    search_fields = ['user', 'order_sn', 'trade_no', 'pay_status', 'post_script', 'order_mount', 'pay_time', 'address',
                     'signer_name', 'signer_mobile']
    list_filter = ['user', 'order_sn', 'trade_no', 'pay_status', 'post_script', 'order_mount', 'pay_time', 'address',
                   'signer_name', 'signer_mobile', 'add_time']


class OrderGoodsAdmin:
    list_display = ['order', 'goods', 'goods_num', 'add_time']
    search_fields = ['order', 'goods', 'goods_num']
    list_filter = ['order', 'goods', 'goods_num', 'add_time']


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)
