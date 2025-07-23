"""
Django settings for dymanic project – ajustadas para producción y desarrollo.

Requiere un archivo .env en la raíz con, por ejemplo:
DEBUG=True
SECRET_KEY=tu_clave_secreta
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=dymanic
DB_USER=dymanic
DB_PASSWORD=supersecret
DB_HOST=localhost
DB_PORT=5432
"""

from pathlib import Path
import os
import environ

# ───────────────────────────────────────────
# Rutas base
# ───────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ───────────────────────────────────────────
# Variables de entorno
# ───────────────────────────────────────────
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env("DEBUG")
# Si no existe SECRET_KEY en entorno, usar este fallback (útil en CI/local)
SECRET_KEY = env("SECRET_KEY", default="django-insecure-fallback-key")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="").split(",")

# ───────────────────────────────────────────
# Apps
# ───────────────────────────────────────────
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Terceros
    "django_htmx",
    # Propias
    "inventario",
    "ventas",
    "reportes",
]

# ───────────────────────────────────────────
# Middleware
# ───────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",      # para servir estáticos
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dymanic.urls"

# ───────────────────────────────────────────
# Templates
# ───────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "dymanic.wsgi.application"

# ───────────────────────────────────────────
# Base de datos – PostgreSQL
# ───────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="dymanic"),
        "USER": env("DB_USER", default="dymanic"),
        "PASSWORD": env("DB_PASSWORD", default=""),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
    }
}

# ───────────────────────────────────────────
# Password validation
# ───────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ───────────────────────────────────────────
# Internacionalización
# ───────────────────────────────────────────
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# ───────────────────────────────────────────
# Archivos estáticos
# ───────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ───────────────────────────────────────────
# Seguridad adicional
# ───────────────────────────────────────────
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
CSP_DEFAULT_SRC = ("'self'",)

# ───────────────────────────────────────────
# Redirecciones de login/logout
# ───────────────────────────────────────────
LOGIN_REDIRECT_URL = "/inventario/productos/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# ───────────────────────────────────────────
# Clave primaria por defecto
# ───────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
