from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_default_login
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .form import *
from .models import *
from config_busi.models import *
from appcenter.models import *
from sys_user.func import *

# Create your views here.

"""

登录
注册
修改密码
默认注册为系统用户
模块管理员

"""


def register(request):
    if request.method == "GET":
        context = dict()
        context["registerform"] = RegisterForm()
        context["error_message"] = ""
        return HttpResponse(
            loader.get_template(f"register.html").render(context, request)
        )
    obj = mydict(request.POST)
    registerform = RegisterForm(request.POST)
    if not registerform.is_valid():
        return render(request, "login.html", locals())
    username = registerform.cleaned_data.get("username")
    password1 = registerform.cleaned_data.get("password1")
    password2 = registerform.cleaned_data.get("password2")

    user = User.objects.filter(username=username)
    if user:
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "用户名已存在"},
        )
    if password1 != password2:
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "密码不一致"},
        )
    user_table_id = obj.get("user_table_id")
    table_user_ins = None

    # 用户表

    if str(8094) == user_table_id:
        table_user_ins = mc_users
    # 系统管理员

    if str(8127) == user_table_id:
        table_user_ins = mc_supermanager
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
    my_user = table_user_ins.objects.filter(username=username)
    if my_user:
        print("该用户已经注册")
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "用户名已存在"},
        )
    # save

    my_user = table_user_ins(username=username)
    my_user.save()

    user = User.objects.create_user(
        username=username,
        password=password1,
        email=registerform.cleaned_data.get("email"),
        is_superuser=True,
    )

    user.set_password(password1)
    user.save()
    return redirect("/")


def logout_view(request):
    logout(request)

    response = redirect("/")
    response.delete_cookie("username")
    response.delete_cookie("user_table_id")
    return response


def admin_logout_view(request):
    logout(request)
    response = redirect("/admin")
    response.delete_cookie("username")
    return response


def login_view(request):
    if request.method == "GET":
        context = dict()
        print("in login.html")
        context["loginform"] = LoginForm()

        # response = HttpResponse(loader.get_template('login_v6.html').render(context, request))

        response = HttpResponse(
            loader.get_template("login.html").render(context, request)
        )
        response.delete_cookie("user_table_id")
        return response
    # post

    obj = mydict(request.POST)
    loginform = LoginForm(request.POST)
    # print(loginform)

    if not loginform.is_valid():
        response = render(request, "login.html", locals())
        response.delete_cookie("user_table_id")
        return response
    username = loginform.cleaned_data.get("username")
    password = loginform.cleaned_data.get("password")
    # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。

    user = authenticate(request, username=username, password=password)

    user_table_id = obj.get("user_table_id")
    table_user_ins = None

    # 用户表

    if str(8094) == user_table_id:
        table_user_ins = mc_users
        page = "users"
    # 系统管理员

    if str(8127) == user_table_id:
        table_user_ins = mc_supermanager
        page = "supermanager"
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
        error_message = "登录信息失效"
        return redirect("/", locals())
    my_user = table_user_ins.objects.filter(username=username)
    if len(my_user) == 0:
        print("登录失败")
        error_message = "登录信息失效"
        return redirect("/", locals())
    # 验证如果用户不为空

    if user is None:
        # 强制注册功能
        # 返回登录失败信息
        # error_message = 'login faild'
        # response = render(request, 'login.html', locals())
        # response.delete_cookie('user_table_id')
        # return response
        # 默认即注册:

        # save

        my_user = table_user_ins(username=username)
        my_user.save()
        user = User.objects.create_user(
            username=username,
            password=password,
            email="",
            is_superuser=True,
        )

        user.set_password(password)
        user.save()
    # login方法登录

    django_default_login(request, user)
    print("login success")
    response = HttpResponseRedirect("/index", locals())
    response.set_cookie("user_table_id", user_table_id)
    return response


def usercenter(request):
    if request.method == "GET":
        context = dict()
        context["usercenterform"] = UserCenterForm()
        context["error_message"] = ""
    return render(request, "config_user/index.html", locals())


def index(request):

    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    username = request.user.username

    table_user_ins = None

    # 用户表

    if str(8094) == user_table_id:
        table_user_ins = mc_users
        page = "users"
    # 系统管理员

    if str(8127) == user_table_id:
        table_user_ins = mc_supermanager
        page = "supermanager"
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
        error_message = "登录信息失效"
        return redirect("/", locals())
    my_user = table_user_ins.objects.filter(username=username)
    if len(my_user) == 0:
        print("登录失败")
        error_message = "登录信息失效"
        return redirect("/", locals())
    if request.method == "GET":
        # 主页默认配置信息

        """若需控制访问权限，可在此处加上判断条件，如：
            if not request.user.is_superuser:
                return render(request, 'index.html', locals())

            # 判断表内容对于当前用户的权限:
                1. 若是管理员，则显示所有项目
                2. 若是普通用户，则显示当前用户所属内容

        Returns:
            response: 请求处理
        """

        tab_mc_users = {
            "params": mc_users().toParams_zh(),
            "records": mc_users.objects.all()[::-1],
            "json": [m.toJson() for m in mc_users.objects.all()[::-1]],
        }

        tab_mc_roles = {
            "params": mc_roles().toParams_zh(),
            "records": mc_roles.objects.all()[::-1],
            "json": [m.toJson() for m in mc_roles.objects.all()[::-1]],
        }

        tab_mc_userrolerelations = {
            "params": mc_userrolerelations().toParams_zh(),
            "records": mc_userrolerelations.objects.all()[::-1],
            "json": [m.toJson() for m in mc_userrolerelations.objects.all()[::-1]],
        }

        tab_mc_weeklyrepkwkworttemplates = {
            "params": mc_weeklyrepkwkworttemplates().toParams_zh(),
            "records": mc_weeklyrepkwkworttemplates.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_weeklyrepkwkworttemplates.objects.all()[::-1]
            ],
        }

        tab_mc_weeklyrepkwkworts = {
            "params": mc_weeklyrepkwkworts().toParams_zh(),
            "records": mc_weeklyrepkwkworts.objects.all()[::-1],
            "json": [m.toJson() for m in mc_weeklyrepkwkworts.objects.all()[::-1]],
        }

        tab_mc_repkwkwortperiods = {
            "params": mc_repkwkwortperiods().toParams_zh(),
            "records": mc_repkwkwortperiods.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortperiods.objects.all()[::-1]],
        }

        tab_mc_repkwkwortstatuses = {
            "params": mc_repkwkwortstatuses().toParams_zh(),
            "records": mc_repkwkwortstatuses.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortstatuses.objects.all()[::-1]],
        }

        tab_mc_repkwkworttypes = {
            "params": mc_repkwkworttypes().toParams_zh(),
            "records": mc_repkwkworttypes.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkworttypes.objects.all()[::-1]],
        }

        tab_mc_repkwkwortaudits = {
            "params": mc_repkwkwortaudits().toParams_zh(),
            "records": mc_repkwkwortaudits.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortaudits.objects.all()[::-1]],
        }

        tab_mc_auditcomments = {
            "params": mc_auditcomments().toParams_zh(),
            "records": mc_auditcomments.objects.all()[::-1],
            "json": [m.toJson() for m in mc_auditcomments.objects.all()[::-1]],
        }

        tab_mc_departments = {
            "params": mc_departments().toParams_zh(),
            "records": mc_departments.objects.all()[::-1],
            "json": [m.toJson() for m in mc_departments.objects.all()[::-1]],
        }

        tab_mc_employees = {
            "params": mc_employees().toParams_zh(),
            "records": mc_employees.objects.all()[::-1],
            "json": [m.toJson() for m in mc_employees.objects.all()[::-1]],
        }

        tab_mc_employeeweeklyrepkwkwortrelations = {
            "params": mc_employeeweeklyrepkwkwortrelations().toParams_zh(),
            "records": mc_employeeweeklyrepkwkwortrelations.objects.all()[::-1],
            "json": [
                m.toJson()
                for m in mc_employeeweeklyrepkwkwortrelations.objects.all()[::-1]
            ],
        }

        tab_mc_notkwkwifications = {
            "params": mc_notkwkwifications().toParams_zh(),
            "records": mc_notkwkwifications.objects.all()[::-1],
            "json": [m.toJson() for m in mc_notkwkwifications.objects.all()[::-1]],
        }

        tab_mc_notkwkwificationtypes = {
            "params": mc_notkwkwificationtypes().toParams_zh(),
            "records": mc_notkwkwificationtypes.objects.all()[::-1],
            "json": [m.toJson() for m in mc_notkwkwificationtypes.objects.all()[::-1]],
        }

        tab_mc_emaillogs = {
            "params": mc_emaillogs().toParams_zh(),
            "records": mc_emaillogs.objects.all()[::-1],
            "json": [m.toJson() for m in mc_emaillogs.objects.all()[::-1]],
        }

        tab_mc_smslogs = {
            "params": mc_smslogs().toParams_zh(),
            "records": mc_smslogs.objects.all()[::-1],
            "json": [m.toJson() for m in mc_smslogs.objects.all()[::-1]],
        }

        tab_mc_attachments = {
            "params": mc_attachments().toParams_zh(),
            "records": mc_attachments.objects.all()[::-1],
            "json": [m.toJson() for m in mc_attachments.objects.all()[::-1]],
        }

        tab_mc_attachmenttypes = {
            "params": mc_attachmenttypes().toParams_zh(),
            "records": mc_attachmenttypes.objects.all()[::-1],
            "json": [m.toJson() for m in mc_attachmenttypes.objects.all()[::-1]],
        }

        tab_mc_repkwkwortsubmkwkwissionhkwkwistkwkwories = {
            "params": mc_repkwkwortsubmkwkwissionhkwkwistkwkwories().toParams_zh(),
            "records": mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.all()[::-1],
            "json": [
                m.toJson()
                for m in mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.all()[
                    ::-1
                ]
            ],
        }

        tab_mc_repkwkwortmodkwkwificationhkwkwistkwkwories = {
            "params": mc_repkwkwortmodkwkwificationhkwkwistkwkwories().toParams_zh(),
            "records": mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.all()[
                ::-1
            ],
            "json": [
                m.toJson()
                for m in mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.all()[
                    ::-1
                ]
            ],
        }

        tab_mc_repkwkwortcomments = {
            "params": mc_repkwkwortcomments().toParams_zh(),
            "records": mc_repkwkwortcomments.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortcomments.objects.all()[::-1]],
        }

        tab_mc_commentreplies = {
            "params": mc_commentreplies().toParams_zh(),
            "records": mc_commentreplies.objects.all()[::-1],
            "json": [m.toJson() for m in mc_commentreplies.objects.all()[::-1]],
        }

        tab_mc_repkwkwortratkwkwings = {
            "params": mc_repkwkwortratkwkwings().toParams_zh(),
            "records": mc_repkwkwortratkwkwings.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortratkwkwings.objects.all()[::-1]],
        }

        tab_mc_ratkwkwingcriteria = {
            "params": mc_ratkwkwingcriteria().toParams_zh(),
            "records": mc_ratkwkwingcriteria.objects.all()[::-1],
            "json": [m.toJson() for m in mc_ratkwkwingcriteria.objects.all()[::-1]],
        }

        tab_mc_permkwkwissions = {
            "params": mc_permkwkwissions().toParams_zh(),
            "records": mc_permkwkwissions.objects.all()[::-1],
            "json": [m.toJson() for m in mc_permkwkwissions.objects.all()[::-1]],
        }

        tab_mc_permkwkwissionrolerelations = {
            "params": mc_permkwkwissionrolerelations().toParams_zh(),
            "records": mc_permkwkwissionrolerelations.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_permkwkwissionrolerelations.objects.all()[::-1]
            ],
        }

        tab_mc_systemlogs = {
            "params": mc_systemlogs().toParams_zh(),
            "records": mc_systemlogs.objects.all()[::-1],
            "json": [m.toJson() for m in mc_systemlogs.objects.all()[::-1]],
        }

        tab_mc_repkwkwortconfigurations = {
            "params": mc_repkwkwortconfigurations().toParams_zh(),
            "records": mc_repkwkwortconfigurations.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_repkwkwortconfigurations.objects.all()[::-1]
            ],
        }

        tab_mc_repkwkwortexpkwkwortreckwkwords = {
            "params": mc_repkwkwortexpkwkwortreckwkwords().toParams_zh(),
            "records": mc_repkwkwortexpkwkwortreckwkwords.objects.all()[::-1],
            "json": [
                m.toJson()
                for m in mc_repkwkwortexpkwkwortreckwkwords.objects.all()[::-1]
            ],
        }

        tab_mc_repkwkworttemplatefields = {
            "params": mc_repkwkworttemplatefields().toParams_zh(),
            "records": mc_repkwkworttemplatefields.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_repkwkworttemplatefields.objects.all()[::-1]
            ],
        }

        tab_mc_repkwkwortfieldtypes = {
            "params": mc_repkwkwortfieldtypes().toParams_zh(),
            "records": mc_repkwkwortfieldtypes.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortfieldtypes.objects.all()[::-1]],
        }

        tab_mc_repkwkwortdata = {
            "params": mc_repkwkwortdata().toParams_zh(),
            "records": mc_repkwkwortdata.objects.all()[::-1],
            "json": [m.toJson() for m in mc_repkwkwortdata.objects.all()[::-1]],
        }

        tab_mc_supermanager = {
            "params": mc_supermanager().toParams_zh(),
            "records": mc_supermanager.objects.all()[::-1],
            "json": [m.toJson() for m in mc_supermanager.objects.all()[::-1]],
        }
    __version__ = settings.GLOBAL_VERSION

    if request.method == "GET":

        # 配置不同用户访问的主页不同
        # return render(request, f'index_{page}.html', locals())

        return render(request, f"index{__version__}.html", locals())
    # 处理post请求，一般不建议在这里添加多余功能。

    return render(request, f"index{__version__}.html", locals())
