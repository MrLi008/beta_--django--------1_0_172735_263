from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from sys_user.func import *

# 词云

from a_simulink_unit.generate_wordcloud import generate_wordcloud_base64

# Create your views here.


def index(request):

    return render(request, "config_visual/index.html", locals())


"""

# 系统中所有数据表名/中英文+字段中英文
用于快速创建查询语句和分析
测试通过后删除此段.
__deprected__ mark_appcenter_views_all_tables_and_fields
__deprected__ mark_appcenter_views_all_tables_and__two_field_fields
# 根据需要按照表结构和csv文件依次导入数据库.
"""


def bi(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    # users(用户表)->userid(用户ID)

    if obj.get("optype") == "users.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.users group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "users.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.users group by userid",
            "用户ID",
        )
    if obj.get("optype") == "users.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.users group by userid",
            "用户ID",
        )
    if obj.get("optype") == "users.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.users group by userid",
            "用户ID",
        )
    if obj.get("optype") == "users.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.users group by userid",
            "用户ID",
        )
    if obj.get("optype") == "users.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.users group by userid",
            "用户ID",
        )
    # users(用户表)->username(用户名)

    if obj.get("optype") == "users.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm779_2f88e95faa233d77.users group by username order by x desc",
            "用户名",
        )
    if obj.get("optype") == "users.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm779_2f88e95faa233d77.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm779_2f88e95faa233d77.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_line":
        res = get_line(
            "select username x,count(*) y from vm779_2f88e95faa233d77.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm779_2f88e95faa233d77.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm779_2f88e95faa233d77.users group by username",
            "用户名",
        )
    # users(用户表)->useremail(用户邮箱)

    if obj.get("optype") == "users.useremail_pie":
        res = get_pie(
            "select useremail x,count(*) y from vm779_2f88e95faa233d77.users group by useremail order by x desc",
            "用户邮箱",
        )
    if obj.get("optype") == "users.useremail_pie_v1":
        res = get_pie_v1(
            "select useremail x,count(*) y from vm779_2f88e95faa233d77.users group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "users.useremail_pie_v2":
        res = get_pie_v2(
            "select useremail x,count(*) y from vm779_2f88e95faa233d77.users group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "users.useremail_line":
        res = get_line(
            "select useremail x,count(*) y from vm779_2f88e95faa233d77.users group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "users.useremail_bar":
        res = get_bar(
            "select useremail x,count(*) y from vm779_2f88e95faa233d77.users group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "users.useremail_bar_v1":
        res = get_bar_v1(
            "select useremail x,count(*) y from vm779_2f88e95faa233d77.users group by useremail",
            "用户邮箱",
        )
    # users(用户表)->userpkwkwasswkwkword(用户密码)

    if obj.get("optype") == "users.userpkwkwasswkwkword_pie":
        res = get_pie(
            "select userpkwkwasswkwkword x,count(*) y from vm779_2f88e95faa233d77.users group by userpkwkwasswkwkword order by x desc",
            "用户密码",
        )
    if obj.get("optype") == "users.userpkwkwasswkwkword_pie_v1":
        res = get_pie_v1(
            "select userpkwkwasswkwkword x,count(*) y from vm779_2f88e95faa233d77.users group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "users.userpkwkwasswkwkword_pie_v2":
        res = get_pie_v2(
            "select userpkwkwasswkwkword x,count(*) y from vm779_2f88e95faa233d77.users group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "users.userpkwkwasswkwkword_line":
        res = get_line(
            "select userpkwkwasswkwkword x,count(*) y from vm779_2f88e95faa233d77.users group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "users.userpkwkwasswkwkword_bar":
        res = get_bar(
            "select userpkwkwasswkwkword x,count(*) y from vm779_2f88e95faa233d77.users group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "users.userpkwkwasswkwkword_bar_v1":
        res = get_bar_v1(
            "select userpkwkwasswkwkword x,count(*) y from vm779_2f88e95faa233d77.users group by userpkwkwasswkwkword",
            "用户密码",
        )
    # users(用户表)->userrole(用户角色)

    if obj.get("optype") == "users.userrole_pie":
        res = get_pie(
            "select userrole x,count(*) y from vm779_2f88e95faa233d77.users group by userrole order by x desc",
            "用户角色",
        )
    if obj.get("optype") == "users.userrole_pie_v1":
        res = get_pie_v1(
            "select userrole x,count(*) y from vm779_2f88e95faa233d77.users group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "users.userrole_pie_v2":
        res = get_pie_v2(
            "select userrole x,count(*) y from vm779_2f88e95faa233d77.users group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "users.userrole_line":
        res = get_line(
            "select userrole x,count(*) y from vm779_2f88e95faa233d77.users group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "users.userrole_bar":
        res = get_bar(
            "select userrole x,count(*) y from vm779_2f88e95faa233d77.users group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "users.userrole_bar_v1":
        res = get_bar_v1(
            "select userrole x,count(*) y from vm779_2f88e95faa233d77.users group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "users.createdate_line":
        res = get_line(
            "select createdate x,count(*) y from vm779_2f88e95faa233d77.users group by createdate order by x",
            "创建日期",
        )
    if obj.get("optype") == "users.lkwkwastlogkwkwindate_line":
        res = get_line(
            "select lkwkwastlogkwkwindate x,count(*) y from vm779_2f88e95faa233d77.users group by lkwkwastlogkwkwindate order by x",
            "最后登录日期",
        )
    # users(用户表)->isactive(是否活跃)

    if obj.get("optype") == "users.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.users group by isactive order by x desc",
            "是否活跃",
        )
    if obj.get("optype") == "users.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.users group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "users.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.users group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "users.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.users group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "users.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.users group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "users.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.users group by isactive",
            "是否活跃",
        )
    # users(用户表)->departmentid(部门ID关联字段)

    if obj.get("optype") == "users.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.users group by departmentid order by x desc",
            "部门ID关联字段",
        )
    if obj.get("optype") == "users.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.users group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "users.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.users group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "users.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.users group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "users.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.users group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "users.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.users group by departmentid",
            "部门ID关联字段",
        )
    # roles(角色表)->roleid(角色ID)

    if obj.get("optype") == "roles.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.roles group by roleid order by x desc",
            "角色ID",
        )
    if obj.get("optype") == "roles.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.roles group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roles.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.roles group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roles.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.roles group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roles.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.roles group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roles.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.roles group by roleid",
            "角色ID",
        )
    # roles(角色表)->rolename(角色名称)

    if obj.get("optype") == "roles.rolename_pie":
        res = get_pie(
            "select rolename x,count(*) y from vm779_2f88e95faa233d77.roles group by rolename order by x desc",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_pie_v1":
        res = get_pie_v1(
            "select rolename x,count(*) y from vm779_2f88e95faa233d77.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_pie_v2":
        res = get_pie_v2(
            "select rolename x,count(*) y from vm779_2f88e95faa233d77.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_line":
        res = get_line(
            "select rolename x,count(*) y from vm779_2f88e95faa233d77.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_bar":
        res = get_bar(
            "select rolename x,count(*) y from vm779_2f88e95faa233d77.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_bar_v1":
        res = get_bar_v1(
            "select rolename x,count(*) y from vm779_2f88e95faa233d77.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.roledescription_wordcloud":
        textlist = get_data(
            "SELECT roledescription result FROM vm779_2f88e95faa233d77.roles;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "roles.createdtime_line":
        res = get_line(
            "select createdtime x,count(*) y from vm779_2f88e95faa233d77.roles group by createdtime order by x",
            "创建时间",
        )
    # roles(角色表)->createdby(创建者ID)

    if obj.get("optype") == "roles.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.roles group by createdby order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "roles.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.roles group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "roles.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.roles group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "roles.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.roles group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "roles.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.roles group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "roles.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.roles group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "roles.updatedtime_line":
        res = get_line(
            "select updatedtime x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedtime order by x",
            "更新时间",
        )
    # roles(角色表)->updatedby(更新者ID)

    if obj.get("optype") == "roles.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedby order by x desc",
            "更新者ID",
        )
    if obj.get("optype") == "roles.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "roles.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "roles.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "roles.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "roles.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.roles group by updatedby",
            "更新者ID",
        )
    # roles(角色表)->isactive(是否激活)

    if obj.get("optype") == "roles.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.roles group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "roles.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.roles group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roles.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.roles group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roles.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.roles group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roles.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.roles group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roles.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.roles group by isactive",
            "是否激活",
        )
    # roles(角色表)->departmentid(部门ID关联字段指向部门的ID)

    if obj.get("optype") == "roles.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.roles group by departmentid order by x desc",
            "部门ID关联字段指向部门的ID",
        )
    if obj.get("optype") == "roles.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.roles group by departmentid",
            "部门ID关联字段指向部门的ID",
        )
    if obj.get("optype") == "roles.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.roles group by departmentid",
            "部门ID关联字段指向部门的ID",
        )
    if obj.get("optype") == "roles.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.roles group by departmentid",
            "部门ID关联字段指向部门的ID",
        )
    if obj.get("optype") == "roles.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.roles group by departmentid",
            "部门ID关联字段指向部门的ID",
        )
    if obj.get("optype") == "roles.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.roles group by departmentid",
            "部门ID关联字段指向部门的ID",
        )
    # userrolerelations(用户角色关联表)->userid(用户ID)

    if obj.get("optype") == "userrolerelations.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelations.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelations.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelations.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelations.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelations.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by userid",
            "用户ID",
        )
    # userrolerelations(用户角色关联表)->roleid(角色ID)

    if obj.get("optype") == "userrolerelations.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by roleid order by x desc",
            "角色ID",
        )
    if obj.get("optype") == "userrolerelations.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userrolerelations.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userrolerelations.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userrolerelations.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userrolerelations.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userrolerelations.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "userrolerelations.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by updatetime order by x",
            "更新时间",
        )
    # userrolerelations(用户角色关联表)->kwkwisactive(是否激活用于标记该关联是否有效)

    if obj.get("optype") == "userrolerelations.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by kwkwisactive order by x desc",
            "是否激活用于标记该关联是否有效",
        )
    if obj.get("optype") == "userrolerelations.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by kwkwisactive",
            "是否激活用于标记该关联是否有效",
        )
    if obj.get("optype") == "userrolerelations.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by kwkwisactive",
            "是否激活用于标记该关联是否有效",
        )
    if obj.get("optype") == "userrolerelations.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by kwkwisactive",
            "是否激活用于标记该关联是否有效",
        )
    if obj.get("optype") == "userrolerelations.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by kwkwisactive",
            "是否激活用于标记该关联是否有效",
        )
    if obj.get("optype") == "userrolerelations.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by kwkwisactive",
            "是否激活用于标记该关联是否有效",
        )
    # userrolerelations(用户角色关联表)->creatkwkworid(创建者ID)

    if obj.get("optype") == "userrolerelations.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by creatkwkworid order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelations.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelations.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelations.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelations.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelations.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by creatkwkworid",
            "创建者ID",
        )
    # userrolerelations(用户角色关联表)->lkwkwastmodkwkwifierid(最后修改者ID)

    if obj.get("optype") == "userrolerelations.lkwkwastmodkwkwifierid_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by lkwkwastmodkwkwifierid order by x desc",
            "最后修改者ID",
        )
    if obj.get("optype") == "userrolerelations.lkwkwastmodkwkwifierid_pie_v1":
        res = get_pie_v1(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by lkwkwastmodkwkwifierid",
            "最后修改者ID",
        )
    if obj.get("optype") == "userrolerelations.lkwkwastmodkwkwifierid_pie_v2":
        res = get_pie_v2(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by lkwkwastmodkwkwifierid",
            "最后修改者ID",
        )
    if obj.get("optype") == "userrolerelations.lkwkwastmodkwkwifierid_line":
        res = get_line(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by lkwkwastmodkwkwifierid",
            "最后修改者ID",
        )
    if obj.get("optype") == "userrolerelations.lkwkwastmodkwkwifierid_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by lkwkwastmodkwkwifierid",
            "最后修改者ID",
        )
    if obj.get("optype") == "userrolerelations.lkwkwastmodkwkwifierid_bar_v1":
        res = get_bar_v1(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.userrolerelations group by lkwkwastmodkwkwifierid",
            "最后修改者ID",
        )
    # weeklyrepkwkworttemplates(周报模板表)->templateid(模板ID)

    if obj.get("optype") == "weeklyrepkwkworttemplates.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templateid order by x desc",
            "模板ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templateid",
            "模板ID",
        )
    # weeklyrepkwkworttemplates(周报模板表)->templatename(模板名称)

    if obj.get("optype") == "weeklyrepkwkworttemplates.templatename_pie":
        res = get_pie(
            "select templatename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templatename order by x desc",
            "模板名称",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templatename_pie_v1":
        res = get_pie_v1(
            "select templatename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templatename_pie_v2":
        res = get_pie_v2(
            "select templatename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templatename_line":
        res = get_line(
            "select templatename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templatename_bar":
        res = get_bar(
            "select templatename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.templatename_bar_v1":
        res = get_bar_v1(
            "select templatename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.weeklyrepkwkworttemplates;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # weeklyrepkwkworttemplates(周报模板表)->creatkwkwor(创建者)

    if obj.get("optype") == "weeklyrepkwkworttemplates.creatkwkwor_pie":
        res = get_pie(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creatkwkwor order by x desc",
            "创建者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.creatkwkwor_pie_v1":
        res = get_pie_v1(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.creatkwkwor_pie_v2":
        res = get_pie_v2(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.creatkwkwor_line":
        res = get_line(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.creatkwkwor_bar":
        res = get_bar(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.creatkwkwor_bar_v1":
        res = get_bar_v1(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.creationdate_line":
        res = get_line(
            "select creationdate x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by creationdate order by x",
            "创建日期",
        )
    # weeklyrepkwkworttemplates(周报模板表)->lkwkwastmodkwkwifier(最后修改者)

    if obj.get("optype") == "weeklyrepkwkworttemplates.lkwkwastmodkwkwifier_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifier x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwifier order by x desc",
            "最后修改者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.lkwkwastmodkwkwifier_pie_v1":
        res = get_pie_v1(
            "select lkwkwastmodkwkwifier x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwifier",
            "最后修改者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.lkwkwastmodkwkwifier_pie_v2":
        res = get_pie_v2(
            "select lkwkwastmodkwkwifier x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwifier",
            "最后修改者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.lkwkwastmodkwkwifier_line":
        res = get_line(
            "select lkwkwastmodkwkwifier x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwifier",
            "最后修改者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.lkwkwastmodkwkwifier_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifier x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwifier",
            "最后修改者",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.lkwkwastmodkwkwifier_bar_v1":
        res = get_bar_v1(
            "select lkwkwastmodkwkwifier x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwifier",
            "最后修改者",
        )
    if (
        obj.get("optype")
        == "weeklyrepkwkworttemplates.lkwkwastmodkwkwificationdate_line"
    ):
        res = get_line(
            "select lkwkwastmodkwkwificationdate x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by lkwkwastmodkwkwificationdate order by x",
            "最后修改日期",
        )
    # weeklyrepkwkworttemplates(周报模板表)->isactive(是否激活)

    if obj.get("optype") == "weeklyrepkwkworttemplates.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by isactive",
            "是否激活",
        )
    # weeklyrepkwkworttemplates(周报模板表)->departmentid(部门ID)

    if obj.get("optype") == "weeklyrepkwkworttemplates.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by departmentid order by x desc",
            "部门ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "weeklyrepkwkworttemplates.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworttemplates group by departmentid",
            "部门ID",
        )
    # weeklyrepkwkworts(周报表)->repkwkwortid(报ID)

    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by repkwkwortid order by x desc",
            "报ID",
        )
    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "weeklyrepkwkworts.weekstartdate_line":
        res = get_line(
            "select weekstartdate x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by weekstartdate order by x",
            "周开始日期",
        )
    if obj.get("optype") == "weeklyrepkwkworts.weekenddate_line":
        res = get_line(
            "select weekenddate x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by weekenddate order by x",
            "周结束日期",
        )
    # weeklyrepkwkworts(周报表)->department(部门)

    if obj.get("optype") == "weeklyrepkwkworts.department_pie":
        res = get_pie(
            "select department x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by department order by x desc",
            "部门",
        )
    if obj.get("optype") == "weeklyrepkwkworts.department_pie_v1":
        res = get_pie_v1(
            "select department x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by department",
            "部门",
        )
    if obj.get("optype") == "weeklyrepkwkworts.department_pie_v2":
        res = get_pie_v2(
            "select department x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by department",
            "部门",
        )
    if obj.get("optype") == "weeklyrepkwkworts.department_line":
        res = get_line(
            "select department x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by department",
            "部门",
        )
    if obj.get("optype") == "weeklyrepkwkworts.department_bar":
        res = get_bar(
            "select department x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by department",
            "部门",
        )
    if obj.get("optype") == "weeklyrepkwkworts.department_bar_v1":
        res = get_bar_v1(
            "select department x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by department",
            "部门",
        )
    # weeklyrepkwkworts(周报表)->employeename(员工姓名)

    if obj.get("optype") == "weeklyrepkwkworts.employeename_pie":
        res = get_pie(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by employeename order by x desc",
            "员工姓名",
        )
    if obj.get("optype") == "weeklyrepkwkworts.employeename_pie_v1":
        res = get_pie_v1(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "weeklyrepkwkworts.employeename_pie_v2":
        res = get_pie_v2(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "weeklyrepkwkworts.employeename_line":
        res = get_line(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "weeklyrepkwkworts.employeename_bar":
        res = get_bar(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "weeklyrepkwkworts.employeename_bar_v1":
        res = get_bar_v1(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "weeklyrepkwkworts.repkwkwortcontent_wordcloud":
        textlist = get_data(
            "SELECT repkwkwortcontent result FROM vm779_2f88e95faa233d77.weeklyrepkwkworts;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # weeklyrepkwkworts(周报表)->status(状态)

    if obj.get("optype") == "weeklyrepkwkworts.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "weeklyrepkwkworts.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by status",
            "状态",
        )
    if obj.get("optype") == "weeklyrepkwkworts.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by status",
            "状态",
        )
    if obj.get("optype") == "weeklyrepkwkworts.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by status",
            "状态",
        )
    if obj.get("optype") == "weeklyrepkwkworts.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by status",
            "状态",
        )
    if obj.get("optype") == "weeklyrepkwkworts.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by status",
            "状态",
        )
    if obj.get("optype") == "weeklyrepkwkworts.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "weeklyrepkwkworts.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.weeklyrepkwkworts group by updatedat order by x",
            "更新时间",
        )
    # repkwkwortperiods(报告周期表)->repkwkwortperiodid(报告周期ID)

    if obj.get("optype") == "repkwkwortperiods.repkwkwortperiodid_pie":
        res = get_pie(
            "select repkwkwortperiodid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by repkwkwortperiodid order by x desc",
            "报告周期ID",
        )
    if obj.get("optype") == "repkwkwortperiods.repkwkwortperiodid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortperiodid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by repkwkwortperiodid",
            "报告周期ID",
        )
    if obj.get("optype") == "repkwkwortperiods.repkwkwortperiodid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortperiodid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by repkwkwortperiodid",
            "报告周期ID",
        )
    if obj.get("optype") == "repkwkwortperiods.repkwkwortperiodid_line":
        res = get_line(
            "select repkwkwortperiodid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by repkwkwortperiodid",
            "报告周期ID",
        )
    if obj.get("optype") == "repkwkwortperiods.repkwkwortperiodid_bar":
        res = get_bar(
            "select repkwkwortperiodid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by repkwkwortperiodid",
            "报告周期ID",
        )
    if obj.get("optype") == "repkwkwortperiods.repkwkwortperiodid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortperiodid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by repkwkwortperiodid",
            "报告周期ID",
        )
    # repkwkwortperiods(报告周期表)->periodname(周期名称)

    if obj.get("optype") == "repkwkwortperiods.periodname_pie":
        res = get_pie(
            "select periodname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by periodname order by x desc",
            "周期名称",
        )
    if obj.get("optype") == "repkwkwortperiods.periodname_pie_v1":
        res = get_pie_v1(
            "select periodname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by periodname",
            "周期名称",
        )
    if obj.get("optype") == "repkwkwortperiods.periodname_pie_v2":
        res = get_pie_v2(
            "select periodname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by periodname",
            "周期名称",
        )
    if obj.get("optype") == "repkwkwortperiods.periodname_line":
        res = get_line(
            "select periodname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by periodname",
            "周期名称",
        )
    if obj.get("optype") == "repkwkwortperiods.periodname_bar":
        res = get_bar(
            "select periodname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by periodname",
            "周期名称",
        )
    if obj.get("optype") == "repkwkwortperiods.periodname_bar_v1":
        res = get_bar_v1(
            "select periodname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by periodname",
            "周期名称",
        )
    if obj.get("optype") == "repkwkwortperiods.startdate_line":
        res = get_line(
            "select startdate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by startdate order by x",
            "开始日期",
        )
    if obj.get("optype") == "repkwkwortperiods.enddate_line":
        res = get_line(
            "select enddate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by enddate order by x",
            "结束日期",
        )
    # repkwkwortperiods(报告周期表)->isactive(是否活跃用于标记当前周期是否还在使用中)

    if obj.get("optype") == "repkwkwortperiods.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by isactive order by x desc",
            "是否活跃用于标记当前周期是否还在使用中",
        )
    if obj.get("optype") == "repkwkwortperiods.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by isactive",
            "是否活跃用于标记当前周期是否还在使用中",
        )
    if obj.get("optype") == "repkwkwortperiods.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by isactive",
            "是否活跃用于标记当前周期是否还在使用中",
        )
    if obj.get("optype") == "repkwkwortperiods.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by isactive",
            "是否活跃用于标记当前周期是否还在使用中",
        )
    if obj.get("optype") == "repkwkwortperiods.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by isactive",
            "是否活跃用于标记当前周期是否还在使用中",
        )
    if obj.get("optype") == "repkwkwortperiods.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by isactive",
            "是否活跃用于标记当前周期是否还在使用中",
        )
    # repkwkwortperiods(报告周期表)->createdby(创建者记录创建该周期的用户)

    if obj.get("optype") == "repkwkwortperiods.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by createdby order by x desc",
            "创建者记录创建该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by createdby",
            "创建者记录创建该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by createdby",
            "创建者记录创建该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by createdby",
            "创建者记录创建该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by createdby",
            "创建者记录创建该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by createdby",
            "创建者记录创建该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.creationdate_line":
        res = get_line(
            "select creationdate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by creationdate order by x",
            "创建日期",
        )
    # repkwkwortperiods(报告周期表)->lkwkwastmodkwkwifiedby(最后修改者记录最后修改该周期的用户)

    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifiedby_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifiedby order by x desc",
            "最后修改者记录最后修改该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifiedby_pie_v1":
        res = get_pie_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifiedby",
            "最后修改者记录最后修改该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifiedby_pie_v2":
        res = get_pie_v2(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifiedby",
            "最后修改者记录最后修改该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifiedby_line":
        res = get_line(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifiedby",
            "最后修改者记录最后修改该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifiedby_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifiedby",
            "最后修改者记录最后修改该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifiedby_bar_v1":
        res = get_bar_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifiedby",
            "最后修改者记录最后修改该周期的用户",
        )
    if obj.get("optype") == "repkwkwortperiods.lkwkwastmodkwkwifieddate_line":
        res = get_line(
            "select lkwkwastmodkwkwifieddate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortperiods group by lkwkwastmodkwkwifieddate order by x",
            "最后修改日期",
        )
    # repkwkwortstatuses(报告状态表)->repkwkwortstatusid(报告状态ID)

    if obj.get("optype") == "repkwkwortstatuses.repkwkwortstatusid_pie":
        res = get_pie(
            "select repkwkwortstatusid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortstatusid order by x desc",
            "报告状态ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortstatusid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortstatusid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortstatusid",
            "报告状态ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortstatusid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortstatusid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortstatusid",
            "报告状态ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortstatusid_line":
        res = get_line(
            "select repkwkwortstatusid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortstatusid",
            "报告状态ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortstatusid_bar":
        res = get_bar(
            "select repkwkwortstatusid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortstatusid",
            "报告状态ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortstatusid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortstatusid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortstatusid",
            "报告状态ID",
        )
    # repkwkwortstatuses(报告状态表)->statusname(状态名称)

    if obj.get("optype") == "repkwkwortstatuses.statusname_pie":
        res = get_pie(
            "select statusname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by statusname order by x desc",
            "状态名称",
        )
    if obj.get("optype") == "repkwkwortstatuses.statusname_pie_v1":
        res = get_pie_v1(
            "select statusname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "repkwkwortstatuses.statusname_pie_v2":
        res = get_pie_v2(
            "select statusname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "repkwkwortstatuses.statusname_line":
        res = get_line(
            "select statusname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "repkwkwortstatuses.statusname_bar":
        res = get_bar(
            "select statusname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "repkwkwortstatuses.statusname_bar_v1":
        res = get_bar_v1(
            "select statusname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "repkwkwortstatuses.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.repkwkwortstatuses;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "repkwkwortstatuses.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "repkwkwortstatuses.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by updatedat order by x",
            "更新时间",
        )
    # repkwkwortstatuses(报告状态表)->isactive(是否激活)

    if obj.get("optype") == "repkwkwortstatuses.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortstatuses.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortstatuses.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortstatuses.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortstatuses.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortstatuses.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isactive",
            "是否激活",
        )
    # repkwkwortstatuses(报告状态表)->isdefault(是否为默认状态)

    if obj.get("optype") == "repkwkwortstatuses.isdefault_pie":
        res = get_pie(
            "select isdefault x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isdefault order by x desc",
            "是否为默认状态",
        )
    if obj.get("optype") == "repkwkwortstatuses.isdefault_pie_v1":
        res = get_pie_v1(
            "select isdefault x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isdefault",
            "是否为默认状态",
        )
    if obj.get("optype") == "repkwkwortstatuses.isdefault_pie_v2":
        res = get_pie_v2(
            "select isdefault x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isdefault",
            "是否为默认状态",
        )
    if obj.get("optype") == "repkwkwortstatuses.isdefault_line":
        res = get_line(
            "select isdefault x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isdefault",
            "是否为默认状态",
        )
    if obj.get("optype") == "repkwkwortstatuses.isdefault_bar":
        res = get_bar(
            "select isdefault x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isdefault",
            "是否为默认状态",
        )
    if obj.get("optype") == "repkwkwortstatuses.isdefault_bar_v1":
        res = get_bar_v1(
            "select isdefault x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by isdefault",
            "是否为默认状态",
        )
    # repkwkwortstatuses(报告状态表)->skwkwortorder(排序顺序)

    if obj.get("optype") == "repkwkwortstatuses.skwkwortorder_pie":
        res = get_pie(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by skwkwortorder order by x desc",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkwortstatuses.skwkwortorder_pie_v1":
        res = get_pie_v1(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkwortstatuses.skwkwortorder_pie_v2":
        res = get_pie_v2(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkwortstatuses.skwkwortorder_line":
        res = get_line(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkwortstatuses.skwkwortorder_bar":
        res = get_bar(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkwortstatuses.skwkwortorder_bar_v1":
        res = get_bar_v1(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by skwkwortorder",
            "排序顺序",
        )
    # repkwkwortstatuses(报告状态表)->repkwkwortid(关联报告ID指向报告的ID)

    if obj.get("optype") == "repkwkwortstatuses.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortid order by x desc",
            "关联报告ID指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortid",
            "关联报告ID指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortid",
            "关联报告ID指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortid",
            "关联报告ID指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortid",
            "关联报告ID指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortstatuses.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortstatuses group by repkwkwortid",
            "关联报告ID指向报告的ID",
        )
    # repkwkworttypes(报告类型表)->repkwkworttypeid(报告类型ID)

    if obj.get("optype") == "repkwkworttypes.repkwkworttypeid_pie":
        res = get_pie(
            "select repkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypeid order by x desc",
            "报告类型ID",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypeid_pie_v1":
        res = get_pie_v1(
            "select repkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypeid",
            "报告类型ID",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypeid_pie_v2":
        res = get_pie_v2(
            "select repkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypeid",
            "报告类型ID",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypeid_line":
        res = get_line(
            "select repkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypeid",
            "报告类型ID",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypeid_bar":
        res = get_bar(
            "select repkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypeid",
            "报告类型ID",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypeid_bar_v1":
        res = get_bar_v1(
            "select repkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypeid",
            "报告类型ID",
        )
    # repkwkworttypes(报告类型表)->repkwkworttypename(报告类型名称)

    if obj.get("optype") == "repkwkworttypes.repkwkworttypename_pie":
        res = get_pie(
            "select repkwkworttypename x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypename order by x desc",
            "报告类型名称",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypename_pie_v1":
        res = get_pie_v1(
            "select repkwkworttypename x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypename",
            "报告类型名称",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypename_pie_v2":
        res = get_pie_v2(
            "select repkwkworttypename x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypename",
            "报告类型名称",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypename_line":
        res = get_line(
            "select repkwkworttypename x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypename",
            "报告类型名称",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypename_bar":
        res = get_bar(
            "select repkwkworttypename x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypename",
            "报告类型名称",
        )
    if obj.get("optype") == "repkwkworttypes.repkwkworttypename_bar_v1":
        res = get_bar_v1(
            "select repkwkworttypename x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by repkwkworttypename",
            "报告类型名称",
        )
    if obj.get("optype") == "repkwkworttypes.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.repkwkworttypes;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkworttypes(报告类型表)->isactive(是否激活用于控制该报告类型是否可用)

    if obj.get("optype") == "repkwkworttypes.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by isactive order by x desc",
            "是否激活用于控制该报告类型是否可用",
        )
    if obj.get("optype") == "repkwkworttypes.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by isactive",
            "是否激活用于控制该报告类型是否可用",
        )
    if obj.get("optype") == "repkwkworttypes.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by isactive",
            "是否激活用于控制该报告类型是否可用",
        )
    if obj.get("optype") == "repkwkworttypes.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by isactive",
            "是否激活用于控制该报告类型是否可用",
        )
    if obj.get("optype") == "repkwkworttypes.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by isactive",
            "是否激活用于控制该报告类型是否可用",
        )
    if obj.get("optype") == "repkwkworttypes.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by isactive",
            "是否激活用于控制该报告类型是否可用",
        )
    if obj.get("optype") == "repkwkworttypes.createddate_line":
        res = get_line(
            "select createddate x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createddate order by x",
            "创建日期",
        )
    # repkwkworttypes(报告类型表)->createdby(创建者ID关联用户)

    if obj.get("optype") == "repkwkworttypes.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createdby order by x desc",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createdby",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createdby",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createdby",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createdby",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by createdby",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.modkwkwifieddate_line":
        res = get_line(
            "select modkwkwifieddate x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifieddate order by x",
            "修改日期",
        )
    # repkwkworttypes(报告类型表)->modkwkwifiedby(修改者ID关联用户)

    if obj.get("optype") == "repkwkworttypes.modkwkwifiedby_pie":
        res = get_pie(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifiedby order by x desc",
            "修改者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.modkwkwifiedby_pie_v1":
        res = get_pie_v1(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifiedby",
            "修改者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.modkwkwifiedby_pie_v2":
        res = get_pie_v2(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifiedby",
            "修改者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.modkwkwifiedby_line":
        res = get_line(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifiedby",
            "修改者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.modkwkwifiedby_bar":
        res = get_bar(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifiedby",
            "修改者ID关联用户",
        )
    if obj.get("optype") == "repkwkworttypes.modkwkwifiedby_bar_v1":
        res = get_bar_v1(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by modkwkwifiedby",
            "修改者ID关联用户",
        )
    # repkwkworttypes(报告类型表)->parentrepkwkworttypeid(父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID)

    if obj.get("optype") == "repkwkworttypes.parentrepkwkworttypeid_pie":
        res = get_pie(
            "select parentrepkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by parentrepkwkworttypeid order by x desc",
            "父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID",
        )
    if obj.get("optype") == "repkwkworttypes.parentrepkwkworttypeid_pie_v1":
        res = get_pie_v1(
            "select parentrepkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by parentrepkwkworttypeid",
            "父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID",
        )
    if obj.get("optype") == "repkwkworttypes.parentrepkwkworttypeid_pie_v2":
        res = get_pie_v2(
            "select parentrepkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by parentrepkwkworttypeid",
            "父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID",
        )
    if obj.get("optype") == "repkwkworttypes.parentrepkwkworttypeid_line":
        res = get_line(
            "select parentrepkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by parentrepkwkworttypeid",
            "父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID",
        )
    if obj.get("optype") == "repkwkworttypes.parentrepkwkworttypeid_bar":
        res = get_bar(
            "select parentrepkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by parentrepkwkworttypeid",
            "父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID",
        )
    if obj.get("optype") == "repkwkworttypes.parentrepkwkworttypeid_bar_v1":
        res = get_bar_v1(
            "select parentrepkwkworttypeid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttypes group by parentrepkwkworttypeid",
            "父报告类型ID用于构建报告类型的层级关系关联本的RepkwkwortTypeID",
        )
    # repkwkwortaudits(报告审核表)->repkwkwortauditid(报告审核ID)

    if obj.get("optype") == "repkwkwortaudits.repkwkwortauditid_pie":
        res = get_pie(
            "select repkwkwortauditid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortauditid order by x desc",
            "报告审核ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortauditid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortauditid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortauditid",
            "报告审核ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortauditid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortauditid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortauditid",
            "报告审核ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortauditid_line":
        res = get_line(
            "select repkwkwortauditid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortauditid",
            "报告审核ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortauditid_bar":
        res = get_bar(
            "select repkwkwortauditid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortauditid",
            "报告审核ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortauditid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortauditid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortauditid",
            "报告审核ID",
        )
    # repkwkwortaudits(报告审核表)->repkwkwortid(报告ID)

    if obj.get("optype") == "repkwkwortaudits.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortid order by x desc",
            "报告ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortid",
            "报告ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortid",
            "报告ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortid",
            "报告ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortid",
            "报告ID",
        )
    if obj.get("optype") == "repkwkwortaudits.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by repkwkwortid",
            "报告ID",
        )
    # repkwkwortaudits(报告审核表)->auditkwkworid(审核人ID)

    if obj.get("optype") == "repkwkwortaudits.auditkwkworid_pie":
        res = get_pie(
            "select auditkwkworid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditkwkworid order by x desc",
            "审核人ID",
        )
    if obj.get("optype") == "repkwkwortaudits.auditkwkworid_pie_v1":
        res = get_pie_v1(
            "select auditkwkworid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditkwkworid",
            "审核人ID",
        )
    if obj.get("optype") == "repkwkwortaudits.auditkwkworid_pie_v2":
        res = get_pie_v2(
            "select auditkwkworid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditkwkworid",
            "审核人ID",
        )
    if obj.get("optype") == "repkwkwortaudits.auditkwkworid_line":
        res = get_line(
            "select auditkwkworid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditkwkworid",
            "审核人ID",
        )
    if obj.get("optype") == "repkwkwortaudits.auditkwkworid_bar":
        res = get_bar(
            "select auditkwkworid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditkwkworid",
            "审核人ID",
        )
    if obj.get("optype") == "repkwkwortaudits.auditkwkworid_bar_v1":
        res = get_bar_v1(
            "select auditkwkworid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditkwkworid",
            "审核人ID",
        )
    if obj.get("optype") == "repkwkwortaudits.auditdate_line":
        res = get_line(
            "select auditdate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditdate order by x",
            "审核日期",
        )
    # repkwkwortaudits(报告审核表)->auditstatus(审核状态)

    if obj.get("optype") == "repkwkwortaudits.auditstatus_pie":
        res = get_pie(
            "select auditstatus x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditstatus order by x desc",
            "审核状态",
        )
    if obj.get("optype") == "repkwkwortaudits.auditstatus_pie_v1":
        res = get_pie_v1(
            "select auditstatus x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditstatus",
            "审核状态",
        )
    if obj.get("optype") == "repkwkwortaudits.auditstatus_pie_v2":
        res = get_pie_v2(
            "select auditstatus x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditstatus",
            "审核状态",
        )
    if obj.get("optype") == "repkwkwortaudits.auditstatus_line":
        res = get_line(
            "select auditstatus x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditstatus",
            "审核状态",
        )
    if obj.get("optype") == "repkwkwortaudits.auditstatus_bar":
        res = get_bar(
            "select auditstatus x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditstatus",
            "审核状态",
        )
    if obj.get("optype") == "repkwkwortaudits.auditstatus_bar_v1":
        res = get_bar_v1(
            "select auditstatus x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditstatus",
            "审核状态",
        )
    # repkwkwortaudits(报告审核表)->auditcomment(审核意见)

    if obj.get("optype") == "repkwkwortaudits.auditcomment_pie":
        res = get_pie(
            "select auditcomment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditcomment order by x desc",
            "审核意见",
        )
    if obj.get("optype") == "repkwkwortaudits.auditcomment_pie_v1":
        res = get_pie_v1(
            "select auditcomment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditcomment",
            "审核意见",
        )
    if obj.get("optype") == "repkwkwortaudits.auditcomment_pie_v2":
        res = get_pie_v2(
            "select auditcomment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditcomment",
            "审核意见",
        )
    if obj.get("optype") == "repkwkwortaudits.auditcomment_line":
        res = get_line(
            "select auditcomment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditcomment",
            "审核意见",
        )
    if obj.get("optype") == "repkwkwortaudits.auditcomment_bar":
        res = get_bar(
            "select auditcomment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditcomment",
            "审核意见",
        )
    if obj.get("optype") == "repkwkwortaudits.auditcomment_bar_v1":
        res = get_bar_v1(
            "select auditcomment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by auditcomment",
            "审核意见",
        )
    if obj.get("optype") == "repkwkwortaudits.approvaldate_line":
        res = get_line(
            "select approvaldate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvaldate order by x",
            "批准日期",
        )
    # repkwkwortaudits(报告审核表)->approvalby(批准人)

    if obj.get("optype") == "repkwkwortaudits.approvalby_pie":
        res = get_pie(
            "select approvalby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvalby order by x desc",
            "批准人",
        )
    if obj.get("optype") == "repkwkwortaudits.approvalby_pie_v1":
        res = get_pie_v1(
            "select approvalby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvalby",
            "批准人",
        )
    if obj.get("optype") == "repkwkwortaudits.approvalby_pie_v2":
        res = get_pie_v2(
            "select approvalby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvalby",
            "批准人",
        )
    if obj.get("optype") == "repkwkwortaudits.approvalby_line":
        res = get_line(
            "select approvalby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvalby",
            "批准人",
        )
    if obj.get("optype") == "repkwkwortaudits.approvalby_bar":
        res = get_bar(
            "select approvalby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvalby",
            "批准人",
        )
    if obj.get("optype") == "repkwkwortaudits.approvalby_bar_v1":
        res = get_bar_v1(
            "select approvalby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by approvalby",
            "批准人",
        )
    # repkwkwortaudits(报告审核表)->isapproved(是否已批准)

    if obj.get("optype") == "repkwkwortaudits.isapproved_pie":
        res = get_pie(
            "select isapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by isapproved order by x desc",
            "是否已批准",
        )
    if obj.get("optype") == "repkwkwortaudits.isapproved_pie_v1":
        res = get_pie_v1(
            "select isapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by isapproved",
            "是否已批准",
        )
    if obj.get("optype") == "repkwkwortaudits.isapproved_pie_v2":
        res = get_pie_v2(
            "select isapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by isapproved",
            "是否已批准",
        )
    if obj.get("optype") == "repkwkwortaudits.isapproved_line":
        res = get_line(
            "select isapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by isapproved",
            "是否已批准",
        )
    if obj.get("optype") == "repkwkwortaudits.isapproved_bar":
        res = get_bar(
            "select isapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by isapproved",
            "是否已批准",
        )
    if obj.get("optype") == "repkwkwortaudits.isapproved_bar_v1":
        res = get_bar_v1(
            "select isapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by isapproved",
            "是否已批准",
        )
    # repkwkwortaudits(报告审核表)->rejectionrekwkwason(拒绝理由)

    if obj.get("optype") == "repkwkwortaudits.rejectionrekwkwason_pie":
        res = get_pie(
            "select rejectionrekwkwason x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by rejectionrekwkwason order by x desc",
            "拒绝理由",
        )
    if obj.get("optype") == "repkwkwortaudits.rejectionrekwkwason_pie_v1":
        res = get_pie_v1(
            "select rejectionrekwkwason x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by rejectionrekwkwason",
            "拒绝理由",
        )
    if obj.get("optype") == "repkwkwortaudits.rejectionrekwkwason_pie_v2":
        res = get_pie_v2(
            "select rejectionrekwkwason x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by rejectionrekwkwason",
            "拒绝理由",
        )
    if obj.get("optype") == "repkwkwortaudits.rejectionrekwkwason_line":
        res = get_line(
            "select rejectionrekwkwason x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by rejectionrekwkwason",
            "拒绝理由",
        )
    if obj.get("optype") == "repkwkwortaudits.rejectionrekwkwason_bar":
        res = get_bar(
            "select rejectionrekwkwason x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by rejectionrekwkwason",
            "拒绝理由",
        )
    if obj.get("optype") == "repkwkwortaudits.rejectionrekwkwason_bar_v1":
        res = get_bar_v1(
            "select rejectionrekwkwason x,count(*) y from vm779_2f88e95faa233d77.repkwkwortaudits group by rejectionrekwkwason",
            "拒绝理由",
        )
    if obj.get("optype") == "auditcomments.commentcontent_wordcloud":
        textlist = get_data(
            "SELECT commentcontent result FROM vm779_2f88e95faa233d77.auditcomments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # auditcomments(审核意见表)->creatkwkworid(创建者ID关联用户)

    if obj.get("optype") == "auditcomments.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creatkwkworid order by x desc",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.creationtime_line":
        res = get_line(
            "select creationtime x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by creationtime order by x",
            "创建时间",
        )
    # auditcomments(审核意见表)->lkwkwastmodkwkwifierid(最后修改者ID关联用户)

    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwifierid_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwifierid order by x desc",
            "最后修改者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwifierid_pie_v1":
        res = get_pie_v1(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwifierid",
            "最后修改者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwifierid_pie_v2":
        res = get_pie_v2(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwifierid",
            "最后修改者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwifierid_line":
        res = get_line(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwifierid",
            "最后修改者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwifierid_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwifierid",
            "最后修改者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwifierid_bar_v1":
        res = get_bar_v1(
            "select lkwkwastmodkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwifierid",
            "最后修改者ID关联用户",
        )
    if obj.get("optype") == "auditcomments.lkwkwastmodkwkwificationtime_line":
        res = get_line(
            "select lkwkwastmodkwkwificationtime x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by lkwkwastmodkwkwificationtime order by x",
            "最后修改时间",
        )
    # auditcomments(审核意见表)->status(审核状态例如待审核、已通过、未通过)

    if obj.get("optype") == "auditcomments.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by status order by x desc",
            "审核状态例如待审核、已通过、未通过",
        )
    if obj.get("optype") == "auditcomments.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by status",
            "审核状态例如待审核、已通过、未通过",
        )
    if obj.get("optype") == "auditcomments.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by status",
            "审核状态例如待审核、已通过、未通过",
        )
    if obj.get("optype") == "auditcomments.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by status",
            "审核状态例如待审核、已通过、未通过",
        )
    if obj.get("optype") == "auditcomments.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by status",
            "审核状态例如待审核、已通过、未通过",
        )
    if obj.get("optype") == "auditcomments.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by status",
            "审核状态例如待审核、已通过、未通过",
        )
    # auditcomments(审核意见表)->targetid(目标ID关联被审核对象的ID如周报ID)

    if obj.get("optype") == "auditcomments.targetid_pie":
        res = get_pie(
            "select targetid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targetid order by x desc",
            "目标ID关联被审核对象的ID如周报ID",
        )
    if obj.get("optype") == "auditcomments.targetid_pie_v1":
        res = get_pie_v1(
            "select targetid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targetid",
            "目标ID关联被审核对象的ID如周报ID",
        )
    if obj.get("optype") == "auditcomments.targetid_pie_v2":
        res = get_pie_v2(
            "select targetid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targetid",
            "目标ID关联被审核对象的ID如周报ID",
        )
    if obj.get("optype") == "auditcomments.targetid_line":
        res = get_line(
            "select targetid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targetid",
            "目标ID关联被审核对象的ID如周报ID",
        )
    if obj.get("optype") == "auditcomments.targetid_bar":
        res = get_bar(
            "select targetid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targetid",
            "目标ID关联被审核对象的ID如周报ID",
        )
    if obj.get("optype") == "auditcomments.targetid_bar_v1":
        res = get_bar_v1(
            "select targetid x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targetid",
            "目标ID关联被审核对象的ID如周报ID",
        )
    # auditcomments(审核意见表)->targettype(目标类型例如周报、项目报告等)

    if obj.get("optype") == "auditcomments.targettype_pie":
        res = get_pie(
            "select targettype x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targettype order by x desc",
            "目标类型例如周报、项目报告等",
        )
    if obj.get("optype") == "auditcomments.targettype_pie_v1":
        res = get_pie_v1(
            "select targettype x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targettype",
            "目标类型例如周报、项目报告等",
        )
    if obj.get("optype") == "auditcomments.targettype_pie_v2":
        res = get_pie_v2(
            "select targettype x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targettype",
            "目标类型例如周报、项目报告等",
        )
    if obj.get("optype") == "auditcomments.targettype_line":
        res = get_line(
            "select targettype x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targettype",
            "目标类型例如周报、项目报告等",
        )
    if obj.get("optype") == "auditcomments.targettype_bar":
        res = get_bar(
            "select targettype x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targettype",
            "目标类型例如周报、项目报告等",
        )
    if obj.get("optype") == "auditcomments.targettype_bar_v1":
        res = get_bar_v1(
            "select targettype x,count(*) y from vm779_2f88e95faa233d77.auditcomments group by targettype",
            "目标类型例如周报、项目报告等",
        )
    # departments(部门表)->departmentid(部门ID)

    if obj.get("optype") == "departments.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentid order by x desc",
            "部门ID",
        )
    if obj.get("optype") == "departments.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "departments.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "departments.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "departments.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "departments.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentid",
            "部门ID",
        )
    # departments(部门表)->departmentname(部门名称)

    if obj.get("optype") == "departments.departmentname_pie":
        res = get_pie(
            "select departmentname x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentname order by x desc",
            "部门名称",
        )
    if obj.get("optype") == "departments.departmentname_pie_v1":
        res = get_pie_v1(
            "select departmentname x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentname",
            "部门名称",
        )
    if obj.get("optype") == "departments.departmentname_pie_v2":
        res = get_pie_v2(
            "select departmentname x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentname",
            "部门名称",
        )
    if obj.get("optype") == "departments.departmentname_line":
        res = get_line(
            "select departmentname x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentname",
            "部门名称",
        )
    if obj.get("optype") == "departments.departmentname_bar":
        res = get_bar(
            "select departmentname x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentname",
            "部门名称",
        )
    if obj.get("optype") == "departments.departmentname_bar_v1":
        res = get_bar_v1(
            "select departmentname x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentname",
            "部门名称",
        )
    # departments(部门表)->parentdepartmentid(上级部门ID)

    if obj.get("optype") == "departments.parentdepartmentid_pie":
        res = get_pie(
            "select parentdepartmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by parentdepartmentid order by x desc",
            "上级部门ID",
        )
    if obj.get("optype") == "departments.parentdepartmentid_pie_v1":
        res = get_pie_v1(
            "select parentdepartmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by parentdepartmentid",
            "上级部门ID",
        )
    if obj.get("optype") == "departments.parentdepartmentid_pie_v2":
        res = get_pie_v2(
            "select parentdepartmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by parentdepartmentid",
            "上级部门ID",
        )
    if obj.get("optype") == "departments.parentdepartmentid_line":
        res = get_line(
            "select parentdepartmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by parentdepartmentid",
            "上级部门ID",
        )
    if obj.get("optype") == "departments.parentdepartmentid_bar":
        res = get_bar(
            "select parentdepartmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by parentdepartmentid",
            "上级部门ID",
        )
    if obj.get("optype") == "departments.parentdepartmentid_bar_v1":
        res = get_bar_v1(
            "select parentdepartmentid x,count(*) y from vm779_2f88e95faa233d77.departments group by parentdepartmentid",
            "上级部门ID",
        )
    # departments(部门表)->departmentcode(部门编码)

    if obj.get("optype") == "departments.departmentcode_pie":
        res = get_pie(
            "select departmentcode x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentcode order by x desc",
            "部门编码",
        )
    if obj.get("optype") == "departments.departmentcode_pie_v1":
        res = get_pie_v1(
            "select departmentcode x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentcode",
            "部门编码",
        )
    if obj.get("optype") == "departments.departmentcode_pie_v2":
        res = get_pie_v2(
            "select departmentcode x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentcode",
            "部门编码",
        )
    if obj.get("optype") == "departments.departmentcode_line":
        res = get_line(
            "select departmentcode x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentcode",
            "部门编码",
        )
    if obj.get("optype") == "departments.departmentcode_bar":
        res = get_bar(
            "select departmentcode x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentcode",
            "部门编码",
        )
    if obj.get("optype") == "departments.departmentcode_bar_v1":
        res = get_bar_v1(
            "select departmentcode x,count(*) y from vm779_2f88e95faa233d77.departments group by departmentcode",
            "部门编码",
        )
    if obj.get("optype") == "departments.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.departments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "departments.createdate_line":
        res = get_line(
            "select createdate x,count(*) y from vm779_2f88e95faa233d77.departments group by createdate order by x",
            "创建日期",
        )
    # departments(部门表)->createdby(创建人)

    if obj.get("optype") == "departments.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.departments group by createdby order by x desc",
            "创建人",
        )
    if obj.get("optype") == "departments.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.departments group by createdby",
            "创建人",
        )
    if obj.get("optype") == "departments.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.departments group by createdby",
            "创建人",
        )
    if obj.get("optype") == "departments.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.departments group by createdby",
            "创建人",
        )
    if obj.get("optype") == "departments.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.departments group by createdby",
            "创建人",
        )
    if obj.get("optype") == "departments.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.departments group by createdby",
            "创建人",
        )
    if obj.get("optype") == "departments.lkwkwastmodkwkwifieddate_line":
        res = get_line(
            "select lkwkwastmodkwkwifieddate x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifieddate order by x",
            "最后修改日期",
        )
    # departments(部门表)->lkwkwastmodkwkwifiedby(最后修改人)

    if obj.get("optype") == "departments.lkwkwastmodkwkwifiedby_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifiedby order by x desc",
            "最后修改人",
        )
    if obj.get("optype") == "departments.lkwkwastmodkwkwifiedby_pie_v1":
        res = get_pie_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifiedby",
            "最后修改人",
        )
    if obj.get("optype") == "departments.lkwkwastmodkwkwifiedby_pie_v2":
        res = get_pie_v2(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifiedby",
            "最后修改人",
        )
    if obj.get("optype") == "departments.lkwkwastmodkwkwifiedby_line":
        res = get_line(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifiedby",
            "最后修改人",
        )
    if obj.get("optype") == "departments.lkwkwastmodkwkwifiedby_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifiedby",
            "最后修改人",
        )
    if obj.get("optype") == "departments.lkwkwastmodkwkwifiedby_bar_v1":
        res = get_bar_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.departments group by lkwkwastmodkwkwifiedby",
            "最后修改人",
        )
    # departments(部门表)->isactive(是否活跃)

    if obj.get("optype") == "departments.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.departments group by isactive order by x desc",
            "是否活跃",
        )
    if obj.get("optype") == "departments.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.departments group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "departments.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.departments group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "departments.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.departments group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "departments.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.departments group by isactive",
            "是否活跃",
        )
    if obj.get("optype") == "departments.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.departments group by isactive",
            "是否活跃",
        )
    # employees(员工表)->employeeid(员工ID)

    if obj.get("optype") == "employees.employeeid_pie":
        res = get_pie(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employees group by employeeid order by x desc",
            "员工ID",
        )
    if obj.get("optype") == "employees.employeeid_pie_v1":
        res = get_pie_v1(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employees group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employees.employeeid_pie_v2":
        res = get_pie_v2(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employees group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employees.employeeid_line":
        res = get_line(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employees group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employees.employeeid_bar":
        res = get_bar(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employees group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employees.employeeid_bar_v1":
        res = get_bar_v1(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employees group by employeeid",
            "员工ID",
        )
    # employees(员工表)->employeename(员工姓名)

    if obj.get("optype") == "employees.employeename_pie":
        res = get_pie(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.employees group by employeename order by x desc",
            "员工姓名",
        )
    if obj.get("optype") == "employees.employeename_pie_v1":
        res = get_pie_v1(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.employees group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "employees.employeename_pie_v2":
        res = get_pie_v2(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.employees group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "employees.employeename_line":
        res = get_line(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.employees group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "employees.employeename_bar":
        res = get_bar(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.employees group by employeename",
            "员工姓名",
        )
    if obj.get("optype") == "employees.employeename_bar_v1":
        res = get_bar_v1(
            "select employeename x,count(*) y from vm779_2f88e95faa233d77.employees group by employeename",
            "员工姓名",
        )
    # employees(员工表)->departmentid(部门ID)

    if obj.get("optype") == "employees.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.employees group by departmentid order by x desc",
            "部门ID",
        )
    if obj.get("optype") == "employees.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.employees group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "employees.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.employees group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "employees.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.employees group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "employees.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.employees group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "employees.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.employees group by departmentid",
            "部门ID",
        )
    # employees(员工表)->position(职位)

    if obj.get("optype") == "employees.position_pie":
        res = get_pie(
            "select position x,count(*) y from vm779_2f88e95faa233d77.employees group by position order by x desc",
            "职位",
        )
    if obj.get("optype") == "employees.position_pie_v1":
        res = get_pie_v1(
            "select position x,count(*) y from vm779_2f88e95faa233d77.employees group by position",
            "职位",
        )
    if obj.get("optype") == "employees.position_pie_v2":
        res = get_pie_v2(
            "select position x,count(*) y from vm779_2f88e95faa233d77.employees group by position",
            "职位",
        )
    if obj.get("optype") == "employees.position_line":
        res = get_line(
            "select position x,count(*) y from vm779_2f88e95faa233d77.employees group by position",
            "职位",
        )
    if obj.get("optype") == "employees.position_bar":
        res = get_bar(
            "select position x,count(*) y from vm779_2f88e95faa233d77.employees group by position",
            "职位",
        )
    if obj.get("optype") == "employees.position_bar_v1":
        res = get_bar_v1(
            "select position x,count(*) y from vm779_2f88e95faa233d77.employees group by position",
            "职位",
        )
    # employees(员工表)->email(电子邮件)

    if obj.get("optype") == "employees.email_pie":
        res = get_pie(
            "select email x,count(*) y from vm779_2f88e95faa233d77.employees group by email order by x desc",
            "电子邮件",
        )
    if obj.get("optype") == "employees.email_pie_v1":
        res = get_pie_v1(
            "select email x,count(*) y from vm779_2f88e95faa233d77.employees group by email",
            "电子邮件",
        )
    if obj.get("optype") == "employees.email_pie_v2":
        res = get_pie_v2(
            "select email x,count(*) y from vm779_2f88e95faa233d77.employees group by email",
            "电子邮件",
        )
    if obj.get("optype") == "employees.email_line":
        res = get_line(
            "select email x,count(*) y from vm779_2f88e95faa233d77.employees group by email",
            "电子邮件",
        )
    if obj.get("optype") == "employees.email_bar":
        res = get_bar(
            "select email x,count(*) y from vm779_2f88e95faa233d77.employees group by email",
            "电子邮件",
        )
    if obj.get("optype") == "employees.email_bar_v1":
        res = get_bar_v1(
            "select email x,count(*) y from vm779_2f88e95faa233d77.employees group by email",
            "电子邮件",
        )
    # employees(员工表)->phonenumber(电话号码)

    if obj.get("optype") == "employees.phonenumber_pie":
        res = get_pie(
            "select phonenumber x,count(*) y from vm779_2f88e95faa233d77.employees group by phonenumber order by x desc",
            "电话号码",
        )
    if obj.get("optype") == "employees.phonenumber_pie_v1":
        res = get_pie_v1(
            "select phonenumber x,count(*) y from vm779_2f88e95faa233d77.employees group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "employees.phonenumber_pie_v2":
        res = get_pie_v2(
            "select phonenumber x,count(*) y from vm779_2f88e95faa233d77.employees group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "employees.phonenumber_line":
        res = get_line(
            "select phonenumber x,count(*) y from vm779_2f88e95faa233d77.employees group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "employees.phonenumber_bar":
        res = get_bar(
            "select phonenumber x,count(*) y from vm779_2f88e95faa233d77.employees group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "employees.phonenumber_bar_v1":
        res = get_bar_v1(
            "select phonenumber x,count(*) y from vm779_2f88e95faa233d77.employees group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "employees.startdate_line":
        res = get_line(
            "select startdate x,count(*) y from vm779_2f88e95faa233d77.employees group by startdate order by x",
            "入职日期",
        )
    # employees(员工表)->salary(薪资)

    if obj.get("optype") == "employees.salary_pie":
        res = get_pie(
            "select salary x,count(*) y from vm779_2f88e95faa233d77.employees group by salary order by x desc",
            "薪资",
        )
    if obj.get("optype") == "employees.salary_pie_v1":
        res = get_pie_v1(
            "select salary x,count(*) y from vm779_2f88e95faa233d77.employees group by salary",
            "薪资",
        )
    if obj.get("optype") == "employees.salary_pie_v2":
        res = get_pie_v2(
            "select salary x,count(*) y from vm779_2f88e95faa233d77.employees group by salary",
            "薪资",
        )
    if obj.get("optype") == "employees.salary_line":
        res = get_line(
            "select salary x,count(*) y from vm779_2f88e95faa233d77.employees group by salary",
            "薪资",
        )
    if obj.get("optype") == "employees.salary_bar":
        res = get_bar(
            "select salary x,count(*) y from vm779_2f88e95faa233d77.employees group by salary",
            "薪资",
        )
    if obj.get("optype") == "employees.salary_bar_v1":
        res = get_bar_v1(
            "select salary x,count(*) y from vm779_2f88e95faa233d77.employees group by salary",
            "薪资",
        )
    # employees(员工表)->managerid(上级员工ID)

    if obj.get("optype") == "employees.managerid_pie":
        res = get_pie(
            "select managerid x,count(*) y from vm779_2f88e95faa233d77.employees group by managerid order by x desc",
            "上级员工ID",
        )
    if obj.get("optype") == "employees.managerid_pie_v1":
        res = get_pie_v1(
            "select managerid x,count(*) y from vm779_2f88e95faa233d77.employees group by managerid",
            "上级员工ID",
        )
    if obj.get("optype") == "employees.managerid_pie_v2":
        res = get_pie_v2(
            "select managerid x,count(*) y from vm779_2f88e95faa233d77.employees group by managerid",
            "上级员工ID",
        )
    if obj.get("optype") == "employees.managerid_line":
        res = get_line(
            "select managerid x,count(*) y from vm779_2f88e95faa233d77.employees group by managerid",
            "上级员工ID",
        )
    if obj.get("optype") == "employees.managerid_bar":
        res = get_bar(
            "select managerid x,count(*) y from vm779_2f88e95faa233d77.employees group by managerid",
            "上级员工ID",
        )
    if obj.get("optype") == "employees.managerid_bar_v1":
        res = get_bar_v1(
            "select managerid x,count(*) y from vm779_2f88e95faa233d77.employees group by managerid",
            "上级员工ID",
        )
    # employees(员工表)->isactive(是否在职)

    if obj.get("optype") == "employees.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.employees group by isactive order by x desc",
            "是否在职",
        )
    if obj.get("optype") == "employees.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.employees group by isactive",
            "是否在职",
        )
    if obj.get("optype") == "employees.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.employees group by isactive",
            "是否在职",
        )
    if obj.get("optype") == "employees.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.employees group by isactive",
            "是否在职",
        )
    if obj.get("optype") == "employees.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.employees group by isactive",
            "是否在职",
        )
    if obj.get("optype") == "employees.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.employees group by isactive",
            "是否在职",
        )
    # employeeweeklyrepkwkwortrelations(员工周报关联表)->employeeid(员工ID)

    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.employeeid_pie":
        res = get_pie(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by employeeid order by x desc",
            "员工ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.employeeid_pie_v1":
        res = get_pie_v1(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.employeeid_pie_v2":
        res = get_pie_v2(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.employeeid_line":
        res = get_line(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.employeeid_bar":
        res = get_bar(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.employeeid_bar_v1":
        res = get_bar_v1(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by employeeid",
            "员工ID",
        )
    # employeeweeklyrepkwkwortrelations(员工周报关联表)->repkwkwortid(周报ID)

    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by repkwkwortid order by x desc",
            "周报ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by repkwkwortid",
            "周报ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by repkwkwortid",
            "周报ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by repkwkwortid",
            "周报ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by repkwkwortid",
            "周报ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by repkwkwortid",
            "周报ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.weekstartdate_line":
        res = get_line(
            "select weekstartdate x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by weekstartdate order by x",
            "周报开始日期",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.weekenddate_line":
        res = get_line(
            "select weekenddate x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by weekenddate order by x",
            "周报结束日期",
        )
    # employeeweeklyrepkwkwortrelations(员工周报关联表)->status(状态如已提交、待审核、已审核等)

    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by status order by x desc",
            "状态如已提交、待审核、已审核等",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by status",
            "状态如已提交、待审核、已审核等",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by status",
            "状态如已提交、待审核、已审核等",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by status",
            "状态如已提交、待审核、已审核等",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by status",
            "状态如已提交、待审核、已审核等",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by status",
            "状态如已提交、待审核、已审核等",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.submittime_line":
        res = get_line(
            "select submittime x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by submittime order by x",
            "提交时间",
        )
    # employeeweeklyrepkwkwortrelations(员工周报关联表)->reviewerid(审核人ID)

    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewerid_pie":
        res = get_pie(
            "select reviewerid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewerid order by x desc",
            "审核人ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewerid_pie_v1":
        res = get_pie_v1(
            "select reviewerid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewerid",
            "审核人ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewerid_pie_v2":
        res = get_pie_v2(
            "select reviewerid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewerid",
            "审核人ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewerid_line":
        res = get_line(
            "select reviewerid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewerid",
            "审核人ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewerid_bar":
        res = get_bar(
            "select reviewerid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewerid",
            "审核人ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewerid_bar_v1":
        res = get_bar_v1(
            "select reviewerid x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewerid",
            "审核人ID",
        )
    if obj.get("optype") == "employeeweeklyrepkwkwortrelations.reviewtime_line":
        res = get_line(
            "select reviewtime x,count(*) y from vm779_2f88e95faa233d77.employeeweeklyrepkwkwortrelations group by reviewtime order by x",
            "审核时间",
        )
    # notkwkwifications(通知表)->title(通知标题)

    if obj.get("optype") == "notkwkwifications.title_pie":
        res = get_pie(
            "select title x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by title order by x desc",
            "通知标题",
        )
    if obj.get("optype") == "notkwkwifications.title_pie_v1":
        res = get_pie_v1(
            "select title x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by title",
            "通知标题",
        )
    if obj.get("optype") == "notkwkwifications.title_pie_v2":
        res = get_pie_v2(
            "select title x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by title",
            "通知标题",
        )
    if obj.get("optype") == "notkwkwifications.title_line":
        res = get_line(
            "select title x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by title",
            "通知标题",
        )
    if obj.get("optype") == "notkwkwifications.title_bar":
        res = get_bar(
            "select title x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by title",
            "通知标题",
        )
    if obj.get("optype") == "notkwkwifications.title_bar_v1":
        res = get_bar_v1(
            "select title x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by title",
            "通知标题",
        )
    if obj.get("optype") == "notkwkwifications.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm779_2f88e95faa233d77.notkwkwifications;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # notkwkwifications(通知表)->senderid(发送者ID)

    if obj.get("optype") == "notkwkwifications.senderid_pie":
        res = get_pie(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by senderid order by x desc",
            "发送者ID",
        )
    if obj.get("optype") == "notkwkwifications.senderid_pie_v1":
        res = get_pie_v1(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "notkwkwifications.senderid_pie_v2":
        res = get_pie_v2(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "notkwkwifications.senderid_line":
        res = get_line(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "notkwkwifications.senderid_bar":
        res = get_bar(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "notkwkwifications.senderid_bar_v1":
        res = get_bar_v1(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by senderid",
            "发送者ID",
        )
    # notkwkwifications(通知表)->receiverid(接收者ID)

    if obj.get("optype") == "notkwkwifications.receiverid_pie":
        res = get_pie(
            "select receiverid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by receiverid order by x desc",
            "接收者ID",
        )
    if obj.get("optype") == "notkwkwifications.receiverid_pie_v1":
        res = get_pie_v1(
            "select receiverid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "notkwkwifications.receiverid_pie_v2":
        res = get_pie_v2(
            "select receiverid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "notkwkwifications.receiverid_line":
        res = get_line(
            "select receiverid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "notkwkwifications.receiverid_bar":
        res = get_bar(
            "select receiverid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "notkwkwifications.receiverid_bar_v1":
        res = get_bar_v1(
            "select receiverid x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "notkwkwifications.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by sendtime order by x",
            "发送时间",
        )
    # notkwkwifications(通知表)->readstatus(阅读状态)

    if obj.get("optype") == "notkwkwifications.readstatus_pie":
        res = get_pie(
            "select readstatus x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by readstatus order by x desc",
            "阅读状态",
        )
    if obj.get("optype") == "notkwkwifications.readstatus_pie_v1":
        res = get_pie_v1(
            "select readstatus x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by readstatus",
            "阅读状态",
        )
    if obj.get("optype") == "notkwkwifications.readstatus_pie_v2":
        res = get_pie_v2(
            "select readstatus x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by readstatus",
            "阅读状态",
        )
    if obj.get("optype") == "notkwkwifications.readstatus_line":
        res = get_line(
            "select readstatus x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by readstatus",
            "阅读状态",
        )
    if obj.get("optype") == "notkwkwifications.readstatus_bar":
        res = get_bar(
            "select readstatus x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by readstatus",
            "阅读状态",
        )
    if obj.get("optype") == "notkwkwifications.readstatus_bar_v1":
        res = get_bar_v1(
            "select readstatus x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by readstatus",
            "阅读状态",
        )
    # notkwkwifications(通知表)->prikwkwority(优先级)

    if obj.get("optype") == "notkwkwifications.prikwkwority_pie":
        res = get_pie(
            "select prikwkwority x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by prikwkwority order by x desc",
            "优先级",
        )
    if obj.get("optype") == "notkwkwifications.prikwkwority_pie_v1":
        res = get_pie_v1(
            "select prikwkwority x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by prikwkwority",
            "优先级",
        )
    if obj.get("optype") == "notkwkwifications.prikwkwority_pie_v2":
        res = get_pie_v2(
            "select prikwkwority x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by prikwkwority",
            "优先级",
        )
    if obj.get("optype") == "notkwkwifications.prikwkwority_line":
        res = get_line(
            "select prikwkwority x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by prikwkwority",
            "优先级",
        )
    if obj.get("optype") == "notkwkwifications.prikwkwority_bar":
        res = get_bar(
            "select prikwkwority x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by prikwkwority",
            "优先级",
        )
    if obj.get("optype") == "notkwkwifications.prikwkwority_bar_v1":
        res = get_bar_v1(
            "select prikwkwority x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by prikwkwority",
            "优先级",
        )
    # notkwkwifications(通知表)->kwkwiskwkwdeleted(是否删除)

    if obj.get("optype") == "notkwkwifications.kwkwiskwkwdeleted_pie":
        res = get_pie(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by kwkwiskwkwdeleted order by x desc",
            "是否删除",
        )
    if obj.get("optype") == "notkwkwifications.kwkwiskwkwdeleted_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by kwkwiskwkwdeleted",
            "是否删除",
        )
    if obj.get("optype") == "notkwkwifications.kwkwiskwkwdeleted_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by kwkwiskwkwdeleted",
            "是否删除",
        )
    if obj.get("optype") == "notkwkwifications.kwkwiskwkwdeleted_line":
        res = get_line(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by kwkwiskwkwdeleted",
            "是否删除",
        )
    if obj.get("optype") == "notkwkwifications.kwkwiskwkwdeleted_bar":
        res = get_bar(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by kwkwiskwkwdeleted",
            "是否删除",
        )
    if obj.get("optype") == "notkwkwifications.kwkwiskwkwdeleted_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.notkwkwifications group by kwkwiskwkwdeleted",
            "是否删除",
        )
    # notkwkwificationtypes(通知类型表)->notkwkwificationtypeid(通知类型ID)

    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypeid_pie":
        res = get_pie(
            "select notkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypeid order by x desc",
            "通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypeid_pie_v1":
        res = get_pie_v1(
            "select notkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypeid",
            "通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypeid_pie_v2":
        res = get_pie_v2(
            "select notkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypeid",
            "通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypeid_line":
        res = get_line(
            "select notkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypeid",
            "通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypeid_bar":
        res = get_bar(
            "select notkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypeid",
            "通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypeid_bar_v1":
        res = get_bar_v1(
            "select notkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypeid",
            "通知类型ID",
        )
    # notkwkwificationtypes(通知类型表)->notkwkwificationtypename(通知类型名称)

    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypename_pie":
        res = get_pie(
            "select notkwkwificationtypename x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypename order by x desc",
            "通知类型名称",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypename_pie_v1":
        res = get_pie_v1(
            "select notkwkwificationtypename x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypename",
            "通知类型名称",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypename_pie_v2":
        res = get_pie_v2(
            "select notkwkwificationtypename x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypename",
            "通知类型名称",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypename_line":
        res = get_line(
            "select notkwkwificationtypename x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypename",
            "通知类型名称",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypename_bar":
        res = get_bar(
            "select notkwkwificationtypename x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypename",
            "通知类型名称",
        )
    if obj.get("optype") == "notkwkwificationtypes.notkwkwificationtypename_bar_v1":
        res = get_bar_v1(
            "select notkwkwificationtypename x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by notkwkwificationtypename",
            "通知类型名称",
        )
    if obj.get("optype") == "notkwkwificationtypes.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.notkwkwificationtypes;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # notkwkwificationtypes(通知类型表)->isactive(是否激活)

    if obj.get("optype") == "notkwkwificationtypes.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "notkwkwificationtypes.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "notkwkwificationtypes.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "notkwkwificationtypes.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "notkwkwificationtypes.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "notkwkwificationtypes.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "notkwkwificationtypes.createddate_line":
        res = get_line(
            "select createddate x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createddate order by x",
            "创建日期",
        )
    # notkwkwificationtypes(通知类型表)->createdby(创建者)

    if obj.get("optype") == "notkwkwificationtypes.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createdby order by x desc",
            "创建者",
        )
    if obj.get("optype") == "notkwkwificationtypes.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createdby",
            "创建者",
        )
    if obj.get("optype") == "notkwkwificationtypes.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createdby",
            "创建者",
        )
    if obj.get("optype") == "notkwkwificationtypes.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createdby",
            "创建者",
        )
    if obj.get("optype") == "notkwkwificationtypes.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createdby",
            "创建者",
        )
    if obj.get("optype") == "notkwkwificationtypes.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by createdby",
            "创建者",
        )
    if obj.get("optype") == "notkwkwificationtypes.modkwkwifieddate_line":
        res = get_line(
            "select modkwkwifieddate x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifieddate order by x",
            "修改日期",
        )
    # notkwkwificationtypes(通知类型表)->modkwkwifiedby(修改者)

    if obj.get("optype") == "notkwkwificationtypes.modkwkwifiedby_pie":
        res = get_pie(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifiedby order by x desc",
            "修改者",
        )
    if obj.get("optype") == "notkwkwificationtypes.modkwkwifiedby_pie_v1":
        res = get_pie_v1(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifiedby",
            "修改者",
        )
    if obj.get("optype") == "notkwkwificationtypes.modkwkwifiedby_pie_v2":
        res = get_pie_v2(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifiedby",
            "修改者",
        )
    if obj.get("optype") == "notkwkwificationtypes.modkwkwifiedby_line":
        res = get_line(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifiedby",
            "修改者",
        )
    if obj.get("optype") == "notkwkwificationtypes.modkwkwifiedby_bar":
        res = get_bar(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifiedby",
            "修改者",
        )
    if obj.get("optype") == "notkwkwificationtypes.modkwkwifiedby_bar_v1":
        res = get_bar_v1(
            "select modkwkwifiedby x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by modkwkwifiedby",
            "修改者",
        )
    # notkwkwificationtypes(通知类型表)->parentnotkwkwificationtypeid(父通知类型ID)

    if obj.get("optype") == "notkwkwificationtypes.parentnotkwkwificationtypeid_pie":
        res = get_pie(
            "select parentnotkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by parentnotkwkwificationtypeid order by x desc",
            "父通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.parentnotkwkwificationtypeid_pie_v1":
        res = get_pie_v1(
            "select parentnotkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by parentnotkwkwificationtypeid",
            "父通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.parentnotkwkwificationtypeid_pie_v2":
        res = get_pie_v2(
            "select parentnotkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by parentnotkwkwificationtypeid",
            "父通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.parentnotkwkwificationtypeid_line":
        res = get_line(
            "select parentnotkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by parentnotkwkwificationtypeid",
            "父通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.parentnotkwkwificationtypeid_bar":
        res = get_bar(
            "select parentnotkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by parentnotkwkwificationtypeid",
            "父通知类型ID",
        )
    if obj.get("optype") == "notkwkwificationtypes.parentnotkwkwificationtypeid_bar_v1":
        res = get_bar_v1(
            "select parentnotkwkwificationtypeid x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by parentnotkwkwificationtypeid",
            "父通知类型ID",
        )
    # notkwkwificationtypes(通知类型表)->skwkwortorder(排序顺序)

    if obj.get("optype") == "notkwkwificationtypes.skwkwortorder_pie":
        res = get_pie(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by skwkwortorder order by x desc",
            "排序顺序",
        )
    if obj.get("optype") == "notkwkwificationtypes.skwkwortorder_pie_v1":
        res = get_pie_v1(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "notkwkwificationtypes.skwkwortorder_pie_v2":
        res = get_pie_v2(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "notkwkwificationtypes.skwkwortorder_line":
        res = get_line(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "notkwkwificationtypes.skwkwortorder_bar":
        res = get_bar(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "notkwkwificationtypes.skwkwortorder_bar_v1":
        res = get_bar_v1(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.notkwkwificationtypes group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "emaillogs.emailaddress_wordcloud":
        textlist = get_data(
            "SELECT emailaddress result FROM vm779_2f88e95faa233d77.emaillogs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # emaillogs(邮件发送记录表)->subject(邮件主题)

    if obj.get("optype") == "emaillogs.subject_pie":
        res = get_pie(
            "select subject x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by subject order by x desc",
            "邮件主题",
        )
    if obj.get("optype") == "emaillogs.subject_pie_v1":
        res = get_pie_v1(
            "select subject x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by subject",
            "邮件主题",
        )
    if obj.get("optype") == "emaillogs.subject_pie_v2":
        res = get_pie_v2(
            "select subject x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by subject",
            "邮件主题",
        )
    if obj.get("optype") == "emaillogs.subject_line":
        res = get_line(
            "select subject x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by subject",
            "邮件主题",
        )
    if obj.get("optype") == "emaillogs.subject_bar":
        res = get_bar(
            "select subject x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by subject",
            "邮件主题",
        )
    if obj.get("optype") == "emaillogs.subject_bar_v1":
        res = get_bar_v1(
            "select subject x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by subject",
            "邮件主题",
        )
    if obj.get("optype") == "emaillogs.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm779_2f88e95faa233d77.emaillogs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "emaillogs.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by sendtime order by x",
            "发送时间",
        )
    # emaillogs(邮件发送记录表)->status(发送状态如成功、失败、待发送)

    if obj.get("optype") == "emaillogs.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by status order by x desc",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "emaillogs.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "emaillogs.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "emaillogs.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "emaillogs.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "emaillogs.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by status",
            "发送状态如成功、失败、待发送",
        )
    # emaillogs(邮件发送记录表)->recipientcount(收件人数量)

    if obj.get("optype") == "emaillogs.recipientcount_pie":
        res = get_pie(
            "select recipientcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by recipientcount order by x desc",
            "收件人数量",
        )
    if obj.get("optype") == "emaillogs.recipientcount_pie_v1":
        res = get_pie_v1(
            "select recipientcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by recipientcount",
            "收件人数量",
        )
    if obj.get("optype") == "emaillogs.recipientcount_pie_v2":
        res = get_pie_v2(
            "select recipientcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by recipientcount",
            "收件人数量",
        )
    if obj.get("optype") == "emaillogs.recipientcount_line":
        res = get_line(
            "select recipientcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by recipientcount",
            "收件人数量",
        )
    if obj.get("optype") == "emaillogs.recipientcount_bar":
        res = get_bar(
            "select recipientcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by recipientcount",
            "收件人数量",
        )
    if obj.get("optype") == "emaillogs.recipientcount_bar_v1":
        res = get_bar_v1(
            "select recipientcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by recipientcount",
            "收件人数量",
        )
    # emaillogs(邮件发送记录表)->senderid(发送者ID关联用户)

    if obj.get("optype") == "emaillogs.senderid_pie":
        res = get_pie(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by senderid order by x desc",
            "发送者ID关联用户",
        )
    if obj.get("optype") == "emaillogs.senderid_pie_v1":
        res = get_pie_v1(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by senderid",
            "发送者ID关联用户",
        )
    if obj.get("optype") == "emaillogs.senderid_pie_v2":
        res = get_pie_v2(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by senderid",
            "发送者ID关联用户",
        )
    if obj.get("optype") == "emaillogs.senderid_line":
        res = get_line(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by senderid",
            "发送者ID关联用户",
        )
    if obj.get("optype") == "emaillogs.senderid_bar":
        res = get_bar(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by senderid",
            "发送者ID关联用户",
        )
    if obj.get("optype") == "emaillogs.senderid_bar_v1":
        res = get_bar_v1(
            "select senderid x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by senderid",
            "发送者ID关联用户",
        )
    # emaillogs(邮件发送记录表)->attachmentcount(附件数量)

    if obj.get("optype") == "emaillogs.attachmentcount_pie":
        res = get_pie(
            "select attachmentcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by attachmentcount order by x desc",
            "附件数量",
        )
    if obj.get("optype") == "emaillogs.attachmentcount_pie_v1":
        res = get_pie_v1(
            "select attachmentcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by attachmentcount",
            "附件数量",
        )
    if obj.get("optype") == "emaillogs.attachmentcount_pie_v2":
        res = get_pie_v2(
            "select attachmentcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by attachmentcount",
            "附件数量",
        )
    if obj.get("optype") == "emaillogs.attachmentcount_line":
        res = get_line(
            "select attachmentcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by attachmentcount",
            "附件数量",
        )
    if obj.get("optype") == "emaillogs.attachmentcount_bar":
        res = get_bar(
            "select attachmentcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by attachmentcount",
            "附件数量",
        )
    if obj.get("optype") == "emaillogs.attachmentcount_bar_v1":
        res = get_bar_v1(
            "select attachmentcount x,count(*) y from vm779_2f88e95faa233d77.emaillogs group by attachmentcount",
            "附件数量",
        )
    if obj.get("optype") == "smslogs.smscontent_wordcloud":
        textlist = get_data(
            "SELECT smscontent result FROM vm779_2f88e95faa233d77.smslogs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # smslogs(短信发送记录表)->receivernumber(接收者号码)

    if obj.get("optype") == "smslogs.receivernumber_pie":
        res = get_pie(
            "select receivernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by receivernumber order by x desc",
            "接收者号码",
        )
    if obj.get("optype") == "smslogs.receivernumber_pie_v1":
        res = get_pie_v1(
            "select receivernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by receivernumber",
            "接收者号码",
        )
    if obj.get("optype") == "smslogs.receivernumber_pie_v2":
        res = get_pie_v2(
            "select receivernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by receivernumber",
            "接收者号码",
        )
    if obj.get("optype") == "smslogs.receivernumber_line":
        res = get_line(
            "select receivernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by receivernumber",
            "接收者号码",
        )
    if obj.get("optype") == "smslogs.receivernumber_bar":
        res = get_bar(
            "select receivernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by receivernumber",
            "接收者号码",
        )
    if obj.get("optype") == "smslogs.receivernumber_bar_v1":
        res = get_bar_v1(
            "select receivernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by receivernumber",
            "接收者号码",
        )
    # smslogs(短信发送记录表)->sendernumber(发送者号码)

    if obj.get("optype") == "smslogs.sendernumber_pie":
        res = get_pie(
            "select sendernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendernumber order by x desc",
            "发送者号码",
        )
    if obj.get("optype") == "smslogs.sendernumber_pie_v1":
        res = get_pie_v1(
            "select sendernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendernumber",
            "发送者号码",
        )
    if obj.get("optype") == "smslogs.sendernumber_pie_v2":
        res = get_pie_v2(
            "select sendernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendernumber",
            "发送者号码",
        )
    if obj.get("optype") == "smslogs.sendernumber_line":
        res = get_line(
            "select sendernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendernumber",
            "发送者号码",
        )
    if obj.get("optype") == "smslogs.sendernumber_bar":
        res = get_bar(
            "select sendernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendernumber",
            "发送者号码",
        )
    if obj.get("optype") == "smslogs.sendernumber_bar_v1":
        res = get_bar_v1(
            "select sendernumber x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendernumber",
            "发送者号码",
        )
    if obj.get("optype") == "smslogs.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm779_2f88e95faa233d77.smslogs group by sendtime order by x",
            "发送时间",
        )
    # smslogs(短信发送记录表)->status(发送状态如成功、失败、待发送)

    if obj.get("optype") == "smslogs.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.smslogs group by status order by x desc",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "smslogs.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.smslogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "smslogs.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.smslogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "smslogs.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.smslogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "smslogs.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.smslogs group by status",
            "发送状态如成功、失败、待发送",
        )
    if obj.get("optype") == "smslogs.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.smslogs group by status",
            "发送状态如成功、失败、待发送",
        )
    # smslogs(短信发送记录表)->rekwkwtrycount(重试次数)

    if obj.get("optype") == "smslogs.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm779_2f88e95faa233d77.smslogs group by rekwkwtrycount order by x desc",
            "重试次数",
        )
    if obj.get("optype") == "smslogs.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm779_2f88e95faa233d77.smslogs group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "smslogs.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm779_2f88e95faa233d77.smslogs group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "smslogs.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm779_2f88e95faa233d77.smslogs group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "smslogs.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm779_2f88e95faa233d77.smslogs group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "smslogs.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm779_2f88e95faa233d77.smslogs group by rekwkwtrycount",
            "重试次数",
        )
    # smslogs(短信发送记录表)->errkwkwormessage(错误信息如果发送失败)

    if obj.get("optype") == "smslogs.errkwkwormessage_pie":
        res = get_pie(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.smslogs group by errkwkwormessage order by x desc",
            "错误信息如果发送失败",
        )
    if obj.get("optype") == "smslogs.errkwkwormessage_pie_v1":
        res = get_pie_v1(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.smslogs group by errkwkwormessage",
            "错误信息如果发送失败",
        )
    if obj.get("optype") == "smslogs.errkwkwormessage_pie_v2":
        res = get_pie_v2(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.smslogs group by errkwkwormessage",
            "错误信息如果发送失败",
        )
    if obj.get("optype") == "smslogs.errkwkwormessage_line":
        res = get_line(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.smslogs group by errkwkwormessage",
            "错误信息如果发送失败",
        )
    if obj.get("optype") == "smslogs.errkwkwormessage_bar":
        res = get_bar(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.smslogs group by errkwkwormessage",
            "错误信息如果发送失败",
        )
    if obj.get("optype") == "smslogs.errkwkwormessage_bar_v1":
        res = get_bar_v1(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.smslogs group by errkwkwormessage",
            "错误信息如果发送失败",
        )
    # smslogs(短信发送记录表)->kwkwisread(是否已读标记接收者是否已查看短信)

    if obj.get("optype") == "smslogs.kwkwisread_pie":
        res = get_pie(
            "select kwkwisread x,count(*) y from vm779_2f88e95faa233d77.smslogs group by kwkwisread order by x desc",
            "是否已读标记接收者是否已查看短信",
        )
    if obj.get("optype") == "smslogs.kwkwisread_pie_v1":
        res = get_pie_v1(
            "select kwkwisread x,count(*) y from vm779_2f88e95faa233d77.smslogs group by kwkwisread",
            "是否已读标记接收者是否已查看短信",
        )
    if obj.get("optype") == "smslogs.kwkwisread_pie_v2":
        res = get_pie_v2(
            "select kwkwisread x,count(*) y from vm779_2f88e95faa233d77.smslogs group by kwkwisread",
            "是否已读标记接收者是否已查看短信",
        )
    if obj.get("optype") == "smslogs.kwkwisread_line":
        res = get_line(
            "select kwkwisread x,count(*) y from vm779_2f88e95faa233d77.smslogs group by kwkwisread",
            "是否已读标记接收者是否已查看短信",
        )
    if obj.get("optype") == "smslogs.kwkwisread_bar":
        res = get_bar(
            "select kwkwisread x,count(*) y from vm779_2f88e95faa233d77.smslogs group by kwkwisread",
            "是否已读标记接收者是否已查看短信",
        )
    if obj.get("optype") == "smslogs.kwkwisread_bar_v1":
        res = get_bar_v1(
            "select kwkwisread x,count(*) y from vm779_2f88e95faa233d77.smslogs group by kwkwisread",
            "是否已读标记接收者是否已查看短信",
        )
    # smslogs(短信发送记录表)->relatedtkwkwaskid(关联任务ID如果短信发送与某个特定任务相关)

    if obj.get("optype") == "smslogs.relatedtkwkwaskid_pie":
        res = get_pie(
            "select relatedtkwkwaskid x,count(*) y from vm779_2f88e95faa233d77.smslogs group by relatedtkwkwaskid order by x desc",
            "关联任务ID如果短信发送与某个特定任务相关",
        )
    if obj.get("optype") == "smslogs.relatedtkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select relatedtkwkwaskid x,count(*) y from vm779_2f88e95faa233d77.smslogs group by relatedtkwkwaskid",
            "关联任务ID如果短信发送与某个特定任务相关",
        )
    if obj.get("optype") == "smslogs.relatedtkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select relatedtkwkwaskid x,count(*) y from vm779_2f88e95faa233d77.smslogs group by relatedtkwkwaskid",
            "关联任务ID如果短信发送与某个特定任务相关",
        )
    if obj.get("optype") == "smslogs.relatedtkwkwaskid_line":
        res = get_line(
            "select relatedtkwkwaskid x,count(*) y from vm779_2f88e95faa233d77.smslogs group by relatedtkwkwaskid",
            "关联任务ID如果短信发送与某个特定任务相关",
        )
    if obj.get("optype") == "smslogs.relatedtkwkwaskid_bar":
        res = get_bar(
            "select relatedtkwkwaskid x,count(*) y from vm779_2f88e95faa233d77.smslogs group by relatedtkwkwaskid",
            "关联任务ID如果短信发送与某个特定任务相关",
        )
    if obj.get("optype") == "smslogs.relatedtkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select relatedtkwkwaskid x,count(*) y from vm779_2f88e95faa233d77.smslogs group by relatedtkwkwaskid",
            "关联任务ID如果短信发送与某个特定任务相关",
        )
    # attachments(附件表)->filename(文件名)

    if obj.get("optype") == "attachments.filename_pie":
        res = get_pie(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.attachments group by filename order by x desc",
            "文件名",
        )
    if obj.get("optype") == "attachments.filename_pie_v1":
        res = get_pie_v1(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.attachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "attachments.filename_pie_v2":
        res = get_pie_v2(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.attachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "attachments.filename_line":
        res = get_line(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.attachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "attachments.filename_bar":
        res = get_bar(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.attachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "attachments.filename_bar_v1":
        res = get_bar_v1(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.attachments group by filename",
            "文件名",
        )
    # attachments(附件表)->filepath(文件存储路径)

    if obj.get("optype") == "attachments.filepath_pie":
        res = get_pie(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.attachments group by filepath order by x desc",
            "文件存储路径",
        )
    if obj.get("optype") == "attachments.filepath_pie_v1":
        res = get_pie_v1(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.attachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "attachments.filepath_pie_v2":
        res = get_pie_v2(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.attachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "attachments.filepath_line":
        res = get_line(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.attachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "attachments.filepath_bar":
        res = get_bar(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.attachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "attachments.filepath_bar_v1":
        res = get_bar_v1(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.attachments group by filepath",
            "文件存储路径",
        )
    # attachments(附件表)->filesize(文件大小)

    if obj.get("optype") == "attachments.filesize_pie":
        res = get_pie(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.attachments group by filesize order by x desc",
            "文件大小",
        )
    if obj.get("optype") == "attachments.filesize_pie_v1":
        res = get_pie_v1(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.attachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "attachments.filesize_pie_v2":
        res = get_pie_v2(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.attachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "attachments.filesize_line":
        res = get_line(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.attachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "attachments.filesize_bar":
        res = get_bar(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.attachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "attachments.filesize_bar_v1":
        res = get_bar_v1(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.attachments group by filesize",
            "文件大小",
        )
    # attachments(附件表)->filetype(文件类型)

    if obj.get("optype") == "attachments.filetype_pie":
        res = get_pie(
            "select filetype x,count(*) y from vm779_2f88e95faa233d77.attachments group by filetype order by x desc",
            "文件类型",
        )
    if obj.get("optype") == "attachments.filetype_pie_v1":
        res = get_pie_v1(
            "select filetype x,count(*) y from vm779_2f88e95faa233d77.attachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "attachments.filetype_pie_v2":
        res = get_pie_v2(
            "select filetype x,count(*) y from vm779_2f88e95faa233d77.attachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "attachments.filetype_line":
        res = get_line(
            "select filetype x,count(*) y from vm779_2f88e95faa233d77.attachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "attachments.filetype_bar":
        res = get_bar(
            "select filetype x,count(*) y from vm779_2f88e95faa233d77.attachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "attachments.filetype_bar_v1":
        res = get_bar_v1(
            "select filetype x,count(*) y from vm779_2f88e95faa233d77.attachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "attachments.uploadtime_line":
        res = get_line(
            "select uploadtime x,count(*) y from vm779_2f88e95faa233d77.attachments group by uploadtime order by x",
            "上传时间",
        )
    # attachments(附件表)->creatkwkworid(创建者ID)

    if obj.get("optype") == "attachments.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworid order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "attachments.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "attachments.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "attachments.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "attachments.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "attachments.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworid",
            "创建者ID",
        )
    # attachments(附件表)->creatkwkworname(创建者姓名)

    if obj.get("optype") == "attachments.creatkwkworname_pie":
        res = get_pie(
            "select creatkwkworname x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworname order by x desc",
            "创建者姓名",
        )
    if obj.get("optype") == "attachments.creatkwkworname_pie_v1":
        res = get_pie_v1(
            "select creatkwkworname x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworname",
            "创建者姓名",
        )
    if obj.get("optype") == "attachments.creatkwkworname_pie_v2":
        res = get_pie_v2(
            "select creatkwkworname x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworname",
            "创建者姓名",
        )
    if obj.get("optype") == "attachments.creatkwkworname_line":
        res = get_line(
            "select creatkwkworname x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworname",
            "创建者姓名",
        )
    if obj.get("optype") == "attachments.creatkwkworname_bar":
        res = get_bar(
            "select creatkwkworname x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworname",
            "创建者姓名",
        )
    if obj.get("optype") == "attachments.creatkwkworname_bar_v1":
        res = get_bar_v1(
            "select creatkwkworname x,count(*) y from vm779_2f88e95faa233d77.attachments group by creatkwkworname",
            "创建者姓名",
        )
    # attachments(附件表)->relatedrepkwkwortid(关联周报ID)

    if obj.get("optype") == "attachments.relatedrepkwkwortid_pie":
        res = get_pie(
            "select relatedrepkwkwortid x,count(*) y from vm779_2f88e95faa233d77.attachments group by relatedrepkwkwortid order by x desc",
            "关联周报ID",
        )
    if obj.get("optype") == "attachments.relatedrepkwkwortid_pie_v1":
        res = get_pie_v1(
            "select relatedrepkwkwortid x,count(*) y from vm779_2f88e95faa233d77.attachments group by relatedrepkwkwortid",
            "关联周报ID",
        )
    if obj.get("optype") == "attachments.relatedrepkwkwortid_pie_v2":
        res = get_pie_v2(
            "select relatedrepkwkwortid x,count(*) y from vm779_2f88e95faa233d77.attachments group by relatedrepkwkwortid",
            "关联周报ID",
        )
    if obj.get("optype") == "attachments.relatedrepkwkwortid_line":
        res = get_line(
            "select relatedrepkwkwortid x,count(*) y from vm779_2f88e95faa233d77.attachments group by relatedrepkwkwortid",
            "关联周报ID",
        )
    if obj.get("optype") == "attachments.relatedrepkwkwortid_bar":
        res = get_bar(
            "select relatedrepkwkwortid x,count(*) y from vm779_2f88e95faa233d77.attachments group by relatedrepkwkwortid",
            "关联周报ID",
        )
    if obj.get("optype") == "attachments.relatedrepkwkwortid_bar_v1":
        res = get_bar_v1(
            "select relatedrepkwkwortid x,count(*) y from vm779_2f88e95faa233d77.attachments group by relatedrepkwkwortid",
            "关联周报ID",
        )
    if obj.get("optype") == "attachments.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.attachments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # attachmenttypes(附件类型表)->attachmenttypeid(附件类型ID)

    if obj.get("optype") == "attachmenttypes.attachmenttypeid_pie":
        res = get_pie(
            "select attachmenttypeid x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypeid order by x desc",
            "附件类型ID",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypeid_pie_v1":
        res = get_pie_v1(
            "select attachmenttypeid x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypeid",
            "附件类型ID",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypeid_pie_v2":
        res = get_pie_v2(
            "select attachmenttypeid x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypeid",
            "附件类型ID",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypeid_line":
        res = get_line(
            "select attachmenttypeid x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypeid",
            "附件类型ID",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypeid_bar":
        res = get_bar(
            "select attachmenttypeid x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypeid",
            "附件类型ID",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypeid_bar_v1":
        res = get_bar_v1(
            "select attachmenttypeid x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypeid",
            "附件类型ID",
        )
    # attachmenttypes(附件类型表)->attachmenttypename(附件类型名称)

    if obj.get("optype") == "attachmenttypes.attachmenttypename_pie":
        res = get_pie(
            "select attachmenttypename x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypename order by x desc",
            "附件类型名称",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypename_pie_v1":
        res = get_pie_v1(
            "select attachmenttypename x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypename",
            "附件类型名称",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypename_pie_v2":
        res = get_pie_v2(
            "select attachmenttypename x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypename",
            "附件类型名称",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypename_line":
        res = get_line(
            "select attachmenttypename x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypename",
            "附件类型名称",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypename_bar":
        res = get_bar(
            "select attachmenttypename x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypename",
            "附件类型名称",
        )
    if obj.get("optype") == "attachmenttypes.attachmenttypename_bar_v1":
        res = get_bar_v1(
            "select attachmenttypename x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by attachmenttypename",
            "附件类型名称",
        )
    if obj.get("optype") == "attachmenttypes.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.attachmenttypes;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # attachmenttypes(附件类型表)->fileextension(文件扩展名)

    if obj.get("optype") == "attachmenttypes.fileextension_pie":
        res = get_pie(
            "select fileextension x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by fileextension order by x desc",
            "文件扩展名",
        )
    if obj.get("optype") == "attachmenttypes.fileextension_pie_v1":
        res = get_pie_v1(
            "select fileextension x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by fileextension",
            "文件扩展名",
        )
    if obj.get("optype") == "attachmenttypes.fileextension_pie_v2":
        res = get_pie_v2(
            "select fileextension x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by fileextension",
            "文件扩展名",
        )
    if obj.get("optype") == "attachmenttypes.fileextension_line":
        res = get_line(
            "select fileextension x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by fileextension",
            "文件扩展名",
        )
    if obj.get("optype") == "attachmenttypes.fileextension_bar":
        res = get_bar(
            "select fileextension x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by fileextension",
            "文件扩展名",
        )
    if obj.get("optype") == "attachmenttypes.fileextension_bar_v1":
        res = get_bar_v1(
            "select fileextension x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by fileextension",
            "文件扩展名",
        )
    # attachmenttypes(附件类型表)->maxfilesize(最大文件大小单位MB)

    if obj.get("optype") == "attachmenttypes.maxfilesize_pie":
        res = get_pie(
            "select maxfilesize x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by maxfilesize order by x desc",
            "最大文件大小单位MB",
        )
    if obj.get("optype") == "attachmenttypes.maxfilesize_pie_v1":
        res = get_pie_v1(
            "select maxfilesize x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by maxfilesize",
            "最大文件大小单位MB",
        )
    if obj.get("optype") == "attachmenttypes.maxfilesize_pie_v2":
        res = get_pie_v2(
            "select maxfilesize x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by maxfilesize",
            "最大文件大小单位MB",
        )
    if obj.get("optype") == "attachmenttypes.maxfilesize_line":
        res = get_line(
            "select maxfilesize x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by maxfilesize",
            "最大文件大小单位MB",
        )
    if obj.get("optype") == "attachmenttypes.maxfilesize_bar":
        res = get_bar(
            "select maxfilesize x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by maxfilesize",
            "最大文件大小单位MB",
        )
    if obj.get("optype") == "attachmenttypes.maxfilesize_bar_v1":
        res = get_bar_v1(
            "select maxfilesize x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by maxfilesize",
            "最大文件大小单位MB",
        )
    if obj.get("optype") == "attachmenttypes.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "attachmenttypes.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedat order by x",
            "更新时间",
        )
    # attachmenttypes(附件类型表)->isactive(是否激活)

    if obj.get("optype") == "attachmenttypes.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "attachmenttypes.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "attachmenttypes.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "attachmenttypes.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "attachmenttypes.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "attachmenttypes.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by isactive",
            "是否激活",
        )
    # attachmenttypes(附件类型表)->createdby(创建者ID)

    if obj.get("optype") == "attachmenttypes.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdby order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "attachmenttypes.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "attachmenttypes.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "attachmenttypes.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "attachmenttypes.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "attachmenttypes.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by createdby",
            "创建者ID",
        )
    # attachmenttypes(附件类型表)->updatedby(更新者ID)

    if obj.get("optype") == "attachmenttypes.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedby order by x desc",
            "更新者ID",
        )
    if obj.get("optype") == "attachmenttypes.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "attachmenttypes.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "attachmenttypes.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "attachmenttypes.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "attachmenttypes.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.attachmenttypes group by updatedby",
            "更新者ID",
        )
    # repkwkwortsubmkwkwissionhkwkwistkwkwories(报告提交历史表)->repkwkwortid(报告ID)

    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkwortid_pie"
    ):
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkwortid order by x desc",
            "报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkwortid_pie_v1"
    ):
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkwortid",
            "报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkwortid_pie_v2"
    ):
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkwortid",
            "报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkwortid_line"
    ):
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkwortid",
            "报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkwortid_bar"
    ):
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkwortid",
            "报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkwortid_bar_v1"
    ):
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkwortid",
            "报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.submkwkwissiondate_line"
    ):
        res = get_line(
            "select submkwkwissiondate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by submkwkwissiondate order by x",
            "提交日期",
        )
    # repkwkwortsubmkwkwissionhkwkwistkwkwories(报告提交历史表)->employeeid(员工ID)

    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.employeeid_pie":
        res = get_pie(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by employeeid order by x desc",
            "员工ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.employeeid_pie_v1"
    ):
        res = get_pie_v1(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by employeeid",
            "员工ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.employeeid_pie_v2"
    ):
        res = get_pie_v2(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.employeeid_line":
        res = get_line(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by employeeid",
            "员工ID",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.employeeid_bar":
        res = get_bar(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by employeeid",
            "员工ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.employeeid_bar_v1"
    ):
        res = get_bar_v1(
            "select employeeid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by employeeid",
            "员工ID",
        )
    # repkwkwortsubmkwkwissionhkwkwistkwkwories(报告提交历史表)->repkwkworttitle(报告标题)

    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkworttitle_pie"
    ):
        res = get_pie(
            "select repkwkworttitle x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkworttitle order by x desc",
            "报告标题",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkworttitle_pie_v1"
    ):
        res = get_pie_v1(
            "select repkwkworttitle x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkworttitle",
            "报告标题",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkworttitle_pie_v2"
    ):
        res = get_pie_v2(
            "select repkwkworttitle x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkworttitle",
            "报告标题",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkworttitle_line"
    ):
        res = get_line(
            "select repkwkworttitle x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkworttitle",
            "报告标题",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkworttitle_bar"
    ):
        res = get_bar(
            "select repkwkworttitle x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkworttitle",
            "报告标题",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.repkwkworttitle_bar_v1"
    ):
        res = get_bar_v1(
            "select repkwkworttitle x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by repkwkworttitle",
            "报告标题",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.description_wordcloud"
    ):
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkwortsubmkwkwissionhkwkwistkwkwories(报告提交历史表)->status(状态)

    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by status",
            "状态",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approvaldate_line"
    ):
        res = get_line(
            "select approvaldate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approvaldate order by x",
            "审批日期",
        )
    # repkwkwortsubmkwkwissionhkwkwistkwkwories(报告提交历史表)->approverid(审批人ID)

    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approverid_pie":
        res = get_pie(
            "select approverid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approverid order by x desc",
            "审批人ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approverid_pie_v1"
    ):
        res = get_pie_v1(
            "select approverid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approverid",
            "审批人ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approverid_pie_v2"
    ):
        res = get_pie_v2(
            "select approverid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approverid",
            "审批人ID",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approverid_line":
        res = get_line(
            "select approverid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approverid",
            "审批人ID",
        )
    if obj.get("optype") == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approverid_bar":
        res = get_bar(
            "select approverid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approverid",
            "审批人ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.approverid_bar_v1"
    ):
        res = get_bar_v1(
            "select approverid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by approverid",
            "审批人ID",
        )
    # repkwkwortsubmkwkwissionhkwkwistkwkwories(报告提交历史表)->departmentid(部门ID)

    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.departmentid_pie"
    ):
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by departmentid order by x desc",
            "部门ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.departmentid_pie_v1"
    ):
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by departmentid",
            "部门ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.departmentid_pie_v2"
    ):
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by departmentid",
            "部门ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.departmentid_line"
    ):
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by departmentid",
            "部门ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.departmentid_bar"
    ):
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by departmentid",
            "部门ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortsubmkwkwissionhkwkwistkwkwories.departmentid_bar_v1"
    ):
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortsubmkwkwissionhkwkwistkwkwories group by departmentid",
            "部门ID",
        )
    # repkwkwortmodkwkwificationhkwkwistkwkwories(报告修改历史表)->repkwkwortid(关联的报告ID)

    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.repkwkwortid_pie"
    ):
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by repkwkwortid order by x desc",
            "关联的报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.repkwkwortid_pie_v1"
    ):
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by repkwkwortid",
            "关联的报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.repkwkwortid_pie_v2"
    ):
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by repkwkwortid",
            "关联的报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.repkwkwortid_line"
    ):
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by repkwkwortid",
            "关联的报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.repkwkwortid_bar"
    ):
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by repkwkwortid",
            "关联的报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.repkwkwortid_bar_v1"
    ):
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by repkwkwortid",
            "关联的报告ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwificationtime_line"
    ):
        res = get_line(
            "select modkwkwificationtime x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwificationtime order by x",
            "修改时间",
        )
    # repkwkwortmodkwkwificationhkwkwistkwkwories(报告修改历史表)->modkwkwifierid(修改者ID)

    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifierid_pie"
    ):
        res = get_pie(
            "select modkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwifierid order by x desc",
            "修改者ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifierid_pie_v1"
    ):
        res = get_pie_v1(
            "select modkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwifierid",
            "修改者ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifierid_pie_v2"
    ):
        res = get_pie_v2(
            "select modkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwifierid",
            "修改者ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifierid_line"
    ):
        res = get_line(
            "select modkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwifierid",
            "修改者ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifierid_bar"
    ):
        res = get_bar(
            "select modkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwifierid",
            "修改者ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifierid_bar_v1"
    ):
        res = get_bar_v1(
            "select modkwkwifierid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by modkwkwifierid",
            "修改者ID",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.previouscontent_wordcloud"
    ):
        textlist = get_data(
            "SELECT previouscontent result FROM vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwifiedcontent_wordcloud"
    ):
        textlist = get_data(
            "SELECT modkwkwifiedcontent result FROM vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.modkwkwificationtype_wordcloud"
    ):
        textlist = get_data(
            "SELECT modkwkwificationtype result FROM vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkwortmodkwkwificationhkwkwistkwkwories(报告修改历史表)->comment(修改备注)

    if obj.get("optype") == "repkwkwortmodkwkwificationhkwkwistkwkwories.comment_pie":
        res = get_pie(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by comment order by x desc",
            "修改备注",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.comment_pie_v1"
    ):
        res = get_pie_v1(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by comment",
            "修改备注",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.comment_pie_v2"
    ):
        res = get_pie_v2(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by comment",
            "修改备注",
        )
    if obj.get("optype") == "repkwkwortmodkwkwificationhkwkwistkwkwories.comment_line":
        res = get_line(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by comment",
            "修改备注",
        )
    if obj.get("optype") == "repkwkwortmodkwkwificationhkwkwistkwkwories.comment_bar":
        res = get_bar(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by comment",
            "修改备注",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.comment_bar_v1"
    ):
        res = get_bar_v1(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by comment",
            "修改备注",
        )
    # repkwkwortmodkwkwificationhkwkwistkwkwories(报告修改历史表)->kwkwislatest(是否为最新修改用于快速检索最新记录)

    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.kwkwislatest_pie"
    ):
        res = get_pie(
            "select kwkwislatest x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by kwkwislatest order by x desc",
            "是否为最新修改用于快速检索最新记录",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.kwkwislatest_pie_v1"
    ):
        res = get_pie_v1(
            "select kwkwislatest x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by kwkwislatest",
            "是否为最新修改用于快速检索最新记录",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.kwkwislatest_pie_v2"
    ):
        res = get_pie_v2(
            "select kwkwislatest x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by kwkwislatest",
            "是否为最新修改用于快速检索最新记录",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.kwkwislatest_line"
    ):
        res = get_line(
            "select kwkwislatest x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by kwkwislatest",
            "是否为最新修改用于快速检索最新记录",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.kwkwislatest_bar"
    ):
        res = get_bar(
            "select kwkwislatest x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by kwkwislatest",
            "是否为最新修改用于快速检索最新记录",
        )
    if (
        obj.get("optype")
        == "repkwkwortmodkwkwificationhkwkwistkwkwories.kwkwislatest_bar_v1"
    ):
        res = get_bar_v1(
            "select kwkwislatest x,count(*) y from vm779_2f88e95faa233d77.repkwkwortmodkwkwificationhkwkwistkwkwories group by kwkwislatest",
            "是否为最新修改用于快速检索最新记录",
        )
    # repkwkwortcomments(报告评论表)->repkwkwortid(报告ID关联字段指向报告的ID)

    if obj.get("optype") == "repkwkwortcomments.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by repkwkwortid order by x desc",
            "报告ID关联字段指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by repkwkwortid",
            "报告ID关联字段指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by repkwkwortid",
            "报告ID关联字段指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by repkwkwortid",
            "报告ID关联字段指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by repkwkwortid",
            "报告ID关联字段指向报告的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by repkwkwortid",
            "报告ID关联字段指向报告的ID",
        )
    # repkwkwortcomments(报告评论表)->userid(用户ID关联字段指向用户的ID)

    if obj.get("optype") == "repkwkwortcomments.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by userid order by x desc",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "repkwkwortcomments.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm779_2f88e95faa233d77.repkwkwortcomments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "repkwkwortcomments.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "repkwkwortcomments.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by updatedat order by x",
            "更新时间",
        )
    # repkwkwortcomments(报告评论表)->kwkwiskwkwdeleted(是否删除逻辑删除标记)

    if obj.get("optype") == "repkwkwortcomments.kwkwiskwkwdeleted_pie":
        res = get_pie(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by kwkwiskwkwdeleted order by x desc",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "repkwkwortcomments.kwkwiskwkwdeleted_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "repkwkwortcomments.kwkwiskwkwdeleted_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "repkwkwortcomments.kwkwiskwkwdeleted_line":
        res = get_line(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "repkwkwortcomments.kwkwiskwkwdeleted_bar":
        res = get_bar(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "repkwkwortcomments.kwkwiskwkwdeleted_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    # repkwkwortcomments(报告评论表)->ratkwkwing(评分可选用于示用户对报告的评分)

    if obj.get("optype") == "repkwkwortcomments.ratkwkwing_pie":
        res = get_pie(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by ratkwkwing order by x desc",
            "评分可选用于示用户对报告的评分",
        )
    if obj.get("optype") == "repkwkwortcomments.ratkwkwing_pie_v1":
        res = get_pie_v1(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by ratkwkwing",
            "评分可选用于示用户对报告的评分",
        )
    if obj.get("optype") == "repkwkwortcomments.ratkwkwing_pie_v2":
        res = get_pie_v2(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by ratkwkwing",
            "评分可选用于示用户对报告的评分",
        )
    if obj.get("optype") == "repkwkwortcomments.ratkwkwing_line":
        res = get_line(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by ratkwkwing",
            "评分可选用于示用户对报告的评分",
        )
    if obj.get("optype") == "repkwkwortcomments.ratkwkwing_bar":
        res = get_bar(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by ratkwkwing",
            "评分可选用于示用户对报告的评分",
        )
    if obj.get("optype") == "repkwkwortcomments.ratkwkwing_bar_v1":
        res = get_bar_v1(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortcomments group by ratkwkwing",
            "评分可选用于示用户对报告的评分",
        )
    if obj.get("optype") == "repkwkwortcomments.status_wordcloud":
        textlist = get_data(
            "SELECT status result FROM vm779_2f88e95faa233d77.repkwkwortcomments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # commentreplies(评论回复表)->commentid(评论ID关联字段指向评论的ID)

    if obj.get("optype") == "commentreplies.commentid_pie":
        res = get_pie(
            "select commentid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by commentid order by x desc",
            "评论ID关联字段指向评论的ID",
        )
    if obj.get("optype") == "commentreplies.commentid_pie_v1":
        res = get_pie_v1(
            "select commentid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by commentid",
            "评论ID关联字段指向评论的ID",
        )
    if obj.get("optype") == "commentreplies.commentid_pie_v2":
        res = get_pie_v2(
            "select commentid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by commentid",
            "评论ID关联字段指向评论的ID",
        )
    if obj.get("optype") == "commentreplies.commentid_line":
        res = get_line(
            "select commentid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by commentid",
            "评论ID关联字段指向评论的ID",
        )
    if obj.get("optype") == "commentreplies.commentid_bar":
        res = get_bar(
            "select commentid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by commentid",
            "评论ID关联字段指向评论的ID",
        )
    if obj.get("optype") == "commentreplies.commentid_bar_v1":
        res = get_bar_v1(
            "select commentid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by commentid",
            "评论ID关联字段指向评论的ID",
        )
    # commentreplies(评论回复表)->userid(用户ID关联字段指向用户的ID)

    if obj.get("optype") == "commentreplies.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by userid order by x desc",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "commentreplies.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "commentreplies.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "commentreplies.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "commentreplies.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "commentreplies.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "commentreplies.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm779_2f88e95faa233d77.commentreplies;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "commentreplies.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "commentreplies.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by updatedat order by x",
            "更新时间",
        )
    # commentreplies(评论回复表)->kwkwiskwkwdeleted(是否删除逻辑删除标记)

    if obj.get("optype") == "commentreplies.kwkwiskwkwdeleted_pie":
        res = get_pie(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by kwkwiskwkwdeleted order by x desc",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "commentreplies.kwkwiskwkwdeleted_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "commentreplies.kwkwiskwkwdeleted_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "commentreplies.kwkwiskwkwdeleted_line":
        res = get_line(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "commentreplies.kwkwiskwkwdeleted_bar":
        res = get_bar(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "commentreplies.kwkwiskwkwdeleted_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    # commentreplies(评论回复表)->likecount(点赞数)

    if obj.get("optype") == "commentreplies.likecount_pie":
        res = get_pie(
            "select likecount x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by likecount order by x desc",
            "点赞数",
        )
    if obj.get("optype") == "commentreplies.likecount_pie_v1":
        res = get_pie_v1(
            "select likecount x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "commentreplies.likecount_pie_v2":
        res = get_pie_v2(
            "select likecount x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "commentreplies.likecount_line":
        res = get_line(
            "select likecount x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "commentreplies.likecount_bar":
        res = get_bar(
            "select likecount x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "commentreplies.likecount_bar_v1":
        res = get_bar_v1(
            "select likecount x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by likecount",
            "点赞数",
        )
    # commentreplies(评论回复表)->replytoid(回复的回复ID用于构建回复链关联字段指向本的ID)

    if obj.get("optype") == "commentreplies.replytoid_pie":
        res = get_pie(
            "select replytoid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by replytoid order by x desc",
            "回复的回复ID用于构建回复链关联字段指向本的ID",
        )
    if obj.get("optype") == "commentreplies.replytoid_pie_v1":
        res = get_pie_v1(
            "select replytoid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by replytoid",
            "回复的回复ID用于构建回复链关联字段指向本的ID",
        )
    if obj.get("optype") == "commentreplies.replytoid_pie_v2":
        res = get_pie_v2(
            "select replytoid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by replytoid",
            "回复的回复ID用于构建回复链关联字段指向本的ID",
        )
    if obj.get("optype") == "commentreplies.replytoid_line":
        res = get_line(
            "select replytoid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by replytoid",
            "回复的回复ID用于构建回复链关联字段指向本的ID",
        )
    if obj.get("optype") == "commentreplies.replytoid_bar":
        res = get_bar(
            "select replytoid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by replytoid",
            "回复的回复ID用于构建回复链关联字段指向本的ID",
        )
    if obj.get("optype") == "commentreplies.replytoid_bar_v1":
        res = get_bar_v1(
            "select replytoid x,count(*) y from vm779_2f88e95faa233d77.commentreplies group by replytoid",
            "回复的回复ID用于构建回复链关联字段指向本的ID",
        )
    # repkwkwortratkwkwings(报告评分表)->repkwkwortid(报告ID唯一标识一个报告)

    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortid order by x desc",
            "报告ID唯一标识一个报告",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortid",
            "报告ID唯一标识一个报告",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortid",
            "报告ID唯一标识一个报告",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortid",
            "报告ID唯一标识一个报告",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortid",
            "报告ID唯一标识一个报告",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortid",
            "报告ID唯一标识一个报告",
        )
    # repkwkwortratkwkwings(报告评分表)->ratkwkwing(评分示对报告的评分可以是数值类型)

    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwing_pie":
        res = get_pie(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwing order by x desc",
            "评分示对报告的评分可以是数值类型",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwing_pie_v1":
        res = get_pie_v1(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwing",
            "评分示对报告的评分可以是数值类型",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwing_pie_v2":
        res = get_pie_v2(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwing",
            "评分示对报告的评分可以是数值类型",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwing_line":
        res = get_line(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwing",
            "评分示对报告的评分可以是数值类型",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwing_bar":
        res = get_bar(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwing",
            "评分示对报告的评分可以是数值类型",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwing_bar_v1":
        res = get_bar_v1(
            "select ratkwkwing x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwing",
            "评分示对报告的评分可以是数值类型",
        )
    # repkwkwortratkwkwings(报告评分表)->raterid(评分者ID示哪个用户或系统对报告进行了评分)

    if obj.get("optype") == "repkwkwortratkwkwings.raterid_pie":
        res = get_pie(
            "select raterid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by raterid order by x desc",
            "评分者ID示哪个用户或系统对报告进行了评分",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.raterid_pie_v1":
        res = get_pie_v1(
            "select raterid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by raterid",
            "评分者ID示哪个用户或系统对报告进行了评分",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.raterid_pie_v2":
        res = get_pie_v2(
            "select raterid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by raterid",
            "评分者ID示哪个用户或系统对报告进行了评分",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.raterid_line":
        res = get_line(
            "select raterid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by raterid",
            "评分者ID示哪个用户或系统对报告进行了评分",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.raterid_bar":
        res = get_bar(
            "select raterid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by raterid",
            "评分者ID示哪个用户或系统对报告进行了评分",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.raterid_bar_v1":
        res = get_bar_v1(
            "select raterid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by raterid",
            "评分者ID示哪个用户或系统对报告进行了评分",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.repkwkwortdate_line":
        res = get_line(
            "select repkwkwortdate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by repkwkwortdate order by x",
            "报告日期报告提交的日期",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.ratkwkwingdate_line":
        res = get_line(
            "select ratkwkwingdate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by ratkwkwingdate order by x",
            "评分日期对报告进行评分的日期",
        )
    # repkwkwortratkwkwings(报告评分表)->comment(评语对报告的额外评语或反馈)

    if obj.get("optype") == "repkwkwortratkwkwings.comment_pie":
        res = get_pie(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by comment order by x desc",
            "评语对报告的额外评语或反馈",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.comment_pie_v1":
        res = get_pie_v1(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by comment",
            "评语对报告的额外评语或反馈",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.comment_pie_v2":
        res = get_pie_v2(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by comment",
            "评语对报告的额外评语或反馈",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.comment_line":
        res = get_line(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by comment",
            "评语对报告的额外评语或反馈",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.comment_bar":
        res = get_bar(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by comment",
            "评语对报告的额外评语或反馈",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.comment_bar_v1":
        res = get_bar_v1(
            "select comment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by comment",
            "评语对报告的额外评语或反馈",
        )
    # repkwkwortratkwkwings(报告评分表)->kwkwisapproved(是否通过示报告是否通过审核)

    if obj.get("optype") == "repkwkwortratkwkwings.kwkwisapproved_pie":
        res = get_pie(
            "select kwkwisapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by kwkwisapproved order by x desc",
            "是否通过示报告是否通过审核",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.kwkwisapproved_pie_v1":
        res = get_pie_v1(
            "select kwkwisapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by kwkwisapproved",
            "是否通过示报告是否通过审核",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.kwkwisapproved_pie_v2":
        res = get_pie_v2(
            "select kwkwisapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by kwkwisapproved",
            "是否通过示报告是否通过审核",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.kwkwisapproved_line":
        res = get_line(
            "select kwkwisapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by kwkwisapproved",
            "是否通过示报告是否通过审核",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.kwkwisapproved_bar":
        res = get_bar(
            "select kwkwisapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by kwkwisapproved",
            "是否通过示报告是否通过审核",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.kwkwisapproved_bar_v1":
        res = get_bar_v1(
            "select kwkwisapproved x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by kwkwisapproved",
            "是否通过示报告是否通过审核",
        )
    # repkwkwortratkwkwings(报告评分表)->categkwkworyid(类别ID关联字段示报告所属的类别)

    if obj.get("optype") == "repkwkwortratkwkwings.categkwkworyid_pie":
        res = get_pie(
            "select categkwkworyid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by categkwkworyid order by x desc",
            "类别ID关联字段示报告所属的类别",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.categkwkworyid_pie_v1":
        res = get_pie_v1(
            "select categkwkworyid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by categkwkworyid",
            "类别ID关联字段示报告所属的类别",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.categkwkworyid_pie_v2":
        res = get_pie_v2(
            "select categkwkworyid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by categkwkworyid",
            "类别ID关联字段示报告所属的类别",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.categkwkworyid_line":
        res = get_line(
            "select categkwkworyid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by categkwkworyid",
            "类别ID关联字段示报告所属的类别",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.categkwkworyid_bar":
        res = get_bar(
            "select categkwkworyid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by categkwkworyid",
            "类别ID关联字段示报告所属的类别",
        )
    if obj.get("optype") == "repkwkwortratkwkwings.categkwkworyid_bar_v1":
        res = get_bar_v1(
            "select categkwkworyid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortratkwkwings group by categkwkworyid",
            "类别ID关联字段示报告所属的类别",
        )
    # ratkwkwingcriteria(评分标准表)->criterianame(评分标准名称)

    if obj.get("optype") == "ratkwkwingcriteria.criterianame_pie":
        res = get_pie(
            "select criterianame x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by criterianame order by x desc",
            "评分标准名称",
        )
    if obj.get("optype") == "ratkwkwingcriteria.criterianame_pie_v1":
        res = get_pie_v1(
            "select criterianame x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by criterianame",
            "评分标准名称",
        )
    if obj.get("optype") == "ratkwkwingcriteria.criterianame_pie_v2":
        res = get_pie_v2(
            "select criterianame x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by criterianame",
            "评分标准名称",
        )
    if obj.get("optype") == "ratkwkwingcriteria.criterianame_line":
        res = get_line(
            "select criterianame x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by criterianame",
            "评分标准名称",
        )
    if obj.get("optype") == "ratkwkwingcriteria.criterianame_bar":
        res = get_bar(
            "select criterianame x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by criterianame",
            "评分标准名称",
        )
    if obj.get("optype") == "ratkwkwingcriteria.criterianame_bar_v1":
        res = get_bar_v1(
            "select criterianame x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by criterianame",
            "评分标准名称",
        )
    if obj.get("optype") == "ratkwkwingcriteria.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.ratkwkwingcriteria;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # ratkwkwingcriteria(评分标准表)->categkwkwory(类别)

    if obj.get("optype") == "ratkwkwingcriteria.categkwkwory_pie":
        res = get_pie(
            "select categkwkwory x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by categkwkwory order by x desc",
            "类别",
        )
    if obj.get("optype") == "ratkwkwingcriteria.categkwkwory_pie_v1":
        res = get_pie_v1(
            "select categkwkwory x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by categkwkwory",
            "类别",
        )
    if obj.get("optype") == "ratkwkwingcriteria.categkwkwory_pie_v2":
        res = get_pie_v2(
            "select categkwkwory x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by categkwkwory",
            "类别",
        )
    if obj.get("optype") == "ratkwkwingcriteria.categkwkwory_line":
        res = get_line(
            "select categkwkwory x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by categkwkwory",
            "类别",
        )
    if obj.get("optype") == "ratkwkwingcriteria.categkwkwory_bar":
        res = get_bar(
            "select categkwkwory x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by categkwkwory",
            "类别",
        )
    if obj.get("optype") == "ratkwkwingcriteria.categkwkwory_bar_v1":
        res = get_bar_v1(
            "select categkwkwory x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by categkwkwory",
            "类别",
        )
    # ratkwkwingcriteria(评分标准表)->weight(权重)

    if obj.get("optype") == "ratkwkwingcriteria.weight_pie":
        res = get_pie(
            "select weight x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by weight order by x desc",
            "权重",
        )
    if obj.get("optype") == "ratkwkwingcriteria.weight_pie_v1":
        res = get_pie_v1(
            "select weight x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by weight",
            "权重",
        )
    if obj.get("optype") == "ratkwkwingcriteria.weight_pie_v2":
        res = get_pie_v2(
            "select weight x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by weight",
            "权重",
        )
    if obj.get("optype") == "ratkwkwingcriteria.weight_line":
        res = get_line(
            "select weight x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by weight",
            "权重",
        )
    if obj.get("optype") == "ratkwkwingcriteria.weight_bar":
        res = get_bar(
            "select weight x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by weight",
            "权重",
        )
    if obj.get("optype") == "ratkwkwingcriteria.weight_bar_v1":
        res = get_bar_v1(
            "select weight x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by weight",
            "权重",
        )
    # ratkwkwingcriteria(评分标准表)->kwkwisactive(是否激活)

    if obj.get("optype") == "ratkwkwingcriteria.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by kwkwisactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "ratkwkwingcriteria.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "ratkwkwingcriteria.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "ratkwkwingcriteria.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "ratkwkwingcriteria.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "ratkwkwingcriteria.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "ratkwkwingcriteria.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "ratkwkwingcriteria.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by updatedat order by x",
            "更新时间",
        )
    # ratkwkwingcriteria(评分标准表)->relateditemid(关联项目ID)

    if obj.get("optype") == "ratkwkwingcriteria.relateditemid_pie":
        res = get_pie(
            "select relateditemid x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemid order by x desc",
            "关联项目ID",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemid_pie_v1":
        res = get_pie_v1(
            "select relateditemid x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemid",
            "关联项目ID",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemid_pie_v2":
        res = get_pie_v2(
            "select relateditemid x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemid",
            "关联项目ID",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemid_line":
        res = get_line(
            "select relateditemid x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemid",
            "关联项目ID",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemid_bar":
        res = get_bar(
            "select relateditemid x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemid",
            "关联项目ID",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemid_bar_v1":
        res = get_bar_v1(
            "select relateditemid x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemid",
            "关联项目ID",
        )
    # ratkwkwingcriteria(评分标准表)->relateditemtype(关联项目类型)

    if obj.get("optype") == "ratkwkwingcriteria.relateditemtype_pie":
        res = get_pie(
            "select relateditemtype x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemtype order by x desc",
            "关联项目类型",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemtype_pie_v1":
        res = get_pie_v1(
            "select relateditemtype x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemtype",
            "关联项目类型",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemtype_pie_v2":
        res = get_pie_v2(
            "select relateditemtype x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemtype",
            "关联项目类型",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemtype_line":
        res = get_line(
            "select relateditemtype x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemtype",
            "关联项目类型",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemtype_bar":
        res = get_bar(
            "select relateditemtype x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemtype",
            "关联项目类型",
        )
    if obj.get("optype") == "ratkwkwingcriteria.relateditemtype_bar_v1":
        res = get_bar_v1(
            "select relateditemtype x,count(*) y from vm779_2f88e95faa233d77.ratkwkwingcriteria group by relateditemtype",
            "关联项目类型",
        )
    # permkwkwissions(权限表)->name(权限名称)

    if obj.get("optype") == "permkwkwissions.name_pie":
        res = get_pie(
            "select name x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by name order by x desc",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_pie_v1":
        res = get_pie_v1(
            "select name x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_pie_v2":
        res = get_pie_v2(
            "select name x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_line":
        res = get_line(
            "select name x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_bar":
        res = get_bar(
            "select name x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_bar_v1":
        res = get_bar_v1(
            "select name x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.permkwkwissions;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "permkwkwissions.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "permkwkwissions.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by updatedat order by x",
            "更新时间",
        )
    # permkwkwissions(权限表)->kwkwisactive(是否激活用于控制权限是否可用)

    if obj.get("optype") == "permkwkwissions.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by kwkwisactive order by x desc",
            "是否激活用于控制权限是否可用",
        )
    if obj.get("optype") == "permkwkwissions.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by kwkwisactive",
            "是否激活用于控制权限是否可用",
        )
    if obj.get("optype") == "permkwkwissions.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by kwkwisactive",
            "是否激活用于控制权限是否可用",
        )
    if obj.get("optype") == "permkwkwissions.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by kwkwisactive",
            "是否激活用于控制权限是否可用",
        )
    if obj.get("optype") == "permkwkwissions.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by kwkwisactive",
            "是否激活用于控制权限是否可用",
        )
    if obj.get("optype") == "permkwkwissions.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by kwkwisactive",
            "是否激活用于控制权限是否可用",
        )
    # permkwkwissions(权限表)->parentid(父权限ID用于构建权限层级关系)

    if obj.get("optype") == "permkwkwissions.parentid_pie":
        res = get_pie(
            "select parentid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by parentid order by x desc",
            "父权限ID用于构建权限层级关系",
        )
    if obj.get("optype") == "permkwkwissions.parentid_pie_v1":
        res = get_pie_v1(
            "select parentid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by parentid",
            "父权限ID用于构建权限层级关系",
        )
    if obj.get("optype") == "permkwkwissions.parentid_pie_v2":
        res = get_pie_v2(
            "select parentid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by parentid",
            "父权限ID用于构建权限层级关系",
        )
    if obj.get("optype") == "permkwkwissions.parentid_line":
        res = get_line(
            "select parentid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by parentid",
            "父权限ID用于构建权限层级关系",
        )
    if obj.get("optype") == "permkwkwissions.parentid_bar":
        res = get_bar(
            "select parentid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by parentid",
            "父权限ID用于构建权限层级关系",
        )
    if obj.get("optype") == "permkwkwissions.parentid_bar_v1":
        res = get_bar_v1(
            "select parentid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by parentid",
            "父权限ID用于构建权限层级关系",
        )
    # permkwkwissions(权限表)->roleid(关联角色ID示该权限属于哪个角色)

    if obj.get("optype") == "permkwkwissions.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by roleid order by x desc",
            "关联角色ID示该权限属于哪个角色",
        )
    if obj.get("optype") == "permkwkwissions.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by roleid",
            "关联角色ID示该权限属于哪个角色",
        )
    if obj.get("optype") == "permkwkwissions.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by roleid",
            "关联角色ID示该权限属于哪个角色",
        )
    if obj.get("optype") == "permkwkwissions.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by roleid",
            "关联角色ID示该权限属于哪个角色",
        )
    if obj.get("optype") == "permkwkwissions.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by roleid",
            "关联角色ID示该权限属于哪个角色",
        )
    if obj.get("optype") == "permkwkwissions.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by roleid",
            "关联角色ID示该权限属于哪个角色",
        )
    # permkwkwissions(权限表)->systemmodule(所属系统模块标识权限属于哪个系统模块或功能区域)

    if obj.get("optype") == "permkwkwissions.systemmodule_pie":
        res = get_pie(
            "select systemmodule x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by systemmodule order by x desc",
            "所属系统模块标识权限属于哪个系统模块或功能区域",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_pie_v1":
        res = get_pie_v1(
            "select systemmodule x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by systemmodule",
            "所属系统模块标识权限属于哪个系统模块或功能区域",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_pie_v2":
        res = get_pie_v2(
            "select systemmodule x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by systemmodule",
            "所属系统模块标识权限属于哪个系统模块或功能区域",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_line":
        res = get_line(
            "select systemmodule x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by systemmodule",
            "所属系统模块标识权限属于哪个系统模块或功能区域",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_bar":
        res = get_bar(
            "select systemmodule x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by systemmodule",
            "所属系统模块标识权限属于哪个系统模块或功能区域",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_bar_v1":
        res = get_bar_v1(
            "select systemmodule x,count(*) y from vm779_2f88e95faa233d77.permkwkwissions group by systemmodule",
            "所属系统模块标识权限属于哪个系统模块或功能区域",
        )
    # permkwkwissionrolerelations(权限角色关联表)->permkwkwissionid(权限ID)

    if obj.get("optype") == "permkwkwissionrolerelations.permkwkwissionid_pie":
        res = get_pie(
            "select permkwkwissionid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by permkwkwissionid order by x desc",
            "权限ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.permkwkwissionid_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.permkwkwissionid_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.permkwkwissionid_line":
        res = get_line(
            "select permkwkwissionid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.permkwkwissionid_bar":
        res = get_bar(
            "select permkwkwissionid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.permkwkwissionid_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by permkwkwissionid",
            "权限ID",
        )
    # permkwkwissionrolerelations(权限角色关联表)->roleid(角色ID)

    if obj.get("optype") == "permkwkwissionrolerelations.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by roleid order by x desc",
            "角色ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by updatedat order by x",
            "更新时间",
        )
    # permkwkwissionrolerelations(权限角色关联表)->creatkwkworid(创建者ID)

    if obj.get("optype") == "permkwkwissionrolerelations.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by creatkwkworid order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by creatkwkworid",
            "创建者ID",
        )
    # permkwkwissionrolerelations(权限角色关联表)->kwkwisactive(是否激活用于控制权限是否有效)

    if obj.get("optype") == "permkwkwissionrolerelations.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by kwkwisactive order by x desc",
            "是否激活用于控制权限是否有效",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by kwkwisactive",
            "是否激活用于控制权限是否有效",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by kwkwisactive",
            "是否激活用于控制权限是否有效",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by kwkwisactive",
            "是否激活用于控制权限是否有效",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by kwkwisactive",
            "是否激活用于控制权限是否有效",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm779_2f88e95faa233d77.permkwkwissionrolerelations group by kwkwisactive",
            "是否激活用于控制权限是否有效",
        )
    if obj.get("optype") == "permkwkwissionrolerelations.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.permkwkwissionrolerelations;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # systemlogs(系统日志表)->logid(日志ID)

    if obj.get("optype") == "systemlogs.logid_pie":
        res = get_pie(
            "select logid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logid order by x desc",
            "日志ID",
        )
    if obj.get("optype") == "systemlogs.logid_pie_v1":
        res = get_pie_v1(
            "select logid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logid",
            "日志ID",
        )
    if obj.get("optype") == "systemlogs.logid_pie_v2":
        res = get_pie_v2(
            "select logid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logid",
            "日志ID",
        )
    if obj.get("optype") == "systemlogs.logid_line":
        res = get_line(
            "select logid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logid",
            "日志ID",
        )
    if obj.get("optype") == "systemlogs.logid_bar":
        res = get_bar(
            "select logid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logid",
            "日志ID",
        )
    if obj.get("optype") == "systemlogs.logid_bar_v1":
        res = get_bar_v1(
            "select logid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logid",
            "日志ID",
        )
    if obj.get("optype") == "systemlogs.logtime_line":
        res = get_line(
            "select logtime x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by logtime order by x",
            "日志时间",
        )
    # systemlogs(系统日志表)->userid(用户ID)

    if obj.get("optype") == "systemlogs.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "systemlogs.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by userid",
            "用户ID",
        )
    if obj.get("optype") == "systemlogs.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by userid",
            "用户ID",
        )
    if obj.get("optype") == "systemlogs.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by userid",
            "用户ID",
        )
    if obj.get("optype") == "systemlogs.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by userid",
            "用户ID",
        )
    if obj.get("optype") == "systemlogs.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by userid",
            "用户ID",
        )
    # systemlogs(系统日志表)->action(操作类型)

    if obj.get("optype") == "systemlogs.action_pie":
        res = get_pie(
            "select action x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by action order by x desc",
            "操作类型",
        )
    if obj.get("optype") == "systemlogs.action_pie_v1":
        res = get_pie_v1(
            "select action x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by action",
            "操作类型",
        )
    if obj.get("optype") == "systemlogs.action_pie_v2":
        res = get_pie_v2(
            "select action x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by action",
            "操作类型",
        )
    if obj.get("optype") == "systemlogs.action_line":
        res = get_line(
            "select action x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by action",
            "操作类型",
        )
    if obj.get("optype") == "systemlogs.action_bar":
        res = get_bar(
            "select action x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by action",
            "操作类型",
        )
    if obj.get("optype") == "systemlogs.action_bar_v1":
        res = get_bar_v1(
            "select action x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by action",
            "操作类型",
        )
    # systemlogs(系统日志表)->modulename(模块名称)

    if obj.get("optype") == "systemlogs.modulename_pie":
        res = get_pie(
            "select modulename x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by modulename order by x desc",
            "模块名称",
        )
    if obj.get("optype") == "systemlogs.modulename_pie_v1":
        res = get_pie_v1(
            "select modulename x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by modulename",
            "模块名称",
        )
    if obj.get("optype") == "systemlogs.modulename_pie_v2":
        res = get_pie_v2(
            "select modulename x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by modulename",
            "模块名称",
        )
    if obj.get("optype") == "systemlogs.modulename_line":
        res = get_line(
            "select modulename x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by modulename",
            "模块名称",
        )
    if obj.get("optype") == "systemlogs.modulename_bar":
        res = get_bar(
            "select modulename x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by modulename",
            "模块名称",
        )
    if obj.get("optype") == "systemlogs.modulename_bar_v1":
        res = get_bar_v1(
            "select modulename x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by modulename",
            "模块名称",
        )
    if obj.get("optype") == "systemlogs.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.systemlogs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # systemlogs(系统日志表)->result(操作结果)

    if obj.get("optype") == "systemlogs.result_pie":
        res = get_pie(
            "select result x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by result order by x desc",
            "操作结果",
        )
    if obj.get("optype") == "systemlogs.result_pie_v1":
        res = get_pie_v1(
            "select result x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by result",
            "操作结果",
        )
    if obj.get("optype") == "systemlogs.result_pie_v2":
        res = get_pie_v2(
            "select result x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by result",
            "操作结果",
        )
    if obj.get("optype") == "systemlogs.result_line":
        res = get_line(
            "select result x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by result",
            "操作结果",
        )
    if obj.get("optype") == "systemlogs.result_bar":
        res = get_bar(
            "select result x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by result",
            "操作结果",
        )
    if obj.get("optype") == "systemlogs.result_bar_v1":
        res = get_bar_v1(
            "select result x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by result",
            "操作结果",
        )
    if obj.get("optype") == "systemlogs.ipaddressip_wordcloud":
        textlist = get_data(
            "SELECT ipaddressip result FROM vm779_2f88e95faa233d77.systemlogs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # systemlogs(系统日志表)->relatedid(关联ID)

    if obj.get("optype") == "systemlogs.relatedid_pie":
        res = get_pie(
            "select relatedid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by relatedid order by x desc",
            "关联ID",
        )
    if obj.get("optype") == "systemlogs.relatedid_pie_v1":
        res = get_pie_v1(
            "select relatedid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by relatedid",
            "关联ID",
        )
    if obj.get("optype") == "systemlogs.relatedid_pie_v2":
        res = get_pie_v2(
            "select relatedid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by relatedid",
            "关联ID",
        )
    if obj.get("optype") == "systemlogs.relatedid_line":
        res = get_line(
            "select relatedid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by relatedid",
            "关联ID",
        )
    if obj.get("optype") == "systemlogs.relatedid_bar":
        res = get_bar(
            "select relatedid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by relatedid",
            "关联ID",
        )
    if obj.get("optype") == "systemlogs.relatedid_bar_v1":
        res = get_bar_v1(
            "select relatedid x,count(*) y from vm779_2f88e95faa233d77.systemlogs group by relatedid",
            "关联ID",
        )
    # repkwkwortconfigurations(报表配置表)->repkwkwortid(报ID)

    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortid order by x desc",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortid",
            "报ID",
        )
    # repkwkwortconfigurations(报表配置表)->repkwkwortname(报名称)

    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortname_pie":
        res = get_pie(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortname order by x desc",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortname_pie_v1":
        res = get_pie_v1(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortname_pie_v2":
        res = get_pie_v2(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortname_line":
        res = get_line(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortname_bar":
        res = get_bar(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortconfigurations.repkwkwortname_bar_v1":
        res = get_bar_v1(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortconfigurations.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.repkwkwortconfigurations;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkwortconfigurations(报表配置表)->creatkwkwor(创建者)

    if obj.get("optype") == "repkwkwortconfigurations.creatkwkwor_pie":
        res = get_pie(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by creatkwkwor order by x desc",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortconfigurations.creatkwkwor_pie_v1":
        res = get_pie_v1(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortconfigurations.creatkwkwor_pie_v2":
        res = get_pie_v2(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortconfigurations.creatkwkwor_line":
        res = get_line(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortconfigurations.creatkwkwor_bar":
        res = get_bar(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortconfigurations.creatkwkwor_bar_v1":
        res = get_bar_v1(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortconfigurations.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "repkwkwortconfigurations.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by updatetime order by x",
            "更新时间",
        )
    # repkwkwortconfigurations(报表配置表)->isactive(是否激活)

    if obj.get("optype") == "repkwkwortconfigurations.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortconfigurations.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortconfigurations.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortconfigurations.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortconfigurations.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "repkwkwortconfigurations.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by isactive",
            "是否激活",
        )
    # repkwkwortconfigurations(报表配置表)->frequency(报告频率)

    if obj.get("optype") == "repkwkwortconfigurations.frequency_pie":
        res = get_pie(
            "select frequency x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by frequency order by x desc",
            "报告频率",
        )
    if obj.get("optype") == "repkwkwortconfigurations.frequency_pie_v1":
        res = get_pie_v1(
            "select frequency x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by frequency",
            "报告频率",
        )
    if obj.get("optype") == "repkwkwortconfigurations.frequency_pie_v2":
        res = get_pie_v2(
            "select frequency x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by frequency",
            "报告频率",
        )
    if obj.get("optype") == "repkwkwortconfigurations.frequency_line":
        res = get_line(
            "select frequency x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by frequency",
            "报告频率",
        )
    if obj.get("optype") == "repkwkwortconfigurations.frequency_bar":
        res = get_bar(
            "select frequency x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by frequency",
            "报告频率",
        )
    if obj.get("optype") == "repkwkwortconfigurations.frequency_bar_v1":
        res = get_bar_v1(
            "select frequency x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by frequency",
            "报告频率",
        )
    # repkwkwortconfigurations(报表配置表)->departmentid(部门ID)

    if obj.get("optype") == "repkwkwortconfigurations.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by departmentid order by x desc",
            "部门ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "repkwkwortconfigurations.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortconfigurations group by departmentid",
            "部门ID",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->repkwkwortid(报ID关联报)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by repkwkwortid order by x desc",
            "报ID关联报",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by repkwkwortid",
            "报ID关联报",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by repkwkwortid",
            "报ID关联报",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by repkwkwortid",
            "报ID关联报",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by repkwkwortid",
            "报ID关联报",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by repkwkwortid",
            "报ID关联报",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkworttime_line":
        res = get_line(
            "select expkwkworttime x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkworttime order by x",
            "导出时间",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->expkwkwortuser(导出用户)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkwortuser_pie":
        res = get_pie(
            "select expkwkwortuser x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortuser order by x desc",
            "导出用户",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkwortuser_pie_v1":
        res = get_pie_v1(
            "select expkwkwortuser x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortuser",
            "导出用户",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkwortuser_pie_v2":
        res = get_pie_v2(
            "select expkwkwortuser x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortuser",
            "导出用户",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkwortuser_line":
        res = get_line(
            "select expkwkwortuser x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortuser",
            "导出用户",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkwortuser_bar":
        res = get_bar(
            "select expkwkwortuser x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortuser",
            "导出用户",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.expkwkwortuser_bar_v1":
        res = get_bar_v1(
            "select expkwkwortuser x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortuser",
            "导出用户",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->expkwkwortkwkwfkwkwormat(导出格式如PDF)

    if (
        obj.get("optype")
        == "repkwkwortexpkwkwortreckwkwords.expkwkwortkwkwfkwkwormat_pie"
    ):
        res = get_pie(
            "select expkwkwortkwkwfkwkwormat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortkwkwfkwkwormat order by x desc",
            "导出格式如PDF",
        )
    if (
        obj.get("optype")
        == "repkwkwortexpkwkwortreckwkwords.expkwkwortkwkwfkwkwormat_pie_v1"
    ):
        res = get_pie_v1(
            "select expkwkwortkwkwfkwkwormat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortkwkwfkwkwormat",
            "导出格式如PDF",
        )
    if (
        obj.get("optype")
        == "repkwkwortexpkwkwortreckwkwords.expkwkwortkwkwfkwkwormat_pie_v2"
    ):
        res = get_pie_v2(
            "select expkwkwortkwkwfkwkwormat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortkwkwfkwkwormat",
            "导出格式如PDF",
        )
    if (
        obj.get("optype")
        == "repkwkwortexpkwkwortreckwkwords.expkwkwortkwkwfkwkwormat_line"
    ):
        res = get_line(
            "select expkwkwortkwkwfkwkwormat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortkwkwfkwkwormat",
            "导出格式如PDF",
        )
    if (
        obj.get("optype")
        == "repkwkwortexpkwkwortreckwkwords.expkwkwortkwkwfkwkwormat_bar"
    ):
        res = get_bar(
            "select expkwkwortkwkwfkwkwormat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortkwkwfkwkwormat",
            "导出格式如PDF",
        )
    if (
        obj.get("optype")
        == "repkwkwortexpkwkwortreckwkwords.expkwkwortkwkwfkwkwormat_bar_v1"
    ):
        res = get_bar_v1(
            "select expkwkwortkwkwfkwkwormat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by expkwkwortkwkwfkwkwormat",
            "导出格式如PDF",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->filename(文件名)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filename_pie":
        res = get_pie(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filename order by x desc",
            "文件名",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filename_pie_v1":
        res = get_pie_v1(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filename",
            "文件名",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filename_pie_v2":
        res = get_pie_v2(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filename",
            "文件名",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filename_line":
        res = get_line(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filename",
            "文件名",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filename_bar":
        res = get_bar(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filename",
            "文件名",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filename_bar_v1":
        res = get_bar_v1(
            "select filename x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filename",
            "文件名",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->filepath(文件存储路径)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filepath_pie":
        res = get_pie(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filepath order by x desc",
            "文件存储路径",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filepath_pie_v1":
        res = get_pie_v1(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filepath_pie_v2":
        res = get_pie_v2(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filepath_line":
        res = get_line(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filepath_bar":
        res = get_bar(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filepath_bar_v1":
        res = get_bar_v1(
            "select filepath x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filepath",
            "文件存储路径",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->filesize(文件大小单位KB)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filesize_pie":
        res = get_pie(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filesize order by x desc",
            "文件大小单位KB",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filesize_pie_v1":
        res = get_pie_v1(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filesize",
            "文件大小单位KB",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filesize_pie_v2":
        res = get_pie_v2(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filesize",
            "文件大小单位KB",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filesize_line":
        res = get_line(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filesize",
            "文件大小单位KB",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filesize_bar":
        res = get_bar(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filesize",
            "文件大小单位KB",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.filesize_bar_v1":
        res = get_bar_v1(
            "select filesize x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by filesize",
            "文件大小单位KB",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->status(导出状态如成功、失败)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by status order by x desc",
            "导出状态如成功、失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by status",
            "导出状态如成功、失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by status",
            "导出状态如成功、失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by status",
            "导出状态如成功、失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by status",
            "导出状态如成功、失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by status",
            "导出状态如成功、失败",
        )
    # repkwkwortexpkwkwortreckwkwords(报表导出记录表)->errkwkwormessage(错误信息如果导出失败)

    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.errkwkwormessage_pie":
        res = get_pie(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by errkwkwormessage order by x desc",
            "错误信息如果导出失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.errkwkwormessage_pie_v1":
        res = get_pie_v1(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by errkwkwormessage",
            "错误信息如果导出失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.errkwkwormessage_pie_v2":
        res = get_pie_v2(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by errkwkwormessage",
            "错误信息如果导出失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.errkwkwormessage_line":
        res = get_line(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by errkwkwormessage",
            "错误信息如果导出失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.errkwkwormessage_bar":
        res = get_bar(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by errkwkwormessage",
            "错误信息如果导出失败",
        )
    if obj.get("optype") == "repkwkwortexpkwkwortreckwkwords.errkwkwormessage_bar_v1":
        res = get_bar_v1(
            "select errkwkwormessage x,count(*) y from vm779_2f88e95faa233d77.repkwkwortexpkwkwortreckwkwords group by errkwkwormessage",
            "错误信息如果导出失败",
        )
    # repkwkworttemplatefields(报表模板字段表)->templateid(模板ID)

    if obj.get("optype") == "repkwkworttemplatefields.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by templateid order by x desc",
            "模板ID",
        )
    if obj.get("optype") == "repkwkworttemplatefields.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "repkwkworttemplatefields.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "repkwkworttemplatefields.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "repkwkworttemplatefields.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "repkwkworttemplatefields.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by templateid",
            "模板ID",
        )
    # repkwkworttemplatefields(报表模板字段表)->fieldname(字段名称)

    if obj.get("optype") == "repkwkworttemplatefields.fieldname_pie":
        res = get_pie(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldname order by x desc",
            "字段名称",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldname_pie_v1":
        res = get_pie_v1(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldname_pie_v2":
        res = get_pie_v2(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldname_line":
        res = get_line(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldname_bar":
        res = get_bar(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldname_bar_v1":
        res = get_bar_v1(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldname",
            "字段名称",
        )
    # repkwkworttemplatefields(报表模板字段表)->fieldtype(字段类型)

    if obj.get("optype") == "repkwkworttemplatefields.fieldtype_pie":
        res = get_pie(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldtype order by x desc",
            "字段类型",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldtype_pie_v1":
        res = get_pie_v1(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldtype",
            "字段类型",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldtype_pie_v2":
        res = get_pie_v2(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldtype",
            "字段类型",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldtype_line":
        res = get_line(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldtype",
            "字段类型",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldtype_bar":
        res = get_bar(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldtype",
            "字段类型",
        )
    if obj.get("optype") == "repkwkworttemplatefields.fieldtype_bar_v1":
        res = get_bar_v1(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by fieldtype",
            "字段类型",
        )
    # repkwkworttemplatefields(报表模板字段表)->kwkwisrequired(是否必填)

    if obj.get("optype") == "repkwkworttemplatefields.kwkwisrequired_pie":
        res = get_pie(
            "select kwkwisrequired x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwisrequired order by x desc",
            "是否必填",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwisrequired_pie_v1":
        res = get_pie_v1(
            "select kwkwisrequired x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwisrequired",
            "是否必填",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwisrequired_pie_v2":
        res = get_pie_v2(
            "select kwkwisrequired x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwisrequired",
            "是否必填",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwisrequired_line":
        res = get_line(
            "select kwkwisrequired x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwisrequired",
            "是否必填",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwisrequired_bar":
        res = get_bar(
            "select kwkwisrequired x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwisrequired",
            "是否必填",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwisrequired_bar_v1":
        res = get_bar_v1(
            "select kwkwisrequired x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwisrequired",
            "是否必填",
        )
    # repkwkworttemplatefields(报表模板字段表)->kwkwdefaultvalue(默认值)

    if obj.get("optype") == "repkwkworttemplatefields.kwkwdefaultvalue_pie":
        res = get_pie(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwdefaultvalue order by x desc",
            "默认值",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwdefaultvalue_pie_v1":
        res = get_pie_v1(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwdefaultvalue_pie_v2":
        res = get_pie_v2(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwdefaultvalue_line":
        res = get_line(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwdefaultvalue_bar":
        res = get_bar(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkworttemplatefields.kwkwdefaultvalue_bar_v1":
        res = get_bar_v1(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkworttemplatefields.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.repkwkworttemplatefields;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkworttemplatefields(报表模板字段表)->skwkwortorder(排序顺序)

    if obj.get("optype") == "repkwkworttemplatefields.skwkwortorder_pie":
        res = get_pie(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by skwkwortorder order by x desc",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkworttemplatefields.skwkwortorder_pie_v1":
        res = get_pie_v1(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkworttemplatefields.skwkwortorder_pie_v2":
        res = get_pie_v2(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkworttemplatefields.skwkwortorder_line":
        res = get_line(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkworttemplatefields.skwkwortorder_bar":
        res = get_bar(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "repkwkworttemplatefields.skwkwortorder_bar_v1":
        res = get_bar_v1(
            "select skwkwortorder x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by skwkwortorder",
            "排序顺序",
        )
    # repkwkworttemplatefields(报表模板字段表)->createdby(创建人)

    if obj.get("optype") == "repkwkworttemplatefields.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdby order by x desc",
            "创建人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdby",
            "创建人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdby",
            "创建人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdby",
            "创建人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdby",
            "创建人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdby",
            "创建人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by createdat order by x",
            "创建时间",
        )
    # repkwkworttemplatefields(报表模板字段表)->updatedby(更新人)

    if obj.get("optype") == "repkwkworttemplatefields.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedby order by x desc",
            "更新人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedby",
            "更新人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedby",
            "更新人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedby",
            "更新人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedby",
            "更新人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedby",
            "更新人",
        )
    if obj.get("optype") == "repkwkworttemplatefields.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.repkwkworttemplatefields group by updatedat order by x",
            "更新时间",
        )
    # repkwkwortfieldtypes(报表字段类型表)->fieldname(字段名称)

    if obj.get("optype") == "repkwkwortfieldtypes.fieldname_pie":
        res = get_pie(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldname order by x desc",
            "字段名称",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldname_pie_v1":
        res = get_pie_v1(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldname_pie_v2":
        res = get_pie_v2(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldname_line":
        res = get_line(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldname_bar":
        res = get_bar(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldname",
            "字段名称",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldname_bar_v1":
        res = get_bar_v1(
            "select fieldname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldname",
            "字段名称",
        )
    # repkwkwortfieldtypes(报表字段类型表)->fieldtype(字段类型如VARCHAR)

    if obj.get("optype") == "repkwkwortfieldtypes.fieldtype_pie":
        res = get_pie(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldtype order by x desc",
            "字段类型如VARCHAR",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldtype_pie_v1":
        res = get_pie_v1(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldtype",
            "字段类型如VARCHAR",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldtype_pie_v2":
        res = get_pie_v2(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldtype",
            "字段类型如VARCHAR",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldtype_line":
        res = get_line(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldtype",
            "字段类型如VARCHAR",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldtype_bar":
        res = get_bar(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldtype",
            "字段类型如VARCHAR",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.fieldtype_bar_v1":
        res = get_bar_v1(
            "select fieldtype x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by fieldtype",
            "字段类型如VARCHAR",
        )
    # repkwkwortfieldtypes(报表字段类型表)->maxlength(最大长度针对类型)

    if obj.get("optype") == "repkwkwortfieldtypes.maxlength_pie":
        res = get_pie(
            "select maxlength x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by maxlength order by x desc",
            "最大长度针对类型",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.maxlength_pie_v1":
        res = get_pie_v1(
            "select maxlength x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by maxlength",
            "最大长度针对类型",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.maxlength_pie_v2":
        res = get_pie_v2(
            "select maxlength x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by maxlength",
            "最大长度针对类型",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.maxlength_line":
        res = get_line(
            "select maxlength x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by maxlength",
            "最大长度针对类型",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.maxlength_bar":
        res = get_bar(
            "select maxlength x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by maxlength",
            "最大长度针对类型",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.maxlength_bar_v1":
        res = get_bar_v1(
            "select maxlength x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by maxlength",
            "最大长度针对类型",
        )
    # repkwkwortfieldtypes(报表字段类型表)->kwkwisnullable(是否可为空是否)

    if obj.get("optype") == "repkwkwortfieldtypes.kwkwisnullable_pie":
        res = get_pie(
            "select kwkwisnullable x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwisnullable order by x desc",
            "是否可为空是否",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwisnullable_pie_v1":
        res = get_pie_v1(
            "select kwkwisnullable x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwisnullable",
            "是否可为空是否",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwisnullable_pie_v2":
        res = get_pie_v2(
            "select kwkwisnullable x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwisnullable",
            "是否可为空是否",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwisnullable_line":
        res = get_line(
            "select kwkwisnullable x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwisnullable",
            "是否可为空是否",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwisnullable_bar":
        res = get_bar(
            "select kwkwisnullable x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwisnullable",
            "是否可为空是否",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwisnullable_bar_v1":
        res = get_bar_v1(
            "select kwkwisnullable x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwisnullable",
            "是否可为空是否",
        )
    # repkwkwortfieldtypes(报表字段类型表)->kwkwdefaultvalue(默认值)

    if obj.get("optype") == "repkwkwortfieldtypes.kwkwdefaultvalue_pie":
        res = get_pie(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwdefaultvalue order by x desc",
            "默认值",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwdefaultvalue_pie_v1":
        res = get_pie_v1(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwdefaultvalue_pie_v2":
        res = get_pie_v2(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwdefaultvalue_line":
        res = get_line(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwdefaultvalue_bar":
        res = get_bar(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.kwkwdefaultvalue_bar_v1":
        res = get_bar_v1(
            "select kwkwdefaultvalue x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by kwkwdefaultvalue",
            "默认值",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm779_2f88e95faa233d77.repkwkwortfieldtypes;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkwortfieldtypes(报表字段类型表)->createdby(创建人ID)

    if obj.get("optype") == "repkwkwortfieldtypes.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdby order by x desc",
            "创建人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdby",
            "创建人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdby",
            "创建人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdby",
            "创建人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdby",
            "创建人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdby",
            "创建人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by createdat order by x",
            "创建时间",
        )
    # repkwkwortfieldtypes(报表字段类型表)->updatedby(更新人ID)

    if obj.get("optype") == "repkwkwortfieldtypes.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedby order by x desc",
            "更新人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedby",
            "更新人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedby",
            "更新人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedby",
            "更新人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedby",
            "更新人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedby",
            "更新人ID",
        )
    if obj.get("optype") == "repkwkwortfieldtypes.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm779_2f88e95faa233d77.repkwkwortfieldtypes group by updatedat order by x",
            "更新时间",
        )
    # repkwkwortdata(报表数据表)->repkwkwortid(报ID)

    if obj.get("optype") == "repkwkwortdata.repkwkwortid_pie":
        res = get_pie(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortid order by x desc",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortid_pie_v1":
        res = get_pie_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortid_pie_v2":
        res = get_pie_v2(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortid_line":
        res = get_line(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortid_bar":
        res = get_bar(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortid",
            "报ID",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortid_bar_v1":
        res = get_bar_v1(
            "select repkwkwortid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortid",
            "报ID",
        )
    # repkwkwortdata(报表数据表)->repkwkwortname(报名称)

    if obj.get("optype") == "repkwkwortdata.repkwkwortname_pie":
        res = get_pie(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortname order by x desc",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortname_pie_v1":
        res = get_pie_v1(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortname_pie_v2":
        res = get_pie_v2(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortname_line":
        res = get_line(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortname_bar":
        res = get_bar(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortname_bar_v1":
        res = get_bar_v1(
            "select repkwkwortname x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortname",
            "报名称",
        )
    if obj.get("optype") == "repkwkwortdata.repkwkwortdate_line":
        res = get_line(
            "select repkwkwortdate x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by repkwkwortdate order by x",
            "报日期",
        )
    # repkwkwortdata(报表数据表)->creatkwkwor(创建者)

    if obj.get("optype") == "repkwkwortdata.creatkwkwor_pie":
        res = get_pie(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by creatkwkwor order by x desc",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortdata.creatkwkwor_pie_v1":
        res = get_pie_v1(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortdata.creatkwkwor_pie_v2":
        res = get_pie_v2(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortdata.creatkwkwor_line":
        res = get_line(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortdata.creatkwkwor_bar":
        res = get_bar(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "repkwkwortdata.creatkwkwor_bar_v1":
        res = get_bar_v1(
            "select creatkwkwor x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by creatkwkwor",
            "创建者",
        )
    # repkwkwortdata(报表数据表)->department(部门)

    if obj.get("optype") == "repkwkwortdata.department_pie":
        res = get_pie(
            "select department x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by department order by x desc",
            "部门",
        )
    if obj.get("optype") == "repkwkwortdata.department_pie_v1":
        res = get_pie_v1(
            "select department x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by department",
            "部门",
        )
    if obj.get("optype") == "repkwkwortdata.department_pie_v2":
        res = get_pie_v2(
            "select department x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by department",
            "部门",
        )
    if obj.get("optype") == "repkwkwortdata.department_line":
        res = get_line(
            "select department x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by department",
            "部门",
        )
    if obj.get("optype") == "repkwkwortdata.department_bar":
        res = get_bar(
            "select department x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by department",
            "部门",
        )
    if obj.get("optype") == "repkwkwortdata.department_bar_v1":
        res = get_bar_v1(
            "select department x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by department",
            "部门",
        )
    # repkwkwortdata(报表数据表)->status(状态)

    if obj.get("optype") == "repkwkwortdata.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "repkwkwortdata.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortdata.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortdata.status_line":
        res = get_line(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortdata.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortdata.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by status",
            "状态",
        )
    if obj.get("optype") == "repkwkwortdata.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm779_2f88e95faa233d77.repkwkwortdata;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # repkwkwortdata(报表数据表)->attachment(附件路径)

    if obj.get("optype") == "repkwkwortdata.attachment_pie":
        res = get_pie(
            "select attachment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by attachment order by x desc",
            "附件路径",
        )
    if obj.get("optype") == "repkwkwortdata.attachment_pie_v1":
        res = get_pie_v1(
            "select attachment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by attachment",
            "附件路径",
        )
    if obj.get("optype") == "repkwkwortdata.attachment_pie_v2":
        res = get_pie_v2(
            "select attachment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by attachment",
            "附件路径",
        )
    if obj.get("optype") == "repkwkwortdata.attachment_line":
        res = get_line(
            "select attachment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by attachment",
            "附件路径",
        )
    if obj.get("optype") == "repkwkwortdata.attachment_bar":
        res = get_bar(
            "select attachment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by attachment",
            "附件路径",
        )
    if obj.get("optype") == "repkwkwortdata.attachment_bar_v1":
        res = get_bar_v1(
            "select attachment x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by attachment",
            "附件路径",
        )
    if obj.get("optype") == "repkwkwortdata.lkwkwastupdatetime_line":
        res = get_line(
            "select lkwkwastupdatetime x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by lkwkwastupdatetime order by x",
            "最后更新时间",
        )
    # repkwkwortdata(报表数据表)->relateduserid(关联用户ID)

    if obj.get("optype") == "repkwkwortdata.relateduserid_pie":
        res = get_pie(
            "select relateduserid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by relateduserid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "repkwkwortdata.relateduserid_pie_v1":
        res = get_pie_v1(
            "select relateduserid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "repkwkwortdata.relateduserid_pie_v2":
        res = get_pie_v2(
            "select relateduserid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "repkwkwortdata.relateduserid_line":
        res = get_line(
            "select relateduserid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "repkwkwortdata.relateduserid_bar":
        res = get_bar(
            "select relateduserid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "repkwkwortdata.relateduserid_bar_v1":
        res = get_bar_v1(
            "select relateduserid x,count(*) y from vm779_2f88e95faa233d77.repkwkwortdata group by relateduserid",
            "关联用户ID",
        )
    # supermanager(系统管理员)->username(管理员姓名)

    if obj.get("optype") == "supermanager.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm779_2f88e95faa233d77.supermanager group by username order by x desc",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm779_2f88e95faa233d77.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm779_2f88e95faa233d77.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_line":
        res = get_line(
            "select username x,count(*) y from vm779_2f88e95faa233d77.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm779_2f88e95faa233d77.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm779_2f88e95faa233d77.supermanager group by username",
            "管理员姓名",
        )
    assert "title" in res
    return JsonResponse(res)


# __config_visual_views


def bi_level_2(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi_level_2.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    return JsonResponse(res)


def bi_new(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("config_visual/bi_new.html").render())
    obj = mydict(request.POST)
    res = dict()

    # __mark_appcenter_views_all__level_new_bi

    return JsonResponse(res)


def view_users(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpusers.html", locals())


def view_roles(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tproles.html", locals())


def view_userrolerelations(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserrolerelations.html", locals())


def view_weeklyrepkwkworttemplates(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpweeklyrepkwkworttemplates.html", locals()
        )


def view_weeklyrepkwkworts(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpweeklyrepkwkworts.html", locals())


def view_repkwkwortperiods(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprepkwkwortperiods.html", locals())


def view_repkwkwortstatuses(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprepkwkwortstatuses.html", locals())


def view_repkwkworttypes(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprepkwkworttypes.html", locals())


def view_repkwkwortaudits(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprepkwkwortaudits.html", locals())


def view_auditcomments(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpauditcomments.html", locals())


def view_departments(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpdepartments.html", locals())


def view_employees(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpemployees.html", locals())


def view_employeeweeklyrepkwkwortrelations(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tpemployeeweeklyrepkwkwortrelations.html",
            locals(),
        )


def view_notkwkwifications(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpnotkwkwifications.html", locals())


def view_notkwkwificationtypes(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpnotkwkwificationtypes.html", locals()
        )


def view_emaillogs(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpemaillogs.html", locals())


def view_smslogs(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsmslogs.html", locals())


def view_attachments(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpattachments.html", locals())


def view_attachmenttypes(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpattachmenttypes.html", locals())


def view_repkwkwortsubmkwkwissionhkwkwistkwkwories(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tprepkwkwortsubmkwkwissionhkwkwistkwkwories.html",
            locals(),
        )


def view_repkwkwortmodkwkwificationhkwkwistkwkwories(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tprepkwkwortmodkwkwificationhkwkwistkwkwories.html",
            locals(),
        )


def view_repkwkwortcomments(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprepkwkwortcomments.html", locals())


def view_commentreplies(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpcommentreplies.html", locals())


def view_repkwkwortratkwkwings(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprepkwkwortratkwkwings.html", locals()
        )


def view_ratkwkwingcriteria(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpratkwkwingcriteria.html", locals())


def view_permkwkwissions(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tppermkwkwissions.html", locals())


def view_permkwkwissionrolerelations(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tppermkwkwissionrolerelations.html", locals()
        )


def view_systemlogs(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsystemlogs.html", locals())


def view_repkwkwortconfigurations(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprepkwkwortconfigurations.html", locals()
        )


def view_repkwkwortexpkwkwortreckwkwords(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tprepkwkwortexpkwkwortreckwkwords.html",
            locals(),
        )


def view_repkwkworttemplatefields(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprepkwkworttemplatefields.html", locals()
        )


def view_repkwkwortfieldtypes(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprepkwkwortfieldtypes.html", locals()
        )


def view_repkwkwortdata(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprepkwkwortdata.html", locals())


def view_supermanager(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsupermanager.html", locals())
