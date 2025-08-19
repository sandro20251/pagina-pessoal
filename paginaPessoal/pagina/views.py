from django.shortcuts import render
from .models import Projetos, Recados, Cursos

# Create your views here.


def index(request):
    projetos = Projetos.objects.all()
    cursos = Cursos.objects.all()
    return render(request, "pagina/index.html", {"projetos": projetos, "cursos": cursos})


def login(request):
    return render(request, 'pagina/login.html')


def logout(request):
    pass


def projetos(request):
    return render(request, 'pagina/projetos.html')


def cursos(request):
    return render(request, 'pagina/cursos.html')


def recados(request):
    recados = Recados.objects.all()
    return render(request, 'pagina/recados.html', {"recados": recados})
