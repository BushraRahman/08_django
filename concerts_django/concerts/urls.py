from django.urls import path

from . import views

app_name = "concerts"

urlpatterns = [
   path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
]
