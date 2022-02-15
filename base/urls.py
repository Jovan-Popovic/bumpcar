from django.urls import path, re_path

from .views import UserView, VehicleView, ConditionView

urlpatterns = [
    # User requessts
    re_path(r"^user/create/$", UserView.CreateUser.as_view(), name="create-user"),
    re_path(r'^users/$', UserView.ListUser.as_view(), name="get-all-users"),

    # Vehicle requests
    re_path(r'^vehicles/$', VehicleView.VehicleListAll.as_view(), name='get-all-vehicles'),
    re_path(r'^vehicle/id=(?P<pk>.+)/$', VehicleView.GetVehicleById.as_view(), name='get-vehicle-by-id'),
    re_path(r'^vehicle/$', VehicleView.CreateVehicle.as_view(), name='create-vehicle'),

    re_path(r'^conditions/$', ConditionView.GetAllCondition.as_view(), name='get-conditions'),
    re_path(r'^condition/$', ConditionView.CreateCondition.as_view(), name='create-condition'),
]
