from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.loginv, name="login"),
    path("logout/", views.logoutv, name="logout"),
    path("projetos/", views.projetos, name="projetos"),
    path("cursos/", views.cursos, name="cursos"),
    path("recados/", views.recados, name="recados"),
    path("restrito/", views.restrito, name="restrito"),
]
