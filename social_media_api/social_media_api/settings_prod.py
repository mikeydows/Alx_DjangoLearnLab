from .settings import *
import os

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")  # set comma-separated hosts

# Security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # ensure when serving via HTTPS

# Database (example using DATABASE_URL)
import dj_database_url
DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}

# Static files (for Heroku)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    