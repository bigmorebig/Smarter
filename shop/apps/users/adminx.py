__author__ = 'xiao tang'
__date__ = '2019/1/26 15:34'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banner


class BaseSetting():
    enable_themes = True        # 主题功能
    use_bootswatch = True


class GlobalSetting():
    site_title = '胖胖后台管理系统'
    site_footer = '胖胖的网站'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin():
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']
    # model_icon = 'fa fa-group'


class BannerAdmin():
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
