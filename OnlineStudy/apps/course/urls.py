__author__ = 'xiao tang'
__date__ = '2019/2/23 20:57'
from django.urls import path,include,re_path
from .views import CourseListView


app_name = '[organization]'
urlpatterns = [
    path(r'list/',CourseListView.as_view(),name='org_list'),
]