from django.shortcuts import render
from .models import Projetos, Recados, Cursos
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    projetos = Projetos.objects.all()
    cursos = Cursos.objects.all()
    return render(request, "pagina/index.html", {"projetos": projetos, "cursos": cursos})


def loginv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('restrito'))
        return render(request, 'pagina/login.html', {"erro": "Usuário ou senha inválidos"})
    return render(request, 'pagina/login.html')


def logoutv(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def projetos(request):
    return render(request, 'pagina/projetos.html')


def cursos(request):
    return render(request, 'pagina/cursos.html')


def recados(request):
    recados = Recados.objects.all()
    return render(request, 'pagina/recados.html', {"recados": recados})


def restrito(request):
    return render(request, 'pagina/restrito.html')
