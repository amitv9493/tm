from .base_settings import *
DEBUG=False
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "EXCEPTION_HANDLER": "project.handlers.custom_exception_handler",
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# CORS_ALLOWED_ORIGINS = ['http://tubemastercrm.com/']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
X_FRAME_OPTIONS = "SAMEORIGIN"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1 * 24 * 60 * 5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

PASSWORD_RESET_TIMEOUT = 900

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = "/home/arttecrt/public_html/Tube_master/static"
STATIC_URL = "/staticgit/"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "media/"
MEDIA_ROOT = "media"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}