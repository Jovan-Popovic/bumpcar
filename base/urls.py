from django.urls import path, re_path

from . import views

urlpatterns = [
    # Vehicle requests
    ## Get /vehicle - Get all the vehicles, no authentication required.
    ## Get /vehicle?limit=0 - Get all the vehicles with queries, limit presents maximum amount of returned vehicles, offset=0, no authentication required.
    ## Get /vehicle?limit=0&offset=0 -  Get all the vehicles with queries, limit presents maximum amount of returned vehicles,
        # offset presents amount of skipped vehicles from the start of the request, no authentication required.
    re_path(r'^vehicles/$', views.VehicleListAll.as_view(), name='vehicles'),

    ## Get /vehicle/:id - Get vehicle by ID, no authentication required.
    re_path(r'^vehicle/(?P<pk>.+)/$', views.GetVehicleById.as_view(), name='get-vehicle'),
    re_path(r'^users/$', views.ListUser.as_view(), name="get-users"),

    re_path(r"^profile/create/$", views.CreateUser.as_view(), name="create-user"),
]
