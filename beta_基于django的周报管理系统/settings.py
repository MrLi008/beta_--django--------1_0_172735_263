"""
Django settings for beta_基于django的周报管理系统 project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import traceback
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = "django-insecure-*rt-xg(s%^m$o_2x-+pfu^!v^4-opc4%^7cuwke606-ft3dl)b"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "116.204.69.115",
]

# CSRF_TOKEN

CSRF_TRUSTED_ORIGINS = [
    # For VUE develop
    "http://localhost:8080",
    # For Nginx product
    "http://116.204.69.115:29001",
]


# Application definition


INSTALLED_APPS = [
    "simpleui",
    "sys_user.apps.SysUserConfig",
    "appcenter.apps.AppcenterConfig",
    "config_busi.apps.ConfigBusiConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "captcha",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "beta_基于django的周报管理系统.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
            "builtins": ["django.templatetags.static"],
        },
    },
]

WSGI_APPLICATION = "beta_基于django的周报管理系统.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }


import os

PROJECT_NAME = "beta_基于django的周报管理系统"
DATABASE_NAME = "vm779_2f88e95faa233d77"
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = 3306
DATABASE_USER = "root"
DATABASE_PSW = os.getenv("MYSQL_DATABASE_PSW", "123456")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USER,
        "PASSWORD": DATABASE_PSW,
        "HOST": DATABASE_HOST,
        "PORT": DATABASE_PORT,
    }
}
# 建数据库

try:
    from pymysql.connections import Connection

    conn = Connection(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PSW,
    )
    with conn.cursor() as cursor:
        cursor.execute("show databases;".upper())
        res = cursor.fetchall()
        databases = [database[0] for database in res]
        print("Check The DataBase Has Exist?", DATABASE_NAME in databases)
        if DATABASE_NAME not in databases:
            cursor.execute(
                f"create database {DATABASE_NAME} CHARACTER SET utf8 COLLATE utf8_general_ci;"
            )
            print(
                f"Create Database: {DATABASE_NAME}",
            )
        print("Using DataBase: ", DATABASE_NAME)
except Exception as e:
    pass
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/


LANGUAGE_CODE = "zh-hans"
# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = "/".join([BASE_DIR, STATIC_URL])[:-1]
MEDIA_URL = "media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_ROOT = "/".join([BASE_DIR, MEDIA_URL])[:-1]
FILE_UPLOAD_TEMP_DIR = "tmp/"
UPLOAD_ROOT = "upload/"

# 用于分页

MY_CONFIG_LIMIT = 10

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# config for captcha

CAPTCHA_FONT_SIZE = 28
CAPTCHA_NOISE_FUNCTIONS = [
    "captcha.helpers.noise_null",
]
CAPTCHA_IMAGE_SIZE = (200, 50)

#  For SimpleUI

SIMPLEUI_HOME_INFO = False  # 关闭首页信息展示
SIMPLEUI_ANALYSIS = False  # 关闭页面分析
SIMPLEUI_STATIC_OFFLINE = True  # 开启静态资源离线模式
SIMPLEUI_DEFAULT_THEME = "green"  # 设置默认主题为绿色


# 版本管理
# GLOBAL_VERSION = ''

GLOBAL_VERSION = "_v1"
# GLOBAL_VERSION = '_v2'
# GLOBAL_VERSION = '_v3'
# GLOBAL_VERSION = '_v4'
# GLOBAL_VERSION = '_v5'
