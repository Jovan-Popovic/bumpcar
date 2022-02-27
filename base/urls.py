from django.urls import path, re_path

from .views import *

urlpatterns = [
    # User requessts
    re_path(r"^user/create/$", UserView.CreateUser.as_view(), name="create-user"),
    re_path(r'^users/$', UserView.ListUser.as_view(), name="get-all-users"),
    re_path(r'^user/(?P<pk>[0-9]+)/$', UserView.GetUser.as_view(), name='get-user-by-id'),
    re_path(r"^user/update/(?P<pk>[0-9]+)/$", UserView.UpdateUser.as_view(), name="update-user"),
    re_path(r"^user/delete/(?P<pk>[0-9]+)/$", UserView.DeleteUser.as_view(), name="delete-user"),

    # Vehicle requests
    re_path(r'^vehicles/$', VehicleView.VehicleListAll.as_view(), name='get-all-vehicles'),
    re_path(r'^vehicle/(?P<pk>[0-9]+)/$', VehicleView.GetVehicleById.as_view(), name='get-vehicle-by-id'),
    re_path(r'^vehicle/user/(?P<pk>[0-9]+)/$', VehicleView.GetVehicleByUser.as_view(), name='get-vehicle-by-id'),
    re_path(r'^vehicle/(?P<vehicle>[0-9]+)/images/$', GetImageById.as_view(), name='get-vehicle-image-by-vehicle-id'),
    re_path(r'^vehicle/$', VehicleView.CreateVehicle.as_view(), name='create-vehicle'),
    re_path(r'^vehicle/delete/(?P<pk>[0-9]+)/$', VehicleView.DeleteVehicle.as_view(), name='delete-vehicle'),

    # Fields Post Request
    re_path(r'^condition/$',     CreateField.as_view(),       name='create-conditions',    kwargs={ 'model': Condition }),
    re_path(r'^fuel-type/$',     CreateField.as_view(),       name='create-fuel-types',    kwargs={ 'model': FuelType }),
    re_path(r'^gear-type/$',     CreateField.as_view(),       name='create-gear-typles',   kwargs={ 'model': GearType }),
    re_path(r'^color/$',         CreateField.as_view(),       name='create-colors',        kwargs={ 'model': Color }),
    re_path(r'^vehicle-type/$',  CreateField.as_view(),       name='create-vehile-types',  kwargs={ 'model': VehicleType }),
    re_path(r'^drivetrain/$',    CreateField.as_view(),       name='create-drivetrains',   kwargs={ 'model': Drivetrain }),
    re_path(r'^brand/$',         CreateField.as_view(),       name='create-brands',        kwargs={ 'model': Brand }),

    # Fields Get Request
    re_path(r'^conditions/$',    ListFieldValues.as_view(),   name='get-conditions',       kwargs={ 'model': Condition }),
    re_path(r'^fuel-types/$',    ListFieldValues.as_view(),   name='get-fuel-types',       kwargs={ 'model': FuelType }),
    re_path(r'^gear-types/$',    ListFieldValues.as_view(),   name='get-gear-typles',      kwargs={ 'model': GearType }),
    re_path(r'^colors/$',        ListFieldValues.as_view(),   name='get-colors',           kwargs={ 'model': Color }),
    re_path(r'^vehicle-types/$', ListFieldValues.as_view(),   name='get-vehile-types',     kwargs={ 'model': VehicleType }),
    re_path(r'^drivetrains/$',   ListFieldValues.as_view(),   name='get-drivetrains',      kwargs={ 'model': Drivetrain }),
    re_path(r'^brands/$',        ListFieldValues.as_view(),   name='get-brands',           kwargs={ 'model': Brand }),
]
