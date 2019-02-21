from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile,EmailVerifyRecord
from .forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from utils.email_send import send_register_email


class CustomBanckend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user =UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form':login_form})


class ActiveUserView(View):
    '''注册验证'''
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class RegisterView(View):
    '''注册界面'''
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form':register_form,'msg': '用户已经存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name,'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html',{'register_form':register_form})


class ForgetPwdView(View):
    '''忘记密码页面'''
    def get(self,request):
        forget_form = ForgetForm()
        return render(request,'forgetpwd.html',{'forget_form':forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            passwd = request.POST.get('password', '')
            user = authenticate(username=email, password=passwd)
            if user is not None:
                send_register_email(email, 'forget')
                return render(request, 'forgetpwd.html',{'forget_form': forget_form,'msg':'链接已发送，请注意查收！'})
            else:
                return render(request, 'forgetpwd.html',{'forget_form': forget_form,'msg':'邮箱或密码错误'})
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    '''重置密码get请求'''
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                return render(request, 'password_reset.html',{'email':email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    '''重置密码form表单提交'''
    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1','')
            pwd2 = request.POST.get('password2','')
            email = request.POST.get('email','')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email,'msg':'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email':email,'modify_form':modify_form})
