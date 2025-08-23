from django.test import TestCase, Client
from .models import Recados, Cursos, Projetos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import request
# Create your tests here.


class Testes(TestCase):
    def setUp(self):
        """Inserindo dados iniciais"""
        Recados.objects.create(nomeRecados="aaa", assuntoRecados="bbb",
                               emailRecados="aaa@gmail.com", mensagemRecados="ccc")
        Recados.objects.create(nomeRecados="ddd", assuntoRecados="eee",
                               emailRecados="ddd@gmail.com", mensagemRecados="fff")
        Recados.objects.create(nomeRecados="ggg", assuntoRecados="hhh",
                               emailRecados="ggg@gmail.com", mensagemRecados="ggg")

        User.objects.create_user(username="a", password="b", email="c@gmail")

    # Testes para verificar a inserção de dados no modelo

    def test_numeroRecados(self):
        """a quantidade de recados salvo deve ser três"""
        a1 = Recados.objects.all()
        self.assertEqual(a1.count(), 3)

    # teste de rotas

    def test_index(self):
        """teste rota index """
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """teste rota login"""
        c = Client()
        response = c.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_recados(self):
        """teste rota recados"""
        c = Client()
        response = c.get("/recados/")
        self.assertEqual(response.status_code, 200)

    # testes de crud de modelos

    # modelo Recados

    def test_alterarRecados(self):
        """alterando conteudod e recados"""
        recado = Recados.objects.get(nomeRecados="aaa")
        recado.assuntoRecados = "modificado"
        recado.save()
        recado2 = Recados.objects.filter(assuntoRecados="modificado")
        self.assertEqual(recado2.count(), 1)

    def test_removerRecados(self):
        """removendo um recado"""
        recado = Recados.objects.get(nomeRecados="aaa")
        recado.delete()
        recados = Recados.objects.all()
        self.assertEqual(recados.count(), 2)

   # modelo Cursos
