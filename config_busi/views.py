from datetime import datetime
import os
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from appcenter.models import *
from sys_user.func import *


def resp(res, msg, url=None, **kwargs):
    return {"res": res, "msg": msg, "url": url, **kwargs}


# Create your views here.


def index(request):
    records = [
        {
            "id": 1,
        },
        {"id": 2},
    ]
    return render(request, "config_visual/index.html", locals())


@login_required
def view_users(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户邮箱

        mcauthfield_useremail = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户密码

        mcauthfield_userpkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户角色

        mcauthfield_userrole = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录日期

        mcauthfield_lkwkwastlogkwkwindate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否活跃

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID关联字段

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户邮箱

        mcauthfield_useremail = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户密码

        mcauthfield_userpkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户角色

        mcauthfield_userrole = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录日期

        mcauthfield_lkwkwastlogkwkwindate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否活跃

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID关联字段

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_users.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_users().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_users.objects.filter(**filter)
        else:
            records = mc_users.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_departments_55242 = []
        for m in mc_departments.objects.all():
            mobj = m.toJson()
            data_mc_departments_55242.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("departmentname"),
                }
            )
        return render(request, "config_busi/users.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_users()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 用户邮箱

        if mcauthfield_useremail["mcauthchange"]:

            # EmailField # 其他情况/待补充

            ins_table_busi.useremail = obj.get("useremail")
        # 用户密码

        if mcauthfield_userpkwkwasswkwkword["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.userpkwkwasswkwkword = obj.get("userpkwkwasswkwkword")
        # 用户角色

        if mcauthfield_userrole["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.userrole = obj.get("userrole")
        # 创建日期

        if mcauthfield_createdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.createdate = obj.get("createdate")
        # 最后登录日期

        if mcauthfield_lkwkwastlogkwkwindate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastlogkwkwindate = obj.get("lkwkwastlogkwkwindate")
        # 是否活跃

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID关联字段

        if mcauthfield_departmentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.departmentid = obj.get("departmentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 用户邮箱

        if mcauthfield_useremail["mcauthchange"]:

            # EmailField

            ins_table_busi.useremail = obj.get("useremail")
        # 用户密码

        if mcauthfield_userpkwkwasswkwkword["mcauthchange"]:

            # CharField

            ins_table_busi.userpkwkwasswkwkword = obj.get("userpkwkwasswkwkword")
        # 用户角色

        if mcauthfield_userrole["mcauthchange"]:

            # CharField

            ins_table_busi.userrole = obj.get("userrole")
        # 创建日期

        if mcauthfield_createdate["mcauthchange"]:

            # DateField

            ins_table_busi.createdate = obj.get("createdate")
        # 最后登录日期

        if mcauthfield_lkwkwastlogkwkwindate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastlogkwkwindate = obj.get("lkwkwastlogkwkwindate")
        # 是否活跃

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID关联字段

        if mcauthfield_departmentid["mcauthchange"]:

            # SelectField

            ins_table_busi.departmentid = obj.get("departmentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/users")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_roles(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 角色表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色描述

        mcauthfield_roledescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID关联字段指向部门的ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 角色表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色描述

        mcauthfield_roledescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID关联字段指向部门的ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_roles.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_roles().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_roles.objects.filter(**filter)
        else:
            records = mc_roles.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_departments_55251 = []
        for m in mc_departments.objects.all():
            mobj = m.toJson()
            data_mc_departments_55251.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("departmentname"),
                }
            )
        return render(request, "config_busi/roles.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_roles()

        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.roleid = str(uuid.uuid4())
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rolename = obj.get("rolename")
        # 角色描述

        if mcauthfield_roledescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.roledescription = obj.get("roledescription")
        # 创建时间

        if mcauthfield_createdtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdtime = obj.get("createdtime")
        # 创建者ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.createdby = str(uuid.uuid4())
        # 更新时间

        if mcauthfield_updatedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedtime = obj.get("updatedtime")
        # 更新者ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.updatedby = str(uuid.uuid4())
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID关联字段指向部门的ID

        if mcauthfield_departmentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.departmentid = obj.get("departmentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_roles.objects.get(id=obj.get("_id_upd"))

        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.roleid = str(uuid.uuid4())

            ins_table_busi.roleid = str(ins_table_busi.roleid)
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField

            ins_table_busi.rolename = obj.get("rolename")
        # 角色描述

        if mcauthfield_roledescription["mcauthchange"]:

            # TextField

            ins_table_busi.roledescription = obj.get("roledescription")
        # 创建时间

        if mcauthfield_createdtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdtime = obj.get("createdtime")
        # 创建者ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.createdby = str(uuid.uuid4())

            ins_table_busi.createdby = str(ins_table_busi.createdby)
        # 更新时间

        if mcauthfield_updatedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedtime = obj.get("updatedtime")
        # 更新者ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.updatedby = str(uuid.uuid4())

            ins_table_busi.updatedby = str(ins_table_busi.updatedby)
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID关联字段指向部门的ID

        if mcauthfield_departmentid["mcauthchange"]:

            # SelectField

            ins_table_busi.departmentid = obj.get("departmentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_roles.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_roles.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/roles")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userrolerelations(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户角色关联表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于标记该关联是否有效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者ID

        mcauthfield_lkwkwastmodkwkwifierid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户角色关联表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于标记该关联是否有效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者ID

        mcauthfield_lkwkwastmodkwkwifierid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userrolerelations.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userrolerelations().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userrolerelations.objects.filter(**filter)
        else:
            records = mc_userrolerelations.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userrolerelations_55256 = []
        for m in mc_userrolerelations.objects.all():
            mobj = m.toJson()
            data_mc_userrolerelations_55256.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("kwkwisactive"),
                }
            )
        return render(request, "config_busi/userrolerelations.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userrolerelations()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.roleid = str(uuid.uuid4())
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于标记该关联是否有效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.creatkwkworid = str(uuid.uuid4())
        # 最后修改者ID

        if mcauthfield_lkwkwastmodkwkwifierid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.lkwkwastmodkwkwifierid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userrolerelations.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.roleid = str(uuid.uuid4())

            ins_table_busi.roleid = str(ins_table_busi.roleid)
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于标记该关联是否有效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # SelectField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.creatkwkworid = str(uuid.uuid4())

            ins_table_busi.creatkwkworid = str(ins_table_busi.creatkwkworid)
        # 最后修改者ID

        if mcauthfield_lkwkwastmodkwkwifierid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.lkwkwastmodkwkwifierid = str(uuid.uuid4())

            ins_table_busi.lkwkwastmodkwkwifierid = str(
                ins_table_busi.lkwkwastmodkwkwifierid
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userrolerelations.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userrolerelations.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userrolerelations")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_weeklyrepkwkworttemplates(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 周报模板表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板名称

        mcauthfield_templatename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者

        mcauthfield_lkwkwastmodkwkwifier = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改日期

        mcauthfield_lkwkwastmodkwkwificationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 周报模板表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板名称

        mcauthfield_templatename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者

        mcauthfield_lkwkwastmodkwkwifier = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改日期

        mcauthfield_lkwkwastmodkwkwificationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_weeklyrepkwkworttemplates.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_weeklyrepkwkworttemplates().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_weeklyrepkwkworttemplates.objects.filter(**filter)
        else:
            records = mc_weeklyrepkwkworttemplates.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/weeklyrepkwkworttemplates.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_weeklyrepkwkworttemplates()

        # 模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.templateid = str(uuid.uuid4())
        # 模板名称

        if mcauthfield_templatename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.templatename = obj.get("templatename")
        # 模板描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.creationdate = obj.get("creationdate")
        # 最后修改者

        if mcauthfield_lkwkwastmodkwkwifier["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifier = obj.get("lkwkwastmodkwkwifier")
        # 最后修改日期

        if mcauthfield_lkwkwastmodkwkwificationdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwificationdate = obj.get(
                "lkwkwastmodkwkwificationdate"
            )
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_weeklyrepkwkworttemplates.objects.get(id=obj.get("_id_upd"))

        # 模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.templateid = str(uuid.uuid4())

            ins_table_busi.templateid = str(ins_table_busi.templateid)
        # 模板名称

        if mcauthfield_templatename["mcauthchange"]:

            # CharField

            ins_table_busi.templatename = obj.get("templatename")
        # 模板描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField

            ins_table_busi.creationdate = obj.get("creationdate")
        # 最后修改者

        if mcauthfield_lkwkwastmodkwkwifier["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwastmodkwkwifier = obj.get("lkwkwastmodkwkwifier")
        # 最后修改日期

        if mcauthfield_lkwkwastmodkwkwificationdate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmodkwkwificationdate = obj.get(
                "lkwkwastmodkwkwificationdate"
            )
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_weeklyrepkwkworttemplates.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_weeklyrepkwkworttemplates.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/weeklyrepkwkworttemplates")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_weeklyrepkwkworts(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 周报表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周开始日期

        mcauthfield_weekstartdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周结束日期

        mcauthfield_weekenddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门

        mcauthfield_department = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工姓名

        mcauthfield_employeename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告内容

        mcauthfield_repkwkwortcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 周报表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周开始日期

        mcauthfield_weekstartdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周结束日期

        mcauthfield_weekenddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门

        mcauthfield_department = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工姓名

        mcauthfield_employeename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告内容

        mcauthfield_repkwkwortcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_weeklyrepkwkworts.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_weeklyrepkwkworts().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_weeklyrepkwkworts.objects.filter(**filter)
        else:
            records = mc_weeklyrepkwkworts.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/weeklyrepkwkworts.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_weeklyrepkwkworts()

        # 报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 周开始日期

        if mcauthfield_weekstartdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.weekstartdate = obj.get("weekstartdate")
        # 周结束日期

        if mcauthfield_weekenddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.weekenddate = obj.get("weekenddate")
        # 部门

        if mcauthfield_department["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.department = obj.get("department")
        # 员工姓名

        if mcauthfield_employeename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.employeename = obj.get("employeename")
        # 报告内容

        if mcauthfield_repkwkwortcontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.repkwkwortcontent = obj.get("repkwkwortcontent")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_weeklyrepkwkworts.objects.get(id=obj.get("_id_upd"))

        # 报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 周开始日期

        if mcauthfield_weekstartdate["mcauthchange"]:

            # DateField

            ins_table_busi.weekstartdate = obj.get("weekstartdate")
        # 周结束日期

        if mcauthfield_weekenddate["mcauthchange"]:

            # DateField

            ins_table_busi.weekenddate = obj.get("weekenddate")
        # 部门

        if mcauthfield_department["mcauthchange"]:

            # CharField

            ins_table_busi.department = obj.get("department")
        # 员工姓名

        if mcauthfield_employeename["mcauthchange"]:

            # CharField

            ins_table_busi.employeename = obj.get("employeename")
        # 报告内容

        if mcauthfield_repkwkwortcontent["mcauthchange"]:

            # TextField

            ins_table_busi.repkwkwortcontent = obj.get("repkwkwortcontent")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_weeklyrepkwkworts.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_weeklyrepkwkworts.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/weeklyrepkwkworts")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortperiods(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告周期表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告周期ID

        mcauthfield_repkwkwortperiodid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周期名称

        mcauthfield_periodname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始日期

        mcauthfield_startdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束日期

        mcauthfield_enddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否活跃用于标记当前周期是否还在使用中

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者记录创建该周期的用户

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者记录最后修改该周期的用户

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改日期

        mcauthfield_lkwkwastmodkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告周期表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告周期ID

        mcauthfield_repkwkwortperiodid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周期名称

        mcauthfield_periodname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始日期

        mcauthfield_startdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束日期

        mcauthfield_enddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否活跃用于标记当前周期是否还在使用中

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者记录创建该周期的用户

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者记录最后修改该周期的用户

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改日期

        mcauthfield_lkwkwastmodkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortperiods.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortperiods().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortperiods.objects.filter(**filter)
        else:
            records = mc_repkwkwortperiods.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/repkwkwortperiods.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortperiods()

        # 报告周期ID

        if mcauthfield_repkwkwortperiodid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortperiodid = str(uuid.uuid4())
        # 周期名称

        if mcauthfield_periodname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.periodname = obj.get("periodname")
        # 开始日期

        if mcauthfield_startdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.startdate = obj.get("startdate")
        # 结束日期

        if mcauthfield_enddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.enddate = obj.get("enddate")
        # 是否活跃用于标记当前周期是否还在使用中

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者记录创建该周期的用户

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.creationdate = obj.get("creationdate")
        # 最后修改者记录最后修改该周期的用户

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 最后修改日期

        if mcauthfield_lkwkwastmodkwkwifieddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifieddate = obj.get(
                "lkwkwastmodkwkwifieddate"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortperiods.objects.get(id=obj.get("_id_upd"))

        # 报告周期ID

        if mcauthfield_repkwkwortperiodid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortperiodid = str(uuid.uuid4())

            ins_table_busi.repkwkwortperiodid = str(ins_table_busi.repkwkwortperiodid)
        # 周期名称

        if mcauthfield_periodname["mcauthchange"]:

            # CharField

            ins_table_busi.periodname = obj.get("periodname")
        # 开始日期

        if mcauthfield_startdate["mcauthchange"]:

            # DateField

            ins_table_busi.startdate = obj.get("startdate")
        # 结束日期

        if mcauthfield_enddate["mcauthchange"]:

            # DateField

            ins_table_busi.enddate = obj.get("enddate")
        # 是否活跃用于标记当前周期是否还在使用中

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者记录创建该周期的用户

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField

            ins_table_busi.creationdate = obj.get("creationdate")
        # 最后修改者记录最后修改该周期的用户

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 最后修改日期

        if mcauthfield_lkwkwastmodkwkwifieddate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmodkwkwifieddate = obj.get(
                "lkwkwastmodkwkwifieddate"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortperiods.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortperiods.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortperiods")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortstatuses(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告状态表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告状态ID

        mcauthfield_repkwkwortstatusid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态名称

        mcauthfield_statusname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为默认状态

        mcauthfield_isdefault = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联报告ID指向报告的ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告状态表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告状态ID

        mcauthfield_repkwkwortstatusid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态名称

        mcauthfield_statusname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为默认状态

        mcauthfield_isdefault = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联报告ID指向报告的ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortstatuses.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortstatuses().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortstatuses.objects.filter(**filter)
        else:
            records = mc_repkwkwortstatuses.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_weeklyrepkwkworts_55294 = []
        for m in mc_weeklyrepkwkworts.objects.all():
            mobj = m.toJson()
            data_mc_weeklyrepkwkworts_55294.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortcontent"),
                }
            )
        return render(request, "config_busi/repkwkwortstatuses.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortstatuses()

        # 报告状态ID

        if mcauthfield_repkwkwortstatusid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortstatusid = str(uuid.uuid4())
        # 状态名称

        if mcauthfield_statusname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.statusname = obj.get("statusname")
        # 状态描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 是否为默认状态

        if mcauthfield_isdefault["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isdefault = obj.get("isdefault")
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        # 关联报告ID指向报告的ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortstatuses.objects.get(id=obj.get("_id_upd"))

        # 报告状态ID

        if mcauthfield_repkwkwortstatusid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortstatusid = str(uuid.uuid4())

            ins_table_busi.repkwkwortstatusid = str(ins_table_busi.repkwkwortstatusid)
        # 状态名称

        if mcauthfield_statusname["mcauthchange"]:

            # CharField

            ins_table_busi.statusname = obj.get("statusname")
        # 状态描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 是否为默认状态

        if mcauthfield_isdefault["mcauthchange"]:

            # BooleanField

            ins_table_busi.isdefault = obj.get("isdefault")
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        # 关联报告ID指向报告的ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortstatuses.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortstatuses.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortstatuses")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkworttypes(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告类型表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告类型ID

        mcauthfield_repkwkworttypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告类型名称

        mcauthfield_repkwkworttypename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制该报告类型是否可用

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改日期

        mcauthfield_modkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改者ID关联用户

        mcauthfield_modkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID

        mcauthfield_parentrepkwkworttypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告类型表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告类型ID

        mcauthfield_repkwkworttypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告类型名称

        mcauthfield_repkwkworttypename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制该报告类型是否可用

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改日期

        mcauthfield_modkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改者ID关联用户

        mcauthfield_modkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID

        mcauthfield_parentrepkwkworttypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkworttypes.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkworttypes().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkworttypes.objects.filter(**filter)
        else:
            records = mc_repkwkworttypes.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_users_55300 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55300.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_users_55302 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55302.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_repkwkworttypes_55303 = []
        for m in mc_repkwkworttypes.objects.all():
            mobj = m.toJson()
            data_mc_repkwkworttypes_55303.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkworttypename"),
                }
            )
        return render(request, "config_busi/repkwkworttypes.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkworttypes()

        # 报告类型ID

        if mcauthfield_repkwkworttypeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkworttypeid = str(uuid.uuid4())
        # 报告类型名称

        if mcauthfield_repkwkworttypename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repkwkworttypename = obj.get("repkwkworttypename")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 是否激活用于控制该报告类型是否可用

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 创建日期

        if mcauthfield_createddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.createddate = obj.get("createddate")
        # 创建者ID关联用户

        if mcauthfield_createdby["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 修改日期

        if mcauthfield_modkwkwifieddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.modkwkwifieddate = obj.get("modkwkwifieddate")
        # 修改者ID关联用户

        if mcauthfield_modkwkwifiedby["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.modkwkwifiedby = obj.get("modkwkwifiedby")
        # 父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID

        if mcauthfield_parentrepkwkworttypeid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.parentrepkwkworttypeid = obj.get("parentrepkwkworttypeid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkworttypes.objects.get(id=obj.get("_id_upd"))

        # 报告类型ID

        if mcauthfield_repkwkworttypeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkworttypeid = str(uuid.uuid4())

            ins_table_busi.repkwkworttypeid = str(ins_table_busi.repkwkworttypeid)
        # 报告类型名称

        if mcauthfield_repkwkworttypename["mcauthchange"]:

            # CharField

            ins_table_busi.repkwkworttypename = obj.get("repkwkworttypename")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 是否激活用于控制该报告类型是否可用

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 创建日期

        if mcauthfield_createddate["mcauthchange"]:

            # DateField

            ins_table_busi.createddate = obj.get("createddate")
        # 创建者ID关联用户

        if mcauthfield_createdby["mcauthchange"]:

            # SelectField

            ins_table_busi.createdby = obj.get("createdby")
        # 修改日期

        if mcauthfield_modkwkwifieddate["mcauthchange"]:

            # DateField

            ins_table_busi.modkwkwifieddate = obj.get("modkwkwifieddate")
        # 修改者ID关联用户

        if mcauthfield_modkwkwifiedby["mcauthchange"]:

            # SelectField

            ins_table_busi.modkwkwifiedby = obj.get("modkwkwifiedby")
        # 父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID

        if mcauthfield_parentrepkwkworttypeid["mcauthchange"]:

            # SelectField

            ins_table_busi.parentrepkwkworttypeid = obj.get("parentrepkwkworttypeid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkworttypes.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkworttypes.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkworttypes")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortaudits(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告审核表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告审核ID

        mcauthfield_repkwkwortauditid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核人ID

        mcauthfield_auditkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核日期

        mcauthfield_auditdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态

        mcauthfield_auditstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核意见

        mcauthfield_auditcomment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 批准日期

        mcauthfield_approvaldate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 批准人

        mcauthfield_approvalby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已批准

        mcauthfield_isapproved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 拒绝理由

        mcauthfield_rejectionrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告审核表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告审核ID

        mcauthfield_repkwkwortauditid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核人ID

        mcauthfield_auditkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核日期

        mcauthfield_auditdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态

        mcauthfield_auditstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核意见

        mcauthfield_auditcomment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 批准日期

        mcauthfield_approvaldate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 批准人

        mcauthfield_approvalby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已批准

        mcauthfield_isapproved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 拒绝理由

        mcauthfield_rejectionrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortaudits.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortaudits().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortaudits.objects.filter(**filter)
        else:
            records = mc_repkwkwortaudits.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/repkwkwortaudits.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortaudits()

        # 报告审核ID

        if mcauthfield_repkwkwortauditid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortauditid = str(uuid.uuid4())
        # 报告ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 审核人ID

        if mcauthfield_auditkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.auditkwkworid = str(uuid.uuid4())
        # 审核日期

        if mcauthfield_auditdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.auditdate = obj.get("auditdate")
        # 审核状态

        if mcauthfield_auditstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.auditstatus = obj.get("auditstatus")
        # 审核意见

        if mcauthfield_auditcomment["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.auditcomment = obj.get("auditcomment")
        # 批准日期

        if mcauthfield_approvaldate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.approvaldate = obj.get("approvaldate")
        # 批准人

        if mcauthfield_approvalby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.approvalby = obj.get("approvalby")
        # 是否已批准

        if mcauthfield_isapproved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isapproved = obj.get("isapproved")
        # 拒绝理由

        if mcauthfield_rejectionrekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rejectionrekwkwason = obj.get("rejectionrekwkwason")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortaudits.objects.get(id=obj.get("_id_upd"))

        # 报告审核ID

        if mcauthfield_repkwkwortauditid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortauditid = str(uuid.uuid4())

            ins_table_busi.repkwkwortauditid = str(ins_table_busi.repkwkwortauditid)
        # 报告ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 审核人ID

        if mcauthfield_auditkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.auditkwkworid = str(uuid.uuid4())

            ins_table_busi.auditkwkworid = str(ins_table_busi.auditkwkworid)
        # 审核日期

        if mcauthfield_auditdate["mcauthchange"]:

            # DateField

            ins_table_busi.auditdate = obj.get("auditdate")
        # 审核状态

        if mcauthfield_auditstatus["mcauthchange"]:

            # CharField

            ins_table_busi.auditstatus = obj.get("auditstatus")
        # 审核意见

        if mcauthfield_auditcomment["mcauthchange"]:

            # CharField

            ins_table_busi.auditcomment = obj.get("auditcomment")
        # 批准日期

        if mcauthfield_approvaldate["mcauthchange"]:

            # DateField

            ins_table_busi.approvaldate = obj.get("approvaldate")
        # 批准人

        if mcauthfield_approvalby["mcauthchange"]:

            # CharField

            ins_table_busi.approvalby = obj.get("approvalby")
        # 是否已批准

        if mcauthfield_isapproved["mcauthchange"]:

            # BooleanField

            ins_table_busi.isapproved = obj.get("isapproved")
        # 拒绝理由

        if mcauthfield_rejectionrekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.rejectionrekwkwason = obj.get("rejectionrekwkwason")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortaudits.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortaudits.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortaudits")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_auditcomments(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 审核意见表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核意见内容

        mcauthfield_commentcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_creationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者ID关联用户

        mcauthfield_lkwkwastmodkwkwifierid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改时间

        mcauthfield_lkwkwastmodkwkwificationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态例如待审核、已通过、未通过

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标ID关联被审核对象的ID如周报ID

        mcauthfield_targetid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标类型例如周报、项目报告等

        mcauthfield_targettype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 审核意见表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核意见内容

        mcauthfield_commentcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_creationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者ID关联用户

        mcauthfield_lkwkwastmodkwkwifierid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改时间

        mcauthfield_lkwkwastmodkwkwificationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态例如待审核、已通过、未通过

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标ID关联被审核对象的ID如周报ID

        mcauthfield_targetid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标类型例如周报、项目报告等

        mcauthfield_targettype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_auditcomments.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_auditcomments().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_auditcomments.objects.filter(**filter)
        else:
            records = mc_auditcomments.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_users_55316 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55316.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_users_55318 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55318.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_weeklyrepkwkworts_55321 = []
        for m in mc_weeklyrepkwkworts.objects.all():
            mobj = m.toJson()
            data_mc_weeklyrepkwkworts_55321.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortcontent"),
                }
            )
        return render(request, "config_busi/auditcomments.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_auditcomments()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 审核意见内容

        if mcauthfield_commentcontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.commentcontent = obj.get("commentcontent")
        # 创建者ID关联用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_creationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.creationtime = obj.get("creationtime")
        # 最后修改者ID关联用户

        if mcauthfield_lkwkwastmodkwkwifierid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifierid = obj.get("lkwkwastmodkwkwifierid")
        # 最后修改时间

        if mcauthfield_lkwkwastmodkwkwificationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwificationtime = obj.get(
                "lkwkwastmodkwkwificationtime"
            )
        # 审核状态例如待审核、已通过、未通过

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 目标ID关联被审核对象的ID如周报ID

        if mcauthfield_targetid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.targetid = obj.get("targetid")
        # 目标类型例如周报、项目报告等

        if mcauthfield_targettype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.targettype = obj.get("targettype")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_auditcomments.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 审核意见内容

        if mcauthfield_commentcontent["mcauthchange"]:

            # TextField

            ins_table_busi.commentcontent = obj.get("commentcontent")
        # 创建者ID关联用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_creationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.creationtime = obj.get("creationtime")
        # 最后修改者ID关联用户

        if mcauthfield_lkwkwastmodkwkwifierid["mcauthchange"]:

            # SelectField

            ins_table_busi.lkwkwastmodkwkwifierid = obj.get("lkwkwastmodkwkwifierid")
        # 最后修改时间

        if mcauthfield_lkwkwastmodkwkwificationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastmodkwkwificationtime = obj.get(
                "lkwkwastmodkwkwificationtime"
            )
        # 审核状态例如待审核、已通过、未通过

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 目标ID关联被审核对象的ID如周报ID

        if mcauthfield_targetid["mcauthchange"]:

            # SelectField

            ins_table_busi.targetid = obj.get("targetid")
        # 目标类型例如周报、项目报告等

        if mcauthfield_targettype["mcauthchange"]:

            # CharField

            ins_table_busi.targettype = obj.get("targettype")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_auditcomments.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_auditcomments.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/auditcomments")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_departments(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 部门表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门名称

        mcauthfield_departmentname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上级部门ID

        mcauthfield_parentdepartmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门编码

        mcauthfield_departmentcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改日期

        mcauthfield_lkwkwastmodkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改人

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否活跃

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 部门表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门名称

        mcauthfield_departmentname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上级部门ID

        mcauthfield_parentdepartmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门编码

        mcauthfield_departmentcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改日期

        mcauthfield_lkwkwastmodkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改人

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否活跃

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_departments.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_departments().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_departments.objects.filter(**filter)
        else:
            records = mc_departments.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/departments.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_departments()

        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        # 部门名称

        if mcauthfield_departmentname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.departmentname = obj.get("departmentname")
        # 上级部门ID

        if mcauthfield_parentdepartmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.parentdepartmentid = str(uuid.uuid4())
        # 部门编码

        if mcauthfield_departmentcode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.departmentcode = obj.get("departmentcode")
        # 部门描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建日期

        if mcauthfield_createdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.createdate = obj.get("createdate")
        # 创建人

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 最后修改日期

        if mcauthfield_lkwkwastmodkwkwifieddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifieddate = obj.get(
                "lkwkwastmodkwkwifieddate"
            )
        # 最后修改人

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 是否活跃

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_departments.objects.get(id=obj.get("_id_upd"))

        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        # 部门名称

        if mcauthfield_departmentname["mcauthchange"]:

            # CharField

            ins_table_busi.departmentname = obj.get("departmentname")
        # 上级部门ID

        if mcauthfield_parentdepartmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.parentdepartmentid = str(uuid.uuid4())

            ins_table_busi.parentdepartmentid = str(ins_table_busi.parentdepartmentid)
        # 部门编码

        if mcauthfield_departmentcode["mcauthchange"]:

            # CharField

            ins_table_busi.departmentcode = obj.get("departmentcode")
        # 部门描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建日期

        if mcauthfield_createdate["mcauthchange"]:

            # DateField

            ins_table_busi.createdate = obj.get("createdate")
        # 创建人

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 最后修改日期

        if mcauthfield_lkwkwastmodkwkwifieddate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmodkwkwifieddate = obj.get(
                "lkwkwastmodkwkwifieddate"
            )
        # 最后修改人

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 是否活跃

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_departments.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_departments.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/departments")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_employees(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 员工表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 员工ID

        mcauthfield_employeeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工姓名

        mcauthfield_employeename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 职位

        mcauthfield_position = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮件

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 入职日期

        mcauthfield_startdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 薪资

        mcauthfield_salary = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上级员工ID

        mcauthfield_managerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否在职

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 员工表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 员工ID

        mcauthfield_employeeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工姓名

        mcauthfield_employeename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 职位

        mcauthfield_position = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮件

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 入职日期

        mcauthfield_startdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 薪资

        mcauthfield_salary = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上级员工ID

        mcauthfield_managerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否在职

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_employees.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_employees().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_employees.objects.filter(**filter)
        else:
            records = mc_employees.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/employees.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_employees()

        # 员工ID

        if mcauthfield_employeeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.employeeid = str(uuid.uuid4())
        # 员工姓名

        if mcauthfield_employeename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.employeename = obj.get("employeename")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        # 职位

        if mcauthfield_position["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.position = obj.get("position")
        # 电子邮件

        if mcauthfield_email["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 入职日期

        if mcauthfield_startdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.startdate = obj.get("startdate")
        # 薪资

        if mcauthfield_salary["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.salary = obj.get("salary")
        # 上级员工ID

        if mcauthfield_managerid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.managerid = str(uuid.uuid4())
        # 是否在职

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_employees.objects.get(id=obj.get("_id_upd"))

        # 员工ID

        if mcauthfield_employeeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.employeeid = str(uuid.uuid4())

            ins_table_busi.employeeid = str(ins_table_busi.employeeid)
        # 员工姓名

        if mcauthfield_employeename["mcauthchange"]:

            # CharField

            ins_table_busi.employeename = obj.get("employeename")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        # 职位

        if mcauthfield_position["mcauthchange"]:

            # CharField

            ins_table_busi.position = obj.get("position")
        # 电子邮件

        if mcauthfield_email["mcauthchange"]:

            # CharField

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 入职日期

        if mcauthfield_startdate["mcauthchange"]:

            # DateField

            ins_table_busi.startdate = obj.get("startdate")
        # 薪资

        if mcauthfield_salary["mcauthchange"]:

            # CharField

            ins_table_busi.salary = obj.get("salary")
        # 上级员工ID

        if mcauthfield_managerid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.managerid = str(uuid.uuid4())

            ins_table_busi.managerid = str(ins_table_busi.managerid)
        # 是否在职

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_employees.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_employees.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/employees")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_employeeweeklyrepkwkwortrelations(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 员工周报关联表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工ID

        mcauthfield_employeeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周报开始日期

        mcauthfield_weekstartdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周报结束日期

        mcauthfield_weekenddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如已提交、待审核、已审核等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 提交时间

        mcauthfield_submittime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核人ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 员工周报关联表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工ID

        mcauthfield_employeeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周报开始日期

        mcauthfield_weekstartdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 周报结束日期

        mcauthfield_weekenddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如已提交、待审核、已审核等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 提交时间

        mcauthfield_submittime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核人ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_employeeweeklyrepkwkwortrelations.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_employeeweeklyrepkwkwortrelations().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_employeeweeklyrepkwkwortrelations.objects.filter(**filter)
        else:
            records = mc_employeeweeklyrepkwkwortrelations.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_employeeweeklyrepkwkwortrelations_55343 = []
        for m in mc_employeeweeklyrepkwkwortrelations.objects.all():
            mobj = m.toJson()
            data_mc_employeeweeklyrepkwkwortrelations_55343.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("id"),
                }
            )
        return render(
            request, "config_busi/employeeweeklyrepkwkwortrelations.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_employeeweeklyrepkwkwortrelations()

        # 关联ID

        if mcauthfield_id["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 员工ID

        if mcauthfield_employeeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.employeeid = str(uuid.uuid4())
        # 周报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 周报开始日期

        if mcauthfield_weekstartdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.weekstartdate = obj.get("weekstartdate")
        # 周报结束日期

        if mcauthfield_weekenddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.weekenddate = obj.get("weekenddate")
        # 状态如已提交、待审核、已审核等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 提交时间

        if mcauthfield_submittime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.submittime = obj.get("submittime")
        # 审核人ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.reviewerid = str(uuid.uuid4())
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.reviewtime = obj.get("reviewtime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_employeeweeklyrepkwkwortrelations.objects.get(
            id=obj.get("_id_upd")
        )

        # 关联ID

        if mcauthfield_id["mcauthchange"]:

            # SelectField

            ins_table_busi.id = obj.get("id")
        # 员工ID

        if mcauthfield_employeeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.employeeid = str(uuid.uuid4())

            ins_table_busi.employeeid = str(ins_table_busi.employeeid)
        # 周报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 周报开始日期

        if mcauthfield_weekstartdate["mcauthchange"]:

            # DateField

            ins_table_busi.weekstartdate = obj.get("weekstartdate")
        # 周报结束日期

        if mcauthfield_weekenddate["mcauthchange"]:

            # DateField

            ins_table_busi.weekenddate = obj.get("weekenddate")
        # 状态如已提交、待审核、已审核等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 提交时间

        if mcauthfield_submittime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.submittime = obj.get("submittime")
        # 审核人ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.reviewerid = str(uuid.uuid4())

            ins_table_busi.reviewerid = str(ins_table_busi.reviewerid)
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.reviewtime = obj.get("reviewtime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_employeeweeklyrepkwkwortrelations.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_employeeweeklyrepkwkwortrelations.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/employeeweeklyrepkwkwortrelations")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_notkwkwifications(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 通知表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 通知ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 通知标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 通知内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者ID

        mcauthfield_senderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者ID

        mcauthfield_receiverid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 阅读状态

        mcauthfield_readstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 优先级

        mcauthfield_prikwkwority = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 通知表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 通知ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 通知标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 通知内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者ID

        mcauthfield_senderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者ID

        mcauthfield_receiverid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 阅读状态

        mcauthfield_readstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 优先级

        mcauthfield_prikwkwority = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_notkwkwifications.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_notkwkwifications().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_notkwkwifications.objects.filter(**filter)
        else:
            records = mc_notkwkwifications.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/notkwkwifications.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_notkwkwifications()

        # 通知ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 通知标题

        if mcauthfield_title["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.title = obj.get("title")
        # 通知内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 发送者ID

        if mcauthfield_senderid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.senderid = str(uuid.uuid4())
        # 接收者ID

        if mcauthfield_receiverid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.receiverid = str(uuid.uuid4())
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 阅读状态

        if mcauthfield_readstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.readstatus = obj.get("readstatus")
        # 优先级

        if mcauthfield_prikwkwority["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.prikwkwority = obj.get("prikwkwority")
        # 是否删除

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_notkwkwifications.objects.get(id=obj.get("_id_upd"))

        # 通知ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 通知标题

        if mcauthfield_title["mcauthchange"]:

            # CharField

            ins_table_busi.title = obj.get("title")
        # 通知内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 发送者ID

        if mcauthfield_senderid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.senderid = str(uuid.uuid4())

            ins_table_busi.senderid = str(ins_table_busi.senderid)
        # 接收者ID

        if mcauthfield_receiverid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.receiverid = str(uuid.uuid4())

            ins_table_busi.receiverid = str(ins_table_busi.receiverid)
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 阅读状态

        if mcauthfield_readstatus["mcauthchange"]:

            # CharField

            ins_table_busi.readstatus = obj.get("readstatus")
        # 优先级

        if mcauthfield_prikwkwority["mcauthchange"]:

            # CharField

            ins_table_busi.prikwkwority = obj.get("prikwkwority")
        # 是否删除

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_notkwkwifications.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_notkwkwifications.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/notkwkwifications")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_notkwkwificationtypes(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 通知类型表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 通知类型ID

        mcauthfield_notkwkwificationtypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 通知类型名称

        mcauthfield_notkwkwificationtypename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改日期

        mcauthfield_modkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改者

        mcauthfield_modkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父通知类型ID

        mcauthfield_parentnotkwkwificationtypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 通知类型表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 通知类型ID

        mcauthfield_notkwkwificationtypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 通知类型名称

        mcauthfield_notkwkwificationtypename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_createddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改日期

        mcauthfield_modkwkwifieddate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改者

        mcauthfield_modkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父通知类型ID

        mcauthfield_parentnotkwkwificationtypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_notkwkwificationtypes.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_notkwkwificationtypes().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_notkwkwificationtypes.objects.filter(**filter)
        else:
            records = mc_notkwkwificationtypes.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/notkwkwificationtypes.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_notkwkwificationtypes()

        # 通知类型ID

        if mcauthfield_notkwkwificationtypeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.notkwkwificationtypeid = str(uuid.uuid4())
        # 通知类型名称

        if mcauthfield_notkwkwificationtypename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.notkwkwificationtypename = obj.get(
                "notkwkwificationtypename"
            )
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 创建日期

        if mcauthfield_createddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.createddate = obj.get("createddate")
        # 创建者

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 修改日期

        if mcauthfield_modkwkwifieddate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.modkwkwifieddate = obj.get("modkwkwifieddate")
        # 修改者

        if mcauthfield_modkwkwifiedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.modkwkwifiedby = obj.get("modkwkwifiedby")
        # 父通知类型ID

        if mcauthfield_parentnotkwkwificationtypeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.parentnotkwkwificationtypeid = str(uuid.uuid4())
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_notkwkwificationtypes.objects.get(id=obj.get("_id_upd"))

        # 通知类型ID

        if mcauthfield_notkwkwificationtypeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.notkwkwificationtypeid = str(uuid.uuid4())

            ins_table_busi.notkwkwificationtypeid = str(
                ins_table_busi.notkwkwificationtypeid
            )
        # 通知类型名称

        if mcauthfield_notkwkwificationtypename["mcauthchange"]:

            # CharField

            ins_table_busi.notkwkwificationtypename = obj.get(
                "notkwkwificationtypename"
            )
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 创建日期

        if mcauthfield_createddate["mcauthchange"]:

            # DateField

            ins_table_busi.createddate = obj.get("createddate")
        # 创建者

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 修改日期

        if mcauthfield_modkwkwifieddate["mcauthchange"]:

            # DateField

            ins_table_busi.modkwkwifieddate = obj.get("modkwkwifieddate")
        # 修改者

        if mcauthfield_modkwkwifiedby["mcauthchange"]:

            # CharField

            ins_table_busi.modkwkwifiedby = obj.get("modkwkwifiedby")
        # 父通知类型ID

        if mcauthfield_parentnotkwkwificationtypeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.parentnotkwkwificationtypeid = str(uuid.uuid4())

            ins_table_busi.parentnotkwkwificationtypeid = str(
                ins_table_busi.parentnotkwkwificationtypeid
            )
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_notkwkwificationtypes.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_notkwkwificationtypes.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/notkwkwificationtypes")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_emaillogs(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 邮件发送记录表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮件地址

        mcauthfield_emailaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 邮件主题

        mcauthfield_subject = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 邮件内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态如成功、失败、待发送

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 收件人数量

        mcauthfield_recipientcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者ID关联用户

        mcauthfield_senderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 附件数量

        mcauthfield_attachmentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 邮件发送记录表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮件地址

        mcauthfield_emailaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 邮件主题

        mcauthfield_subject = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 邮件内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态如成功、失败、待发送

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 收件人数量

        mcauthfield_recipientcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者ID关联用户

        mcauthfield_senderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 附件数量

        mcauthfield_attachmentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_emaillogs.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_emaillogs().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_emaillogs.objects.filter(**filter)
        else:
            records = mc_emaillogs.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_users_55378 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55378.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/emaillogs.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_emaillogs()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 电子邮件地址

        if mcauthfield_emailaddress["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.emailaddress = obj.get("emailaddress")
        # 邮件主题

        if mcauthfield_subject["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.subject = obj.get("subject")
        # 邮件内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送状态如成功、失败、待发送

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 收件人数量

        if mcauthfield_recipientcount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.recipientcount = obj.get("recipientcount")
        # 发送者ID关联用户

        if mcauthfield_senderid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.senderid = obj.get("senderid")
        # 附件数量

        if mcauthfield_attachmentcount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.attachmentcount = obj.get("attachmentcount")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_emaillogs.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 电子邮件地址

        if mcauthfield_emailaddress["mcauthchange"]:

            # TextField

            ins_table_busi.emailaddress = obj.get("emailaddress")
        # 邮件主题

        if mcauthfield_subject["mcauthchange"]:

            # CharField

            ins_table_busi.subject = obj.get("subject")
        # 邮件内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送状态如成功、失败、待发送

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 收件人数量

        if mcauthfield_recipientcount["mcauthchange"]:

            # IntegerField

            ins_table_busi.recipientcount = obj.get("recipientcount")
        # 发送者ID关联用户

        if mcauthfield_senderid["mcauthchange"]:

            # SelectField

            ins_table_busi.senderid = obj.get("senderid")
        # 附件数量

        if mcauthfield_attachmentcount["mcauthchange"]:

            # IntegerField

            ins_table_busi.attachmentcount = obj.get("attachmentcount")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_emaillogs.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_emaillogs.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/emaillogs")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_smslogs(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 短信发送记录表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 短信内容

        mcauthfield_smscontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者号码

        mcauthfield_receivernumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者号码

        mcauthfield_sendernumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态如成功、失败、待发送

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已读标记接收者是否已查看短信

        mcauthfield_kwkwisread = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联任务ID如果短信发送与某个特定任务相关

        mcauthfield_relatedtkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 短信发送记录表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 短信内容

        mcauthfield_smscontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者号码

        mcauthfield_receivernumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者号码

        mcauthfield_sendernumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态如成功、失败、待发送

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已读标记接收者是否已查看短信

        mcauthfield_kwkwisread = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联任务ID如果短信发送与某个特定任务相关

        mcauthfield_relatedtkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_smslogs.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_smslogs().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_smslogs.objects.filter(**filter)
        else:
            records = mc_smslogs.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_repkwkwortperiods_55389 = []
        for m in mc_repkwkwortperiods.objects.all():
            mobj = m.toJson()
            data_mc_repkwkwortperiods_55389.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("periodname"),
                }
            )
        return render(request, "config_busi/smslogs.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_smslogs()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 短信内容

        if mcauthfield_smscontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.smscontent = obj.get("smscontent")
        # 接收者号码

        if mcauthfield_receivernumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.receivernumber = obj.get("receivernumber")
        # 发送者号码

        if mcauthfield_sendernumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.sendernumber = obj.get("sendernumber")
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送状态如成功、失败、待发送

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 错误信息如果发送失败

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        # 是否已读标记接收者是否已查看短信

        if mcauthfield_kwkwisread["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisread = obj.get("kwkwisread")
        # 关联任务ID如果短信发送与某个特定任务相关

        if mcauthfield_relatedtkwkwaskid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedtkwkwaskid = obj.get("relatedtkwkwaskid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_smslogs.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 短信内容

        if mcauthfield_smscontent["mcauthchange"]:

            # TextField

            ins_table_busi.smscontent = obj.get("smscontent")
        # 接收者号码

        if mcauthfield_receivernumber["mcauthchange"]:

            # CharField

            ins_table_busi.receivernumber = obj.get("receivernumber")
        # 发送者号码

        if mcauthfield_sendernumber["mcauthchange"]:

            # CharField

            ins_table_busi.sendernumber = obj.get("sendernumber")
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送状态如成功、失败、待发送

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 错误信息如果发送失败

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        # 是否已读标记接收者是否已查看短信

        if mcauthfield_kwkwisread["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisread = obj.get("kwkwisread")
        # 关联任务ID如果短信发送与某个特定任务相关

        if mcauthfield_relatedtkwkwaskid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedtkwkwaskid = obj.get("relatedtkwkwaskid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_smslogs.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_smslogs.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/smslogs")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_attachments(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 附件表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 附件ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件大小

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件类型

        mcauthfield_filetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者姓名

        mcauthfield_creatkwkworname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联周报ID

        mcauthfield_relatedrepkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 附件表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 附件ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件大小

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件类型

        mcauthfield_filetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者姓名

        mcauthfield_creatkwkworname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联周报ID

        mcauthfield_relatedrepkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_attachments.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_attachments().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_attachments.objects.filter(**filter)
        else:
            records = mc_attachments.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_weeklyrepkwkworts_55398 = []
        for m in mc_weeklyrepkwkworts.objects.all():
            mobj = m.toJson()
            data_mc_weeklyrepkwkworts_55398.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortcontent"),
                }
            )
        return render(request, "config_busi/attachments.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_attachments()

        # 附件ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小

        if mcauthfield_filesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 文件类型

        if mcauthfield_filetype["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filetype" in request.FILES:
                ins_table_busi.filetype = request.FILES["filetype"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.creatkwkworid = str(uuid.uuid4())
        # 创建者姓名

        if mcauthfield_creatkwkworname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.creatkwkworname = obj.get("creatkwkworname")
        # 关联周报ID

        if mcauthfield_relatedrepkwkwortid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedrepkwkwortid = obj.get("relatedrepkwkwortid")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_attachments.objects.get(id=obj.get("_id_upd"))

        # 附件ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save File FileField

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save File FileField

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小

        if mcauthfield_filesize["mcauthchange"]:

            # Save File FileField

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 文件类型

        if mcauthfield_filetype["mcauthchange"]:

            # Save File FileField

            if "filetype" in request.FILES:
                ins_table_busi.filetype = request.FILES["filetype"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.creatkwkworid = str(uuid.uuid4())

            ins_table_busi.creatkwkworid = str(ins_table_busi.creatkwkworid)
        # 创建者姓名

        if mcauthfield_creatkwkworname["mcauthchange"]:

            # CharField

            ins_table_busi.creatkwkworname = obj.get("creatkwkworname")
        # 关联周报ID

        if mcauthfield_relatedrepkwkwortid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedrepkwkwortid = obj.get("relatedrepkwkwortid")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_attachments.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_attachments.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/attachments")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_attachmenttypes(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 附件类型表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 附件类型ID

        mcauthfield_attachmenttypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 附件类型名称

        mcauthfield_attachmenttypename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件扩展名

        mcauthfield_fileextension = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大文件大小单位MB

        mcauthfield_maxfilesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 附件类型表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 附件类型ID

        mcauthfield_attachmenttypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 附件类型名称

        mcauthfield_attachmenttypename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件扩展名

        mcauthfield_fileextension = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大文件大小单位MB

        mcauthfield_maxfilesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_attachmenttypes.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_attachmenttypes().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_attachmenttypes.objects.filter(**filter)
        else:
            records = mc_attachmenttypes.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/attachmenttypes.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_attachmenttypes()

        # 附件类型ID

        if mcauthfield_attachmenttypeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.attachmenttypeid = str(uuid.uuid4())
        # 附件类型名称

        if mcauthfield_attachmenttypename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.attachmenttypename = obj.get("attachmenttypename")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 文件扩展名

        if mcauthfield_fileextension["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "fileextension" in request.FILES:
                ins_table_busi.fileextension = request.FILES["fileextension"]
        # 最大文件大小单位MB

        if mcauthfield_maxfilesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "maxfilesize" in request.FILES:
                ins_table_busi.maxfilesize = request.FILES["maxfilesize"]
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.createdby = str(uuid.uuid4())
        # 更新者ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.updatedby = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_attachmenttypes.objects.get(id=obj.get("_id_upd"))

        # 附件类型ID

        if mcauthfield_attachmenttypeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.attachmenttypeid = str(uuid.uuid4())

            ins_table_busi.attachmenttypeid = str(ins_table_busi.attachmenttypeid)
        # 附件类型名称

        if mcauthfield_attachmenttypename["mcauthchange"]:

            # CharField

            ins_table_busi.attachmenttypename = obj.get("attachmenttypename")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 文件扩展名

        if mcauthfield_fileextension["mcauthchange"]:

            # Save File FileField

            if "fileextension" in request.FILES:
                ins_table_busi.fileextension = request.FILES["fileextension"]
        # 最大文件大小单位MB

        if mcauthfield_maxfilesize["mcauthchange"]:

            # Save File FileField

            if "maxfilesize" in request.FILES:
                ins_table_busi.maxfilesize = request.FILES["maxfilesize"]
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.createdby = str(uuid.uuid4())

            ins_table_busi.createdby = str(ins_table_busi.createdby)
        # 更新者ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.updatedby = str(uuid.uuid4())

            ins_table_busi.updatedby = str(ins_table_busi.updatedby)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_attachmenttypes.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_attachmenttypes.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/attachmenttypes")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortsubmkwkwissionhkwkwistkwkwories(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告提交历史表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 提交日期

        mcauthfield_submkwkwissiondate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工ID

        mcauthfield_employeeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告标题

        mcauthfield_repkwkworttitle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审批日期

        mcauthfield_approvaldate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审批人ID

        mcauthfield_approverid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告提交历史表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 提交日期

        mcauthfield_submkwkwissiondate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 员工ID

        mcauthfield_employeeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告标题

        mcauthfield_repkwkworttitle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审批日期

        mcauthfield_approvaldate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审批人ID

        mcauthfield_approverid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortsubmkwkwissionhkwkwistkwkwories().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.filter(
                **filter
            )
        else:
            records = mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.all()
        # 加载界面中下拉框所需数据

        return render(
            request,
            "config_busi/repkwkwortsubmkwkwissionhkwkwistkwkwories.html",
            locals(),
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortsubmkwkwissionhkwkwistkwkwories()

        # 报告ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 提交日期

        if mcauthfield_submkwkwissiondate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.submkwkwissiondate = obj.get("submkwkwissiondate")
        # 员工ID

        if mcauthfield_employeeid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.employeeid = str(uuid.uuid4())
        # 报告标题

        if mcauthfield_repkwkworttitle["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repkwkworttitle = obj.get("repkwkworttitle")
        # 报告描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 审批日期

        if mcauthfield_approvaldate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.approvaldate = obj.get("approvaldate")
        # 审批人ID

        if mcauthfield_approverid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.approverid = str(uuid.uuid4())
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.get(
            id=obj.get("_id_upd")
        )

        # 报告ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 提交日期

        if mcauthfield_submkwkwissiondate["mcauthchange"]:

            # DateField

            ins_table_busi.submkwkwissiondate = obj.get("submkwkwissiondate")
        # 员工ID

        if mcauthfield_employeeid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.employeeid = str(uuid.uuid4())

            ins_table_busi.employeeid = str(ins_table_busi.employeeid)
        # 报告标题

        if mcauthfield_repkwkworttitle["mcauthchange"]:

            # CharField

            ins_table_busi.repkwkworttitle = obj.get("repkwkworttitle")
        # 报告描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 审批日期

        if mcauthfield_approvaldate["mcauthchange"]:

            # DateField

            ins_table_busi.approvaldate = obj.get("approvaldate")
        # 审批人ID

        if mcauthfield_approverid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.approverid = str(uuid.uuid4())

            ins_table_busi.approverid = str(ins_table_busi.approverid)
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortsubmkwkwissionhkwkwistkwkwories.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortsubmkwkwissionhkwkwistkwkwories")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortmodkwkwificationhkwkwistkwkwories(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告修改历史表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联的报告ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改时间

        mcauthfield_modkwkwificationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改者ID

        mcauthfield_modkwkwifierid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改前的内容摘要

        mcauthfield_previouscontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改后的内容摘要

        mcauthfield_modkwkwifiedcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改类型如内容更新、状态变更等

        mcauthfield_modkwkwificationtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改备注

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为最新修改用于快速检索最新记录

        mcauthfield_kwkwislatest = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告修改历史表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联的报告ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改时间

        mcauthfield_modkwkwificationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改者ID

        mcauthfield_modkwkwifierid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改前的内容摘要

        mcauthfield_previouscontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改后的内容摘要

        mcauthfield_modkwkwifiedcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改类型如内容更新、状态变更等

        mcauthfield_modkwkwificationtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改备注

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为最新修改用于快速检索最新记录

        mcauthfield_kwkwislatest = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortmodkwkwificationhkwkwistkwkwories().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.filter(
                **filter
            )
        else:
            records = mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_weeklyrepkwkworts_55420 = []
        for m in mc_weeklyrepkwkworts.objects.all():
            mobj = m.toJson()
            data_mc_weeklyrepkwkworts_55420.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortcontent"),
                }
            )
        return render(
            request,
            "config_busi/repkwkwortmodkwkwificationhkwkwistkwkwories.html",
            locals(),
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortmodkwkwificationhkwkwistkwkwories()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 关联的报告ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        # 修改时间

        if mcauthfield_modkwkwificationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.modkwkwificationtime = obj.get("modkwkwificationtime")
        # 修改者ID

        if mcauthfield_modkwkwifierid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.modkwkwifierid = str(uuid.uuid4())
        # 修改前的内容摘要

        if mcauthfield_previouscontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.previouscontent = obj.get("previouscontent")
        # 修改后的内容摘要

        if mcauthfield_modkwkwifiedcontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.modkwkwifiedcontent = obj.get("modkwkwifiedcontent")
        # 修改类型如内容更新、状态变更等

        if mcauthfield_modkwkwificationtype["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.modkwkwificationtype = obj.get("modkwkwificationtype")
        # 修改备注

        if mcauthfield_comment["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.comment = obj.get("comment")
        # 是否为最新修改用于快速检索最新记录

        if mcauthfield_kwkwislatest["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwislatest = obj.get("kwkwislatest")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.get(
            id=obj.get("_id_upd")
        )

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 关联的报告ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        # 修改时间

        if mcauthfield_modkwkwificationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.modkwkwificationtime = obj.get("modkwkwificationtime")
        # 修改者ID

        if mcauthfield_modkwkwifierid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.modkwkwifierid = str(uuid.uuid4())

            ins_table_busi.modkwkwifierid = str(ins_table_busi.modkwkwifierid)
        # 修改前的内容摘要

        if mcauthfield_previouscontent["mcauthchange"]:

            # TextField

            ins_table_busi.previouscontent = obj.get("previouscontent")
        # 修改后的内容摘要

        if mcauthfield_modkwkwifiedcontent["mcauthchange"]:

            # TextField

            ins_table_busi.modkwkwifiedcontent = obj.get("modkwkwifiedcontent")
        # 修改类型如内容更新、状态变更等

        if mcauthfield_modkwkwificationtype["mcauthchange"]:

            # TextField

            ins_table_busi.modkwkwificationtype = obj.get("modkwkwificationtype")
        # 修改备注

        if mcauthfield_comment["mcauthchange"]:

            # CharField

            ins_table_busi.comment = obj.get("comment")
        # 是否为最新修改用于快速检索最新记录

        if mcauthfield_kwkwislatest["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwislatest = obj.get("kwkwislatest")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortmodkwkwificationhkwkwistkwkwories.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortmodkwkwificationhkwkwistkwkwories")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortcomments(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告评论表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 评论ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告ID关联字段指向报告的ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除逻辑删除标记

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分可选用于示用户对报告的评分

        mcauthfield_ratkwkwing = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论状态如待审核、已审核、隐藏等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告评论表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 评论ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告ID关联字段指向报告的ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除逻辑删除标记

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分可选用于示用户对报告的评分

        mcauthfield_ratkwkwing = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论状态如待审核、已审核、隐藏等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortcomments.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortcomments().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortcomments.objects.filter(**filter)
        else:
            records = mc_repkwkwortcomments.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_weeklyrepkwkworts_55429 = []
        for m in mc_weeklyrepkwkworts.objects.all():
            mobj = m.toJson()
            data_mc_weeklyrepkwkworts_55429.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortcontent"),
                }
            )
        data_mc_users_55430 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55430.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/repkwkwortcomments.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortcomments()

        # 评论ID

        if mcauthfield_id["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 报告ID关联字段指向报告的ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        # 用户ID关联字段指向用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 评论内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否删除逻辑删除标记

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        # 评分可选用于示用户对报告的评分

        if mcauthfield_ratkwkwing["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.ratkwkwing = obj.get("ratkwkwing")
        # 评论状态如待审核、已审核、隐藏等

        if mcauthfield_status["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortcomments.objects.get(id=obj.get("_id_upd"))

        # 评论ID

        if mcauthfield_id["mcauthchange"]:

            # TextField

            ins_table_busi.id = obj.get("id")
        # 报告ID关联字段指向报告的ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        # 用户ID关联字段指向用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 评论内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否删除逻辑删除标记

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        # 评分可选用于示用户对报告的评分

        if mcauthfield_ratkwkwing["mcauthchange"]:

            # IntegerField

            ins_table_busi.ratkwkwing = obj.get("ratkwkwing")
        # 评论状态如待审核、已审核、隐藏等

        if mcauthfield_status["mcauthchange"]:

            # TextField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortcomments.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortcomments.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortcomments")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_commentreplies(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 评论回复表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 回复ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论ID关联字段指向评论的ID

        mcauthfield_commentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除逻辑删除标记

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 点赞数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复的回复ID用于构建回复链关联字段指向本的ID

        mcauthfield_replytoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 评论回复表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 回复ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论ID关联字段指向评论的ID

        mcauthfield_commentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除逻辑删除标记

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 点赞数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复的回复ID用于构建回复链关联字段指向本的ID

        mcauthfield_replytoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_commentreplies.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_commentreplies().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_commentreplies.objects.filter(**filter)
        else:
            records = mc_commentreplies.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_repkwkwortcomments_55438 = []
        for m in mc_repkwkwortcomments.objects.all():
            mobj = m.toJson()
            data_mc_repkwkwortcomments_55438.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("content"),
                }
            )
        data_mc_users_55439 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55439.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_commentreplies_55445 = []
        for m in mc_commentreplies.objects.all():
            mobj = m.toJson()
            data_mc_commentreplies_55445.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("content"),
                }
            )
        return render(request, "config_busi/commentreplies.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_commentreplies()

        # 回复ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 评论ID关联字段指向评论的ID

        if mcauthfield_commentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.commentid = obj.get("commentid")
        # 用户ID关联字段指向用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 回复内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否删除逻辑删除标记

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        # 点赞数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likecount = obj.get("likecount")
        # 回复的回复ID用于构建回复链关联字段指向本的ID

        if mcauthfield_replytoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.replytoid = obj.get("replytoid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_commentreplies.objects.get(id=obj.get("_id_upd"))

        # 回复ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 评论ID关联字段指向评论的ID

        if mcauthfield_commentid["mcauthchange"]:

            # SelectField

            ins_table_busi.commentid = obj.get("commentid")
        # 用户ID关联字段指向用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 回复内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否删除逻辑删除标记

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        # 点赞数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField

            ins_table_busi.likecount = obj.get("likecount")
        # 回复的回复ID用于构建回复链关联字段指向本的ID

        if mcauthfield_replytoid["mcauthchange"]:

            # SelectField

            ins_table_busi.replytoid = obj.get("replytoid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_commentreplies.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_commentreplies.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/commentreplies")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortratkwkwings(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报告评分表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告ID唯一标识一个报告

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分示对报告的评分可以是数值类型

        mcauthfield_ratkwkwing = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分者ID示哪个用户或系统对报告进行了评分

        mcauthfield_raterid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告日期报告提交的日期

        mcauthfield_repkwkwortdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分日期对报告进行评分的日期

        mcauthfield_ratkwkwingdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评语对报告的额外评语或反馈

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否通过示报告是否通过审核

        mcauthfield_kwkwisapproved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 类别ID关联字段示报告所属的类别

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报告评分表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报告ID唯一标识一个报告

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分示对报告的评分可以是数值类型

        mcauthfield_ratkwkwing = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分者ID示哪个用户或系统对报告进行了评分

        mcauthfield_raterid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告日期报告提交的日期

        mcauthfield_repkwkwortdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分日期对报告进行评分的日期

        mcauthfield_ratkwkwingdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评语对报告的额外评语或反馈

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否通过示报告是否通过审核

        mcauthfield_kwkwisapproved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 类别ID关联字段示报告所属的类别

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortratkwkwings.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortratkwkwings().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortratkwkwings.objects.filter(**filter)
        else:
            records = mc_repkwkwortratkwkwings.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_repkwkworttypes_55453 = []
        for m in mc_repkwkworttypes.objects.all():
            mobj = m.toJson()
            data_mc_repkwkworttypes_55453.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkworttypename"),
                }
            )
        return render(request, "config_busi/repkwkwortratkwkwings.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortratkwkwings()

        # 报告ID唯一标识一个报告

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 评分示对报告的评分可以是数值类型

        if mcauthfield_ratkwkwing["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.ratkwkwing = obj.get("ratkwkwing")
        # 评分者ID示哪个用户或系统对报告进行了评分

        if mcauthfield_raterid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.raterid = str(uuid.uuid4())
        # 报告日期报告提交的日期

        if mcauthfield_repkwkwortdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.repkwkwortdate = obj.get("repkwkwortdate")
        # 评分日期对报告进行评分的日期

        if mcauthfield_ratkwkwingdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.ratkwkwingdate = obj.get("ratkwkwingdate")
        # 评语对报告的额外评语或反馈

        if mcauthfield_comment["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.comment = obj.get("comment")
        # 是否通过示报告是否通过审核

        if mcauthfield_kwkwisapproved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisapproved = obj.get("kwkwisapproved")
        # 类别ID关联字段示报告所属的类别

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortratkwkwings.objects.get(id=obj.get("_id_upd"))

        # 报告ID唯一标识一个报告

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 评分示对报告的评分可以是数值类型

        if mcauthfield_ratkwkwing["mcauthchange"]:

            # IntegerField

            ins_table_busi.ratkwkwing = obj.get("ratkwkwing")
        # 评分者ID示哪个用户或系统对报告进行了评分

        if mcauthfield_raterid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.raterid = str(uuid.uuid4())

            ins_table_busi.raterid = str(ins_table_busi.raterid)
        # 报告日期报告提交的日期

        if mcauthfield_repkwkwortdate["mcauthchange"]:

            # DateField

            ins_table_busi.repkwkwortdate = obj.get("repkwkwortdate")
        # 评分日期对报告进行评分的日期

        if mcauthfield_ratkwkwingdate["mcauthchange"]:

            # DateField

            ins_table_busi.ratkwkwingdate = obj.get("ratkwkwingdate")
        # 评语对报告的额外评语或反馈

        if mcauthfield_comment["mcauthchange"]:

            # CharField

            ins_table_busi.comment = obj.get("comment")
        # 是否通过示报告是否通过审核

        if mcauthfield_kwkwisapproved["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisapproved = obj.get("kwkwisapproved")
        # 类别ID关联字段示报告所属的类别

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortratkwkwings.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortratkwkwings.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortratkwkwings")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_ratkwkwingcriteria(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 评分标准表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分标准名称

        mcauthfield_criterianame = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 类别

        mcauthfield_categkwkwory = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权重

        mcauthfield_weight = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联项目ID

        mcauthfield_relateditemid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联项目类型

        mcauthfield_relateditemtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 评分标准表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评分标准名称

        mcauthfield_criterianame = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 类别

        mcauthfield_categkwkwory = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权重

        mcauthfield_weight = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联项目ID

        mcauthfield_relateditemid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联项目类型

        mcauthfield_relateditemtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_ratkwkwingcriteria.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_ratkwkwingcriteria().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_ratkwkwingcriteria.objects.filter(**filter)
        else:
            records = mc_ratkwkwingcriteria.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_repkwkwortratkwkwings_55462 = []
        for m in mc_repkwkwortratkwkwings.objects.all():
            mobj = m.toJson()
            data_mc_repkwkwortratkwkwings_55462.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortdate"),
                }
            )
        data_mc_repkwkworttypes_55463 = []
        for m in mc_repkwkworttypes.objects.all():
            mobj = m.toJson()
            data_mc_repkwkworttypes_55463.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkworttypename"),
                }
            )
        return render(request, "config_busi/ratkwkwingcriteria.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_ratkwkwingcriteria()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 评分标准名称

        if mcauthfield_criterianame["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.criterianame = obj.get("criterianame")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 类别

        if mcauthfield_categkwkwory["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.categkwkwory = obj.get("categkwkwory")
        # 权重

        if mcauthfield_weight["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.weight = obj.get("weight")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 关联项目ID

        if mcauthfield_relateditemid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relateditemid = obj.get("relateditemid")
        # 关联项目类型

        if mcauthfield_relateditemtype["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relateditemtype = obj.get("relateditemtype")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_ratkwkwingcriteria.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 评分标准名称

        if mcauthfield_criterianame["mcauthchange"]:

            # IntegerField

            ins_table_busi.criterianame = obj.get("criterianame")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 类别

        if mcauthfield_categkwkwory["mcauthchange"]:

            # CharField

            ins_table_busi.categkwkwory = obj.get("categkwkwory")
        # 权重

        if mcauthfield_weight["mcauthchange"]:

            # CharField

            ins_table_busi.weight = obj.get("weight")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 关联项目ID

        if mcauthfield_relateditemid["mcauthchange"]:

            # SelectField

            ins_table_busi.relateditemid = obj.get("relateditemid")
        # 关联项目类型

        if mcauthfield_relateditemtype["mcauthchange"]:

            # SelectField

            ins_table_busi.relateditemtype = obj.get("relateditemtype")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_ratkwkwingcriteria.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_ratkwkwingcriteria.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/ratkwkwingcriteria")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_permkwkwissions(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 权限表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制权限是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父权限ID用于构建权限层级关系

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联角色ID示该权限属于哪个角色

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 所属系统模块标识权限属于哪个系统模块或功能区域

        mcauthfield_systemmodule = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 权限表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制权限是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父权限ID用于构建权限层级关系

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联角色ID示该权限属于哪个角色

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 所属系统模块标识权限属于哪个系统模块或功能区域

        mcauthfield_systemmodule = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_permkwkwissions.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_permkwkwissions().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_permkwkwissions.objects.filter(**filter)
        else:
            records = mc_permkwkwissions.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_roles_55471 = []
        for m in mc_roles.objects.all():
            mobj = m.toJson()
            data_mc_roles_55471.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("rolename"),
                }
            )
        return render(request, "config_busi/permkwkwissions.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_permkwkwissions()

        # 权限ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 权限名称

        if mcauthfield_name["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.name = obj.get("name")
        # 权限描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制权限是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 父权限ID用于构建权限层级关系

        if mcauthfield_parentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.parentid = str(uuid.uuid4())
        # 关联角色ID示该权限属于哪个角色

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.roleid = obj.get("roleid")
        # 所属系统模块标识权限属于哪个系统模块或功能区域

        if mcauthfield_systemmodule["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.systemmodule = obj.get("systemmodule")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_permkwkwissions.objects.get(id=obj.get("_id_upd"))

        # 权限ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 权限名称

        if mcauthfield_name["mcauthchange"]:

            # CharField

            ins_table_busi.name = obj.get("name")
        # 权限描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制权限是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 父权限ID用于构建权限层级关系

        if mcauthfield_parentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.parentid = str(uuid.uuid4())

            ins_table_busi.parentid = str(ins_table_busi.parentid)
        # 关联角色ID示该权限属于哪个角色

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField

            ins_table_busi.roleid = obj.get("roleid")
        # 所属系统模块标识权限属于哪个系统模块或功能区域

        if mcauthfield_systemmodule["mcauthchange"]:

            # CharField

            ins_table_busi.systemmodule = obj.get("systemmodule")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_permkwkwissions.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_permkwkwissions.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/permkwkwissions")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_permkwkwissionrolerelations(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 权限角色关联表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制权限是否有效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 权限角色关联表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制权限是否有效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_permkwkwissionrolerelations.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_permkwkwissionrolerelations().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_permkwkwissionrolerelations.objects.filter(**filter)
        else:
            records = mc_permkwkwissionrolerelations.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/permkwkwissionrolerelations.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_permkwkwissionrolerelations()

        # 权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.permkwkwissionid = str(uuid.uuid4())
        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.roleid = str(uuid.uuid4())
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.creatkwkworid = str(uuid.uuid4())
        # 是否激活用于控制权限是否有效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_permkwkwissionrolerelations.objects.get(
            id=obj.get("_id_upd")
        )

        # 权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.permkwkwissionid = str(uuid.uuid4())

            ins_table_busi.permkwkwissionid = str(ins_table_busi.permkwkwissionid)
        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.roleid = str(uuid.uuid4())

            ins_table_busi.roleid = str(ins_table_busi.roleid)
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.creatkwkworid = str(uuid.uuid4())

            ins_table_busi.creatkwkworid = str(ins_table_busi.creatkwkworid)
        # 是否激活用于控制权限是否有效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_permkwkwissionrolerelations.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_permkwkwissionrolerelations.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/permkwkwissionrolerelations")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_systemlogs(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统日志表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_logid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 日志时间

        mcauthfield_logtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作类型

        mcauthfield_action = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模块名称

        mcauthfield_modulename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作结果

        mcauthfield_result = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联ID

        mcauthfield_relatedid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 系统日志表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_logid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 日志时间

        mcauthfield_logtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作类型

        mcauthfield_action = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模块名称

        mcauthfield_modulename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作结果

        mcauthfield_result = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联ID

        mcauthfield_relatedid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_systemlogs.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_systemlogs().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_systemlogs.objects.filter(**filter)
        else:
            records = mc_systemlogs.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_systemlogs_55488 = []
        for m in mc_systemlogs.objects.all():
            mobj = m.toJson()
            data_mc_systemlogs_55488.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("relatedid"),
                }
            )
        return render(request, "config_busi/systemlogs.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_systemlogs()

        # 日志ID

        if mcauthfield_logid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.logid = str(uuid.uuid4())
        # 日志时间

        if mcauthfield_logtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.logtime = obj.get("logtime")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 操作类型

        if mcauthfield_action["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.action = obj.get("action")
        # 模块名称

        if mcauthfield_modulename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.modulename = obj.get("modulename")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 操作结果

        if mcauthfield_result["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.result = obj.get("result")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 关联ID

        if mcauthfield_relatedid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedid = obj.get("relatedid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_systemlogs.objects.get(id=obj.get("_id_upd"))

        # 日志ID

        if mcauthfield_logid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.logid = str(uuid.uuid4())

            ins_table_busi.logid = str(ins_table_busi.logid)
        # 日志时间

        if mcauthfield_logtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.logtime = obj.get("logtime")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 操作类型

        if mcauthfield_action["mcauthchange"]:

            # CharField

            ins_table_busi.action = obj.get("action")
        # 模块名称

        if mcauthfield_modulename["mcauthchange"]:

            # CharField

            ins_table_busi.modulename = obj.get("modulename")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 操作结果

        if mcauthfield_result["mcauthchange"]:

            # CharField

            ins_table_busi.result = obj.get("result")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 关联ID

        if mcauthfield_relatedid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedid = obj.get("relatedid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_systemlogs.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_systemlogs.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/systemlogs")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortconfigurations(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报表配置表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报名称

        mcauthfield_repkwkwortname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告频率

        mcauthfield_frequency = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报表配置表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报名称

        mcauthfield_repkwkwortname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报告频率

        mcauthfield_frequency = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortconfigurations.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortconfigurations().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortconfigurations.objects.filter(**filter)
        else:
            records = mc_repkwkwortconfigurations.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/repkwkwortconfigurations.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortconfigurations()

        # 报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 报名称

        if mcauthfield_repkwkwortname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repkwkwortname = obj.get("repkwkwortname")
        # 报描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 报告频率

        if mcauthfield_frequency["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.frequency = obj.get("frequency")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortconfigurations.objects.get(id=obj.get("_id_upd"))

        # 报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 报名称

        if mcauthfield_repkwkwortname["mcauthchange"]:

            # CharField

            ins_table_busi.repkwkwortname = obj.get("repkwkwortname")
        # 报描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 报告频率

        if mcauthfield_frequency["mcauthchange"]:

            # CharField

            ins_table_busi.frequency = obj.get("frequency")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortconfigurations.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortconfigurations.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortconfigurations")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortexpkwkwortreckwkwords(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报表导出记录表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报ID关联报

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出时间

        mcauthfield_expkwkworttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出用户

        mcauthfield_expkwkwortuser = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出格式如PDF

        mcauthfield_expkwkwortkwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件大小单位KB

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出状态如成功、失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果导出失败

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报表导出记录表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报ID关联报

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出时间

        mcauthfield_expkwkworttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出用户

        mcauthfield_expkwkwortuser = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出格式如PDF

        mcauthfield_expkwkwortkwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件大小单位KB

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 导出状态如成功、失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果导出失败

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortexpkwkwortreckwkwords.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortexpkwkwortreckwkwords().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortexpkwkwortreckwkwords.objects.filter(**filter)
        else:
            records = mc_repkwkwortexpkwkwortreckwkwords.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_weeklyrepkwkworts_55499 = []
        for m in mc_weeklyrepkwkworts.objects.all():
            mobj = m.toJson()
            data_mc_weeklyrepkwkworts_55499.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("repkwkwortcontent"),
                }
            )
        return render(
            request, "config_busi/repkwkwortexpkwkwortreckwkwords.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortexpkwkwortreckwkwords()

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 报ID关联报

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        # 导出时间

        if mcauthfield_expkwkworttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.expkwkworttime = obj.get("expkwkworttime")
        # 导出用户

        if mcauthfield_expkwkwortuser["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.expkwkwortuser = obj.get("expkwkwortuser")
        # 导出格式如PDF

        if mcauthfield_expkwkwortkwkwfkwkwormat["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.expkwkwortkwkwfkwkwormat = obj.get(
                "expkwkwortkwkwfkwkwormat"
            )
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小单位KB

        if mcauthfield_filesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 导出状态如成功、失败

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 错误信息如果导出失败

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortexpkwkwortreckwkwords.objects.get(
            id=obj.get("_id_upd")
        )

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 报ID关联报

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # SelectField

            ins_table_busi.repkwkwortid = obj.get("repkwkwortid")
        # 导出时间

        if mcauthfield_expkwkworttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.expkwkworttime = obj.get("expkwkworttime")
        # 导出用户

        if mcauthfield_expkwkwortuser["mcauthchange"]:

            # CharField

            ins_table_busi.expkwkwortuser = obj.get("expkwkwortuser")
        # 导出格式如PDF

        if mcauthfield_expkwkwortkwkwfkwkwormat["mcauthchange"]:

            # CharField

            ins_table_busi.expkwkwortkwkwfkwkwormat = obj.get(
                "expkwkwortkwkwfkwkwormat"
            )
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save File FileField

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save File FileField

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小单位KB

        if mcauthfield_filesize["mcauthchange"]:

            # Save File FileField

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 导出状态如成功、失败

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 错误信息如果导出失败

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortexpkwkwortreckwkwords.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortexpkwkwortreckwkwords.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortexpkwkwortreckwkwords")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkworttemplatefields(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报表模板字段表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段名称

        mcauthfield_fieldname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段类型

        mcauthfield_fieldtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否必填

        mcauthfield_kwkwisrequired = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 默认值

        mcauthfield_kwkwdefaultvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新人

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报表模板字段表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段名称

        mcauthfield_fieldname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段类型

        mcauthfield_fieldtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否必填

        mcauthfield_kwkwisrequired = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 默认值

        mcauthfield_kwkwdefaultvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新人

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkworttemplatefields.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkworttemplatefields().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkworttemplatefields.objects.filter(**filter)
        else:
            records = mc_repkwkworttemplatefields.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/repkwkworttemplatefields.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkworttemplatefields()

        # 模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.templateid = str(uuid.uuid4())
        # 字段名称

        if mcauthfield_fieldname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.fieldname = obj.get("fieldname")
        # 字段类型

        if mcauthfield_fieldtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.fieldtype = obj.get("fieldtype")
        # 是否必填

        if mcauthfield_kwkwisrequired["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisrequired = obj.get("kwkwisrequired")
        # 默认值

        if mcauthfield_kwkwdefaultvalue["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.kwkwdefaultvalue = obj.get("kwkwdefaultvalue")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        # 创建人

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新人

        if mcauthfield_updatedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.updatedby = obj.get("updatedby")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkworttemplatefields.objects.get(id=obj.get("_id_upd"))

        # 模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.templateid = str(uuid.uuid4())

            ins_table_busi.templateid = str(ins_table_busi.templateid)
        # 字段名称

        if mcauthfield_fieldname["mcauthchange"]:

            # CharField

            ins_table_busi.fieldname = obj.get("fieldname")
        # 字段类型

        if mcauthfield_fieldtype["mcauthchange"]:

            # CharField

            ins_table_busi.fieldtype = obj.get("fieldtype")
        # 是否必填

        if mcauthfield_kwkwisrequired["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisrequired = obj.get("kwkwisrequired")
        # 默认值

        if mcauthfield_kwkwdefaultvalue["mcauthchange"]:

            # CharField

            ins_table_busi.kwkwdefaultvalue = obj.get("kwkwdefaultvalue")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        # 创建人

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新人

        if mcauthfield_updatedby["mcauthchange"]:

            # CharField

            ins_table_busi.updatedby = obj.get("updatedby")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkworttemplatefields.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkworttemplatefields.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkworttemplatefields")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortfieldtypes(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报表字段类型表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报字段类型ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段名称

        mcauthfield_fieldname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段类型如VARCHAR

        mcauthfield_fieldtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大长度针对类型

        mcauthfield_maxlength = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否可为空是否

        mcauthfield_kwkwisnullable = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 默认值

        mcauthfield_kwkwdefaultvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新人ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报表字段类型表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报字段类型ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段名称

        mcauthfield_fieldname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段类型如VARCHAR

        mcauthfield_fieldtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大长度针对类型

        mcauthfield_maxlength = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否可为空是否

        mcauthfield_kwkwisnullable = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 默认值

        mcauthfield_kwkwdefaultvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 字段描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新人ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortfieldtypes.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortfieldtypes().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortfieldtypes.objects.filter(**filter)
        else:
            records = mc_repkwkwortfieldtypes.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/repkwkwortfieldtypes.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortfieldtypes()

        # 报字段类型ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 字段名称

        if mcauthfield_fieldname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.fieldname = obj.get("fieldname")
        # 字段类型如VARCHAR

        if mcauthfield_fieldtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.fieldtype = obj.get("fieldtype")
        # 最大长度针对类型

        if mcauthfield_maxlength["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.maxlength = obj.get("maxlength")
        # 是否可为空是否

        if mcauthfield_kwkwisnullable["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisnullable = obj.get("kwkwisnullable")
        # 默认值

        if mcauthfield_kwkwdefaultvalue["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.kwkwdefaultvalue = obj.get("kwkwdefaultvalue")
        # 字段描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建人ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.createdby = str(uuid.uuid4())
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新人ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.updatedby = str(uuid.uuid4())
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortfieldtypes.objects.get(id=obj.get("_id_upd"))

        # 报字段类型ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 字段名称

        if mcauthfield_fieldname["mcauthchange"]:

            # CharField

            ins_table_busi.fieldname = obj.get("fieldname")
        # 字段类型如VARCHAR

        if mcauthfield_fieldtype["mcauthchange"]:

            # CharField

            ins_table_busi.fieldtype = obj.get("fieldtype")
        # 最大长度针对类型

        if mcauthfield_maxlength["mcauthchange"]:

            # CharField

            ins_table_busi.maxlength = obj.get("maxlength")
        # 是否可为空是否

        if mcauthfield_kwkwisnullable["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisnullable = obj.get("kwkwisnullable")
        # 默认值

        if mcauthfield_kwkwdefaultvalue["mcauthchange"]:

            # CharField

            ins_table_busi.kwkwdefaultvalue = obj.get("kwkwdefaultvalue")
        # 字段描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建人ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.createdby = str(uuid.uuid4())

            ins_table_busi.createdby = str(ins_table_busi.createdby)
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新人ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.updatedby = str(uuid.uuid4())

            ins_table_busi.updatedby = str(ins_table_busi.updatedby)
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortfieldtypes.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortfieldtypes.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortfieldtypes")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_repkwkwortdata(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报表数据表 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报名称

        mcauthfield_repkwkwortname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报日期

        mcauthfield_repkwkwortdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门

        mcauthfield_department = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 附件路径

        mcauthfield_attachment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID

        mcauthfield_relateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报表数据表 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 报ID

        mcauthfield_repkwkwortid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报名称

        mcauthfield_repkwkwortname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报日期

        mcauthfield_repkwkwortdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门

        mcauthfield_department = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 附件路径

        mcauthfield_attachment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID

        mcauthfield_relateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_repkwkwortdata.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_repkwkwortdata().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_repkwkwortdata.objects.filter(**filter)
        else:
            records = mc_repkwkwortdata.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_users_55539 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_55539.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/repkwkwortdata.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_repkwkwortdata()

        # 报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repkwkwortid = str(uuid.uuid4())
        # 报名称

        if mcauthfield_repkwkwortname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repkwkwortname = obj.get("repkwkwortname")
        # 报日期

        if mcauthfield_repkwkwortdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.repkwkwortdate = obj.get("repkwkwortdate")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 部门

        if mcauthfield_department["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.department = obj.get("department")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 报内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 附件路径

        if mcauthfield_attachment["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "attachment" in request.FILES:
                ins_table_busi.attachment = request.FILES["attachment"]
        # 最后更新时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 关联用户ID

        if mcauthfield_relateduserid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relateduserid = obj.get("relateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_repkwkwortdata.objects.get(id=obj.get("_id_upd"))

        # 报ID

        if mcauthfield_repkwkwortid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repkwkwortid = str(uuid.uuid4())

            ins_table_busi.repkwkwortid = str(ins_table_busi.repkwkwortid)
        # 报名称

        if mcauthfield_repkwkwortname["mcauthchange"]:

            # CharField

            ins_table_busi.repkwkwortname = obj.get("repkwkwortname")
        # 报日期

        if mcauthfield_repkwkwortdate["mcauthchange"]:

            # DateField

            ins_table_busi.repkwkwortdate = obj.get("repkwkwortdate")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 部门

        if mcauthfield_department["mcauthchange"]:

            # CharField

            ins_table_busi.department = obj.get("department")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 报内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 附件路径

        if mcauthfield_attachment["mcauthchange"]:

            # Save File FileField

            if "attachment" in request.FILES:
                ins_table_busi.attachment = request.FILES["attachment"]
        # 最后更新时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 关联用户ID

        if mcauthfield_relateduserid["mcauthchange"]:

            # SelectField

            ins_table_busi.relateduserid = obj.get("relateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_repkwkwortdata.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_repkwkwortdata.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/repkwkwortdata")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_supermanager(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统管理员 系统管理员(8127)

    if user_table_id == str(8127):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 系统管理员 用户表(8094)

    if user_table_id == str(8094):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_supermanager.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_supermanager().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_supermanager.objects.filter(**filter)
        else:
            records = mc_supermanager.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/supermanager.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_supermanager()

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id_upd"))

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/supermanager")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


def auto_detect(request):
    if request.method == "GET":
        detect = False

        return render(request, "config_algorithm/auto_detect.html", locals())
    obj = mydict(request.POST)

    if "img" not in request.FILES:
        return HttpResponse("请上传图片")
    img = request.FILES["img"]
    # mc_

    detect = True

    detect_result = "算法结果展示"

    # 保存提交的内容
    # 保存分析的结果
    # 若源码中缺少需要的表和字段.联系 qq952934650

    return render(request, "config_algorithm/auto_detect.html", locals())
