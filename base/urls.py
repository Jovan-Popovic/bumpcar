from django.urls import path, re_path

from . import views

urlpatterns = [
    # User requessts
    re_path(r"^user/create/$", views.CreateUser.as_view(), name="create-user"),
    re_path(r'^users/$', views.ListUser.as_view(), name="get-all-users"),

    # Vehicle requests
    re_path(r'^vehicles/$', views.VehicleListAll.as_view(), name='get-all-vehicles'),
    re_path(r'^vehicle/id=(?P<pk>.+)/$', views.GetVehicleById.as_view(), name='get-vehicle-by-id'),
    re_path(r'^vehicle/$', views.CreateVehicle.as_view(), name='create-vehicle')
]
