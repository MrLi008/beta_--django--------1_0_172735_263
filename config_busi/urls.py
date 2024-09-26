from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_busi_view_index"),
    # 如果用到预测算法,图像识别等单页面展示效果的算法去掉下方注释
    path("auto_detect", views.auto_detect, name="config_busi_view_auto_detect"),
    path("users", views.view_users, name="config_busi_view_users"),
    path("roles", views.view_roles, name="config_busi_view_roles"),
    path(
        "userrolerelations",
        views.view_userrolerelations,
        name="config_busi_view_userrolerelations",
    ),
    path(
        "weeklyrepkwkworttemplates",
        views.view_weeklyrepkwkworttemplates,
        name="config_busi_view_weeklyrepkwkworttemplates",
    ),
    path(
        "weeklyrepkwkworts",
        views.view_weeklyrepkwkworts,
        name="config_busi_view_weeklyrepkwkworts",
    ),
    path(
        "repkwkwortperiods",
        views.view_repkwkwortperiods,
        name="config_busi_view_repkwkwortperiods",
    ),
    path(
        "repkwkwortstatuses",
        views.view_repkwkwortstatuses,
        name="config_busi_view_repkwkwortstatuses",
    ),
    path(
        "repkwkworttypes",
        views.view_repkwkworttypes,
        name="config_busi_view_repkwkworttypes",
    ),
    path(
        "repkwkwortaudits",
        views.view_repkwkwortaudits,
        name="config_busi_view_repkwkwortaudits",
    ),
    path(
        "auditcomments", views.view_auditcomments, name="config_busi_view_auditcomments"
    ),
    path("departments", views.view_departments, name="config_busi_view_departments"),
    path("employees", views.view_employees, name="config_busi_view_employees"),
    path(
        "employeeweeklyrepkwkwortrelations",
        views.view_employeeweeklyrepkwkwortrelations,
        name="config_busi_view_employeeweeklyrepkwkwortrelations",
    ),
    path(
        "notkwkwifications",
        views.view_notkwkwifications,
        name="config_busi_view_notkwkwifications",
    ),
    path(
        "notkwkwificationtypes",
        views.view_notkwkwificationtypes,
        name="config_busi_view_notkwkwificationtypes",
    ),
    path("emaillogs", views.view_emaillogs, name="config_busi_view_emaillogs"),
    path("smslogs", views.view_smslogs, name="config_busi_view_smslogs"),
    path("attachments", views.view_attachments, name="config_busi_view_attachments"),
    path(
        "attachmenttypes",
        views.view_attachmenttypes,
        name="config_busi_view_attachmenttypes",
    ),
    path(
        "repkwkwortsubmkwkwissionhkwkwistkwkwories",
        views.view_repkwkwortsubmkwkwissionhkwkwistkwkwories,
        name="config_busi_view_repkwkwortsubmkwkwissionhkwkwistkwkwories",
    ),
    path(
        "repkwkwortmodkwkwificationhkwkwistkwkwories",
        views.view_repkwkwortmodkwkwificationhkwkwistkwkwories,
        name="config_busi_view_repkwkwortmodkwkwificationhkwkwistkwkwories",
    ),
    path(
        "repkwkwortcomments",
        views.view_repkwkwortcomments,
        name="config_busi_view_repkwkwortcomments",
    ),
    path(
        "commentreplies",
        views.view_commentreplies,
        name="config_busi_view_commentreplies",
    ),
    path(
        "repkwkwortratkwkwings",
        views.view_repkwkwortratkwkwings,
        name="config_busi_view_repkwkwortratkwkwings",
    ),
    path(
        "ratkwkwingcriteria",
        views.view_ratkwkwingcriteria,
        name="config_busi_view_ratkwkwingcriteria",
    ),
    path(
        "permkwkwissions",
        views.view_permkwkwissions,
        name="config_busi_view_permkwkwissions",
    ),
    path(
        "permkwkwissionrolerelations",
        views.view_permkwkwissionrolerelations,
        name="config_busi_view_permkwkwissionrolerelations",
    ),
    path("systemlogs", views.view_systemlogs, name="config_busi_view_systemlogs"),
    path(
        "repkwkwortconfigurations",
        views.view_repkwkwortconfigurations,
        name="config_busi_view_repkwkwortconfigurations",
    ),
    path(
        "repkwkwortexpkwkwortreckwkwords",
        views.view_repkwkwortexpkwkwortreckwkwords,
        name="config_busi_view_repkwkwortexpkwkwortreckwkwords",
    ),
    path(
        "repkwkworttemplatefields",
        views.view_repkwkworttemplatefields,
        name="config_busi_view_repkwkworttemplatefields",
    ),
    path(
        "repkwkwortfieldtypes",
        views.view_repkwkwortfieldtypes,
        name="config_busi_view_repkwkwortfieldtypes",
    ),
    path(
        "repkwkwortdata",
        views.view_repkwkwortdata,
        name="config_busi_view_repkwkwortdata",
    ),
    path("supermanager", views.view_supermanager, name="config_busi_view_supermanager"),
]
