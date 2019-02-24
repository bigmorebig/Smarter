__author__ = 'xiao tang'
__date__ = '2019/2/23 20:57'
from django.urls import path,include,re_path
from .views import CourseListView,CourseDetailView,CourseInfoView,CourseCommentView,AddCommentView,VideoPlayView


app_name = '[course]'
urlpatterns = [
    path(r'list/',CourseListView.as_view(),name='course_list'),
    re_path(r'detail/(?P<course_id>\d+)/',CourseDetailView.as_view(),name='course_detail'),
    # 课程详情页
    re_path(r'info/(?P<course_id>\d+)/',CourseInfoView.as_view(),name='course_info'),
    # 课程评论页面
    re_path(r'comment/(?P<course_id>\d+)/',CourseCommentView.as_view(),name='course_comment'),
    # 添加评论
    path(r'add_comment/',AddCommentView.as_view(),name='add_comment'),
    re_path(r'video/(?P<video_id>\d+)/',VideoPlayView.as_view(),name='video_play'),
]