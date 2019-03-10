__author__ = 'xiao tang'
__date__ = '2019/1/26 16:08'

import xadmin

from .models import Course
from .models import Lesson
from .models import Video
from .models import CourseResource
from organization.models import CourseOrg


class LessonInline():
    model = Lesson
    extra = 0


class CourseResourceInline():
    model = CourseResource
    extra = 0


class CourseAdmin():
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time','get_zj_nums','go_to']
    search_fields = ['name','desc','detail','degree','students','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [LessonInline,CourseResourceInline]
    style_fields = {'detail':'ueditor'}
    list_editable = ['degree','desc']       # 在列表页直接修改数据
    refresh_times = [3,5]       # xadmin定时刷新
    import_excel = True

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            # students = obj.students
            course_org.courses = Course.objects.filter(course_org=course_org).count()
            # course_org.students = Course.objects.filter(students=students).count()
            course_org.save()
#
#     def queryset(self):
#         qs = super(CourseAdmin,self).queryset()
#         qs.filter(is_banner = True)
#         return qs
#
#
# class BannerCourseAdmin():
#     list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums'
#     ,'add_time']
#     search_fields = ['name','desc','detail','degree','students','fav_nums','image','click_nums']
#     list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums',
#     'add_time']
#     ordering = ['-click_nums']
#     readonly_fields = ['click_nums']
#     exclude = ['fav_nums']
#     inlines = [LessonInline,CourseResourceInline]
#
#     def queryset(self):
#         qs = super(BannerCourseAdmin,self).queryset()
#         qs.filter(is_banner = True)
#         return qs


class LessonAdmin():
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']


class VideoAdmin():
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']


class CourseResourceAdmin():
    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']


xadmin.site.register(Course,CourseAdmin)
# xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
