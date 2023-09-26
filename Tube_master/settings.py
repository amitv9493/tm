import logging
from datetime import timedelta
import os
from pathlib import Path
import os
from django.contrib.messages import constants as messages
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


IMPORT_EXPORT_USE_TRANSACTIONS = False
DEBUG=os.environ.get("debug")
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "corsheaders",
    "dal",
    "dal_select2",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tube",
    "client",
    "project",
    "phonenumber_field",
    "equipment",
    "part",
    "sorl.thumbnail",
    "ajax_datatable",
    "smart_selects",
    "admin_reorder",
    "django_select2",
    "import_export",
    # 'notifications',
    "comment",
    "schedule",
    "bootstrap_datepicker_plus",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_countries",
    "django_filters",
    "django_extensions",
    "modelhistory.apps.ModelhistoryConfig",
    # "import_export",
]

"""
===============================================================================
        
                    REST_FRAMEWORK + SIMPLE JWT + CORS SETTINGS

===============================================================================

"""
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "EXCEPTION_HANDLER": "project.handlers.custom_exception_handler",
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    
    
    
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


"""
------------------------ END --------------------------------------------
"""

"""=======================================================================

                                JAZZMINE SETTINGS

==========================================================================

"""

JAZZMIN_SETTINGS = {
    "site_title": "Tube Master",
    "site_header": "Tube Master",
    "site_brand": "TM",
    "site_logo_classes": "img-thumbnail",
    "site_icon": "/img/tm_logo.png",
    # Add your own branding here
    "site_logo": "/img/tm_logo.png",
    "welcome_sign": "Welcome to the TubeMaster",
    # Copyright on the footer
    "copyright": "Anant Soft Computing",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    # "topmenu_links": [
    #     # Url that gets reversed (Permissions can be added)
    #     {"name": "TubeMaster", "url": "home", "permissions": ["auth.view_user"], "url": "home", "permissions": ["auth.view_user"]},
    #     # model admin to link to (Permissions checked against model)
    #     {"model": "auth.User"},    {"model": "auth.Warehouse"},
    # ],
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # model admin to link to (Permissions checked against model)
        {"model": "tube.Warehouse"},
        # model admin to link to (Permissions checked against model)
        {"model": "client.Client"},
        # model admin to link to (Permissions checked against model)
        {"model": "project.Project"},
        # # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "tube"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": True,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    "custom_css": True,
    "custom_js": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "related_modal_active": True,
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "slate",
    "dark_mode_theme": "slate",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
}


ADMIN_REORDER = (
    # Keep original label and models
    "sites",
    # # Rename app
    # {'app': 'auth', 'label': 'Authorisation'},
    # Reorder app models
    {"app": "auth", "models": ("auth.User", "auth.Group")},
    # # Exclude models
    # {'app': 'auth', 'models': ('auth.User', )},
    # Cross-linked models
    # {'app': 'tube', 'models': ('tube.Warehouse', 'tube.Catalyst')},
    {
        "app": "client",
        "models": ("client.Client", "client.Plant", "client.Unit", "client.Reactor"),
    },
    {
        "app": "equipment",
        "models": (
            "equipment.TTD",
            "equipment.BDD",
            "equipment.CALIBRATION_STAND",
            "equipment.SwabMaster",
        ),
    },
    {"app": "part", "models": ("part.Part",)},
    {
        "app": "tube",
        "models": (
            "tube.Warehouse",
            "tube.Catalyst",
            "tube.Loading",
        ),
    },
    # # models with custom name
    # {'app': 'auth', 'models': (
    #     'auth.Group',
    #     {'model': 'auth.User', 'label': 'Staff'},
    # )},
)

"""
============================================================================================

"""

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "admin_reorder.middleware.ModelAdminReorder",
    "tm_api.middleware.LogNon200ResponseMiddleware",
]

# GOOGLE_APIz_KEY = 'AIzaSyD--your-google-maps-key-SjQBE'
DRF_API_LOGGER_DATABASE = True  # Default to False
DRF_API_LOGGER_SLOW_API_ABOVE = 200

ROOT_URLCONF = "Tube_master.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "front"), os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "Tube_master.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = "/home/arttecrt/public_html/static"
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static", os.path.join(BASE_DIR, "front", "static")]
MEDIA_URL = "media/"
MEDIA_ROOT = "/home/arttecrt/public_html/media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


"""EMAIL_BACKEND SETTINGS"""

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER = "youremail@gmail.com"
EMAIL_HOST = "smtp.gmail.com"  # smtp server
EMAIL_HOST_PASSWORD = "moxfbfewejtlrhoe"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

APPEND_SLASH = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME':  os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
            'class': 'logging.FileHandler',
            'filename': 'logfile.log',  # Specify the path to your log file.
            'formatter': 'verbose',  # Use the 'verbose' formatter defined above.
        },
    },
    'root': {
        'handlers': ['file'],  # Use the 'file' handler for the root logger.
        'level': 'ERROR',  # Set the desired log level for the root logger.
    },
}
