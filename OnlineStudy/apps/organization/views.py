from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import CourseOrg,CityDict
from .forms import UserAskForm

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
