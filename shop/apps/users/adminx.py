__author__ = 'xiao tang'
__date__ = '2019/1/26 15:34'

import xadmin
from xadmin import views

from .models import VerifyCode


class BaseSetting():
    enable_themes = True        # 主题功能
    use_bootswatch = True


class GlobalSetting():
    site_title = '猪头电商管理系统'
    site_footer = '胖胖的网站'
    menu_style = 'accordion'


class VerifyCodeAdmin():
    list_display = ['code', 'mobile', 'add_time']
    search_fields = ['code', 'mobile']
    list_filter = ['code', 'mobile', 'add_time']
    # model_icon = 'fa fa-group'


xadmin.site.register(VerifyCode,VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
