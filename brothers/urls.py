from django.urls import path
from .views import list_actives, list_inactives

urlpatterns = [
    path("active_house/", list_actives, name="list_actives"),
    path("alumni_house/", list_inactives, name="list_inactives"),
]
