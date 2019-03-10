__author__ = 'xiao tang'
__date__ = '2019/1/26 15:34'

import xadmin

from .models import GoodsCategory, GoodsCategoryBrand, Goods, GoodsImage, Banner


class GoodsCategoryAdmin:
    list_display = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab', 'add_time']
    search_fields = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab']
    list_filter = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab', 'add_time']


class GoodsCategoryBrandAdmin:
    list_display = ['category', 'name', 'desc', 'image', 'add_time']
    search_fields = ['category', 'name', 'desc', 'image']
    list_filter = ['category', 'name', 'desc', 'image', 'add_time']


class GoodsAdmin:
    list_display = ['category', 'goods_sn', 'name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price',
                    'shop_price', 'goods_brief', 'goods_desc', 'ship_free', 'goods_front_image', 'is_new', 'is_hot',
                    'add_time']
    search_fields = ['category', 'goods_sn', 'name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price',
                     'shop_price', 'goods_brief', 'goods_desc', 'ship_free', 'goods_front_image', 'is_new', 'is_hot']
    list_filter = ['category', 'goods_sn', 'name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price',
                   'shop_price', 'goods_brief', 'goods_desc', 'ship_free', 'goods_front_image', 'is_new', 'is_hot',
                   'add_time']
    style_fields = {'goods_desc': 'ueditor'}


class GoodsImageAdmin:
    list_display = ['goods', 'image', 'image_url', 'add_time']
    search_fields = ['goods', 'image', 'image_url']
    list_filter = ['goods', 'image', 'image_url', 'add_time']


class BannerAdmin:
    list_display = ['goods', 'image', 'index', 'add_time']
    search_fields = ['goods', 'image', 'index']
    list_filter = ['goods', 'image', 'index', 'add_time']


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
