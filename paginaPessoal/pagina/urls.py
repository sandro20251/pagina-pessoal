from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.loginv, name="login"),
    path("logout/", views.logoutv, name="logout"),

    path("recados/", views.recados, name="recados"),
    path("restrito/", views.restrito, name="restrito"),
]
