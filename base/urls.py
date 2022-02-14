from django.urls import path, re_path

from . import views

urlpatterns = [
    # User requessts
    re_path(r"^user/create/$", views.CreateUser.as_view(), name="create-user"),
    re_path(r'^users/$', views.ListUser.as_view(), name="get-users"),
    re_path(r'^user/me/$', views.GetUser.as_view(), name="update-user"),

    # Vehicle requests
    re_path(r'^vehicles/$', views.VehicleListAll.as_view(), name='vehicles'),
    re_path(r'^vehicle/(?P<pk>.+)/$', views.GetVehicleById.as_view(), name='get-vehicle'),
]
