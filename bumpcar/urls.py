from django.urls import path, include, re_path
from django.contrib import admin

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r"^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.jwt")),

    path("", include("base.urls")),
]
