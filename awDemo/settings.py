"""
Django settings for awDemo project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(ftj3x762j2vxy)c_)pld#p10!0vo-#i(bu=ya8=wb!vmd_04#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'awDemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'awDemo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

###############
# THIRD PARTY #
###############

THIRD_PART_CONFIG = {
    # 阿里云服务配置(目前业务方向为短信业务、视频点播业务等)
    "ALI_YUN": {
        "ACCESS_KEY": "",
        "SECRET": ""
    },
    # 滑动验证码服务配置
    "GEE_TEST": {
        "ACCESS_KEY": "37ca5631edd1e882721808d35163b3ad",
        "SECRET": "7eb11ccf3e0953bdd060ed8b60b0c4f5",
        # 业务配置
        # 是否启用滑动验证码验证组件(True表示启用)
        "VERIFY_STATUS": True,
        # 无需校验的账户白名单, 配置UID即可
        "NOT_VERIFY_LIST": [
            "2ba6b08d53a4fd27057a32537e2d55ae",  # szww
        ]
    },
    # 支付宝支付相关配置
    "ALI_PAY": {
        # 默认使用配置
        "default": {
            # 支付宝支付调用的接口版本(固定值1.0)
            "version": "1.0",
            # 是否启用调试模式(False是正式环境)
            "debug": True,
            # 支付宝分配给开发者的应用ID(启用线上环境请更改),
            "app_id": "2016081500252288",
            # APP应用的私钥
            "app_private_key_path": os.path.join(BASE_DIR, "data", "ali", "app_private_test_2048"),
            # 支付宝的公钥
            "alipay_public_key_path": os.path.join(BASE_DIR, "data", "ali", "alipay_public_test_2048"),
            # 添加回调域名(异步通知: 支付宝会通知该笔订单交易成功)
            "callback_url": "",
        },
        # 目前针对支付业务进行切换
        "pay": {
            # 支付宝支付调用的接口版本(固定值1.0)
            "version": "1.0",
            # 是否启用调试模式(False是正式环境)
            "debug": True,
            "app_id": "2016081500252288",  # 支付宝分配给开发者的应用ID(启用线上环境请更改),
            # APP应用的私钥
            "app_private_key_path": os.path.join(BASE_DIR, "data", "ali", "app_private_test_2048"),
            # 支付宝的公钥
            "alipay_public_key_path": os.path.join(BASE_DIR, "data", "ali", "alipay_public_test_2048"),
            # 添加回调域名(异步通知: 支付宝会通知该笔订单交易成功)
            "callback_url": "",
        }
    },
    "WX": {
        "app_id": "wxa22d581a68c18b00",
        "secret": "3d392f345458c9924095afe386915dd8",
        "grant_type": "authorization_code",
        "redirect_uri": "http://127.0.0.1:8000/api/v1/servicenum/",  # 网页授权回调API
        "notify_url": "http://test.luffycity.com:33334/api/v1/trade/wx/",
        "token": "bingdujianer",  # 事件推送验证token
        "mch_id": "",
        "api_key_path": os.path.join(BASE_DIR, "data", "wx", "pay_key"),
        "debug": False
    }
}
