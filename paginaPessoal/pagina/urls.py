from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("projetos/", views.projetos, name="projetos"),
    path("cursos/", views.cursos, name="cursos"),
    path("recados/", views.recados, name="recados")
]
