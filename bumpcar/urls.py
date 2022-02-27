from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r"^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("", include("base.urls")),
    re_path(r"^(?P<path>.*)/$", serve, {"document_root": settings.MEDIA_ROOT}),
]
