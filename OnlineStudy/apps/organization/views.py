from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from .models import CourseOrg,CityDict
# Create your views here.
from pure_pagination import Paginator, PageNotAnInteger


class OrgView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_citys = CityDict.objects.all()
        city_id = request.GET.get('city','')

        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

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
        })
