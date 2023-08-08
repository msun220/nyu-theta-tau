from django.urls import path
from .views import list_actives, list_inactives, list_eboard

urlpatterns = [
    path("active_house/", list_actives, name="list_actives"),
    path("alumni_house/", list_inactives, name="list_inactives"),
    path("eboard/", list_eboard, name="list_eboard")
]
