from django.shortcuts import render
from .models import Recados
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
# Create your views here.


def index(request):

    erro = None

    if request.method == "POST":
        nome = request.POST['nomeRecados']
        email = request.POST['emailRecados']
        assunto = request.POST['assuntoRecados']
        mensagem = request.POST['mensagemRecados']

        if not nome or not email or not assunto or not mensagem:
            erro = "preencha os campos necessários"

        registro = Recados(nomeRecados=nome, emailRecados=email, assuntoRecados=assunto,
                           mensagemRecados=mensagem, dataRecados=datetime.now())
        registro.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request, "pagina/index.html", {"erro": erro})


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


def recados(request):
    recados = Recados.objects.all()
    return render(request, 'pagina/recados.html', {"recados": recados})


def restrito(request):
    return render(request, 'pagina/restrito.html')
