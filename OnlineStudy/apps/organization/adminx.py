__author__ = 'xiao tang'
__date__ = '2019/1/26 17:00'

import xadmin

from .models import CityDict
from .models import CourseOrg
from .models import Teacher


class CityDictAdmin():
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc','add_time']


class CourseOrgAdmin():
    list_display = ['name','desc','click_uum','fav_num','image','address','city','add_time']
    search_fields = ['name','desc','click_uum','fav_num','image','address','city']
    list_filter = ['name','desc','click_uum','fav_num','image','address','city','add_time']


class TeacherAdmin():
    list_display = ['org','name','work_years','work_company','work_position','point','click_num','fav_num','add_time']
    search_fields = ['org','name','work_years','work_company','work_position','point','click_num','fav_num']
    list_filter = ['org','name','work_years','work_company','work_position','point','click_num','fav_num','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)