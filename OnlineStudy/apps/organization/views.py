from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import CourseOrg,CityDict
from .forms import UserAskForm
from operation.models import UserFavorite
from course.models import Course

# Create your views here.
from pure_pagination import Paginator, PageNotAnInteger


class OrgView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        all_citys = CityDict.objects.all()
        city_id = request.GET.get('city','')

        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        categroy = request.GET.get('ct','')
        if categroy:
            all_orgs = all_orgs.filter(categroy=categroy)

        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-courses')

        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs,2, request=request)

        orgs = p.page(page)
        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'categroy':categroy,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })


class AddUserAskView(View):
    '''用户添加咨询'''
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        else:
            return HttpResponse(
                '{"status":"fail", "msg":"您的字段有错误,请检查"}',
                content_type='application/json')


class OrgHomeView(View):
    '''机构首页'''
    def get(self,request,org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teacher':all_teacher,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav':has_fav,
        })


class OrgCourseView(View):
    '''机构课程列表页'''
    def get(self,request,org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()
        return render(request,'org-detail-course.html',{
            'all_courses':all_courses,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav': has_fav,
        })


class OrgDescView(View):
    '''机构介绍页'''
    def get(self,request,org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav = True
        return render(request,'org-detail-desc.html',{
            'course_org':course_org,
            'current_page':current_page,
            'has_fav': has_fav,
        })


class OrgTeacherView(View):
    '''机构教师页'''
    def get(self,request,org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_teachers = course_org.teacher_set.all()
        return render(request,'org-detail-teachers.html',{
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav': has_fav,
        })


class AddFavView(View):
    '''用户收藏'''
    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type','')
        if not request.user.is_authenticated:
            return HttpResponse(
                '{"status":"fail", "msg":"用户未登陆!"}',
                content_type='application/json')
        exist_record = UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))
        if exist_record:
            # 如果记录已经存在，则表示用户取消收藏
            exist_record.delete()
            return HttpResponse(
                '{"status":"success", "msg":"收藏!"}',
                content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse(
                    '{"status":"success", "msg":"已收藏!"}',
                    content_type='application/json')
            else:
                return HttpResponse(
                    '{"status":"fail", "msg":"收藏出错!"}',
                    content_type='application/json')
