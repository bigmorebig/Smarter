"""OnlineStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
import xadmin
from django.views.generic import TemplateView
from django.views.static import serve

from users.views import LoginView,LogoutView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView,IndexView
from OnlineStudy.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # path('index/',IndexView.as_view(),name='index'),
    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path(r'captcha/', include('captcha.urls')),
    re_path(r'active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path(r'forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path(r'reset/(?P<active_code>.*)/',ResetView.as_view(),name='reset_pwd'),
    path(r'modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),

    # 课程机构url配置
    path(r'org/', include('organization.urls',namespace='org')),

    # 配置上传文件的访问处理函数
    re_path(r'media/(?P<path>.*)',serve,{'document_root':MEDIA_ROOT}),

    # re_path(r'static/(?P<path>.*)',serve,{'document_root':STATIC_ROOT}),
    # 课程url配置
    path(r'course/', include('course.urls',namespace='course')),

    # 个人中心url配置
    path(r'users/', include('users.urls',namespace='users')),
    path('logout/',LogoutView.as_view(),name='logout'),
    path(r'ueditor/',include('DjangoUeditor.urls' )),
]

# 全局404页面配置
handler404 = 'users.views.pag_not_found'
# 全局500页面配置
handler500 = 'users.views.pag_error'