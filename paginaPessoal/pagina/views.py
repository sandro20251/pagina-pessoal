from django.shortcuts import render
from .models import Projetos, Recados, Cursos
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
# Create your views here.


def index(request):

    projetos = Projetos.objects.all()
    cursos = Cursos.objects.all()

    if request.method == "POST":
        nome = request.POST['nomeRecados']
        email = request.POST['emailRecados']
        assunto = request.POST['assuntoRecados']
        mensagem = request.POST['mensagemRecados']
        registro = Recados(nomeRecados=nome, emailRecados=email, assuntoRecados=assunto,
                           mensagemRecados=mensagem, dataRecados=datetime.now())
        registro.save()
        return HttpResponseRedirect(reverse('index'))
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
    if request.method == "POST":
        titulo = request.POST['tituloProjeto']
        descricao = request.POST['descricaoProjeto']
        link = request.POST['linkProjeto']
        tecnologias = request.POST['tecnologiasProjeto']

        registro = Projetos(tituloProjetos=titulo, descricaoProjetos=descricao,
                            linkProjetos=link, tecnologiasProjetos=tecnologias)
        registro.save()

        return HttpResponseRedirect(reverse('index'))

    return render(request, 'pagina/projetos.html')


def cursos(request):
    if request.method == "POST":
        titulo = request.POST["tituloCursos"]
        instituicao = request.POST["instituicaoCursos"]
        ano = request.POST["anoCursos"]
        descricao = request.POST["descricaoCursos"]

        registro = Cursos(tituloCursos=titulo, instituicaoCursos=instituicao,
                          anoCursos=ano, descricaoCursos=descricao)
        registro.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'pagina/cursos.html')


def recados(request):
    recados = Recados.objects.all()
    return render(request, 'pagina/recados.html', {"recados": recados})


def restrito(request):
    return render(request, 'pagina/restrito.html')
