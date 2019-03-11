__author__ = 'xiao tang'
__date__ = '2019/3/11 18:01'
import sys, os
import django


# 独立使用Django的model

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
django.setup()

from goods.models import Goods, GoodsCategory, GoodsImage
from db_tools.data.product_data import row_data


for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail['name']
    goods.market_price = float(goods_detail['market_price'].replace('￥', '').replace('元', ''))
    goods.shop_price = float(goods_detail['sale_price'].replace('￥', '').replace('元', ''))
    goods.goods_brief = goods_detail['desc'] if goods_detail['desc'] is not None else ''
    goods.goods_desc = goods_detail['goods_desc'] if goods_detail['goods_desc'] is not None else ''
    goods.goods_front_image = goods_detail['images'][0] if goods_detail['images'] is not None else ''

    category_name = goods_detail['categorys'][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    for good_image in goods_detail['images']:
        good_image_instance = GoodsImage()
        good_image_instance.goods = goods
        good_image_instance.image = good_image
        good_image_instance.save()
