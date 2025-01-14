########################################################################################################################
#                                                                                                                      #
#                                      Django settings to be used during testing                                       #
#                                                                                                                      #
########################################################################################################################

SECRET_KEY = "super-secret-key"  # nosec

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_musicbrainz_connector",
    "mneia_backend",
    "mneia_exporter",
]

DATABASES = {
    # SQLite option. SQLite is adequate for most functionality. Does not support `distinct` though:
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "TEST": {
            "NAME": "test-db",
        },
    }
    # Postgres option. Commented out here until it may be needed, e.g. in case `distinct` is used in SQL queries.
    # "default": {
    #     "NAME": "mneia_test",
    #     "ENGINE": "django.db.backends.postgresql",
    #     "USER": "mneia_test",
    #     "PASSWORD": "mneia_test",
    # },
}

ROOT_URLCONF = "mneia_exporter.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

USE_TZ = True
