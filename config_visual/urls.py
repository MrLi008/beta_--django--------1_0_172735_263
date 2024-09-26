from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_visual_view_index"),
    path("bi", views.bi, name="config_visual_view_bi"),
    path("bi_level_2", views.bi_level_2, name="config_visual_view_bi_level_2"),
    path("bi_new", views.bi_new, name="config_visual_view_bi_new"),
    path("bi_v1", views.bi, name="config_visual_view_bi_v1"),
    path("bi_v2", views.bi, name="config_visual_view_bi_v2"),
    path("bi_v3", views.bi, name="config_visual_view_bi_v3"),
    path("bi_v4", views.bi, name="config_visual_view_bi_v4"),
    path("bi_v5", views.bi, name="config_visual_view_bi_v5"),
    #
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpusers",
        views.view_users,
        name="bi_tpusers",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tproles",
        views.view_roles,
        name="bi_tproles",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserrolerelations",
        views.view_userrolerelations,
        name="bi_tpuserrolerelations",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpweeklyrepkwkworttemplates",
        views.view_weeklyrepkwkworttemplates,
        name="bi_tpweeklyrepkwkworttemplates",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpweeklyrepkwkworts",
        views.view_weeklyrepkwkworts,
        name="bi_tpweeklyrepkwkworts",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortperiods",
        views.view_repkwkwortperiods,
        name="bi_tprepkwkwortperiods",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortstatuses",
        views.view_repkwkwortstatuses,
        name="bi_tprepkwkwortstatuses",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkworttypes",
        views.view_repkwkworttypes,
        name="bi_tprepkwkworttypes",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortaudits",
        views.view_repkwkwortaudits,
        name="bi_tprepkwkwortaudits",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpauditcomments",
        views.view_auditcomments,
        name="bi_tpauditcomments",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpdepartments",
        views.view_departments,
        name="bi_tpdepartments",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpemployees",
        views.view_employees,
        name="bi_tpemployees",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpemployeeweeklyrepkwkwortrelations",
        views.view_employeeweeklyrepkwkwortrelations,
        name="bi_tpemployeeweeklyrepkwkwortrelations",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpnotkwkwifications",
        views.view_notkwkwifications,
        name="bi_tpnotkwkwifications",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpnotkwkwificationtypes",
        views.view_notkwkwificationtypes,
        name="bi_tpnotkwkwificationtypes",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpemaillogs",
        views.view_emaillogs,
        name="bi_tpemaillogs",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsmslogs",
        views.view_smslogs,
        name="bi_tpsmslogs",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpattachments",
        views.view_attachments,
        name="bi_tpattachments",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpattachmenttypes",
        views.view_attachmenttypes,
        name="bi_tpattachmenttypes",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortsubmkwkwissionhkwkwistkwkwories",
        views.view_repkwkwortsubmkwkwissionhkwkwistkwkwories,
        name="bi_tprepkwkwortsubmkwkwissionhkwkwistkwkwories",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortmodkwkwificationhkwkwistkwkwories",
        views.view_repkwkwortmodkwkwificationhkwkwistkwkwories,
        name="bi_tprepkwkwortmodkwkwificationhkwkwistkwkwories",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortcomments",
        views.view_repkwkwortcomments,
        name="bi_tprepkwkwortcomments",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpcommentreplies",
        views.view_commentreplies,
        name="bi_tpcommentreplies",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortratkwkwings",
        views.view_repkwkwortratkwkwings,
        name="bi_tprepkwkwortratkwkwings",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpratkwkwingcriteria",
        views.view_ratkwkwingcriteria,
        name="bi_tpratkwkwingcriteria",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tppermkwkwissions",
        views.view_permkwkwissions,
        name="bi_tppermkwkwissions",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tppermkwkwissionrolerelations",
        views.view_permkwkwissionrolerelations,
        name="bi_tppermkwkwissionrolerelations",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsystemlogs",
        views.view_systemlogs,
        name="bi_tpsystemlogs",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortconfigurations",
        views.view_repkwkwortconfigurations,
        name="bi_tprepkwkwortconfigurations",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortexpkwkwortreckwkwords",
        views.view_repkwkwortexpkwkwortreckwkwords,
        name="bi_tprepkwkwortexpkwkwortreckwkwords",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkworttemplatefields",
        views.view_repkwkworttemplatefields,
        name="bi_tprepkwkworttemplatefields",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortfieldtypes",
        views.view_repkwkwortfieldtypes,
        name="bi_tprepkwkwortfieldtypes",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprepkwkwortdata",
        views.view_repkwkwortdata,
        name="bi_tprepkwkwortdata",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsupermanager",
        views.view_supermanager,
        name="bi_tpsupermanager",
    ),
]
