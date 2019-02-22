from django.urls import path,include,re_path
from organization.views import OrgView,AddUserAskView

app_name = '[organization]'
urlpatterns = [
    # 机构列表
    path(r'list/',OrgView.as_view(),name='org_list'),
    path(r'add_ask/',AddUserAskView.as_view(),name='add_ask'),
]