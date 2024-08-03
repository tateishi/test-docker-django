ALLOWED_HOSTS = ["*"]
LANGUAGE_CODE = "ja-jp"
TIME_ZONE = "Asia/Tokyo"
STATIC_ROOT = BASE_DIR / "static"

n = MIDDLEWARE.index("django.middleware.security.SecurityMiddleware")
MIDDLEWARE.insert(n+1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
