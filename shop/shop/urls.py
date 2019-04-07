"""shop URL Configuration

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
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
import xadmin
from shop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewSet


router = DefaultRouter()
# 配置goods的URL
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 配置category的URL
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'codes', SmsCodeViewSet, base_name='codes')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    re_path(r'media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='唐潇唐接口文档')),
    # drf自带的token认证模式
    path(r'api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    path('login/', obtain_jwt_token),
]
