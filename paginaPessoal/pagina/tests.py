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

        Cursos.objects.create(
            tituloCursos="iii", instituicaoCursos="jjj", anoCursos=2025, descricaoCursos="kkk")
        Cursos.objects.create(
            tituloCursos="lll", instituicaoCursos="mmm", anoCursos=2000, descricaoCursos="nnn")
        Cursos.objects.create(
            tituloCursos="ooo", instituicaoCursos="ppp", anoCursos=2025, descricaoCursos="qqq")

        Projetos.objects.create(tituloProjetos="rrr", descricaoProjetos="sss",
                                linkProjetos="#", tecnologiasProjetos="ttt, uuu")
        Projetos.objects.create(tituloProjetos="vvv", descricaoProjetos="xxx",
                                linkProjetos="#", tecnologiasProjetos="yyy, zzz")
        Projetos.objects.create(tituloProjetos="zzz", descricaoProjetos="1aaa",
                                linkProjetos="#", tecnologiasProjetos="1bbb, 1ccc")

        User.objects.create_user(username="a", password="b", email="c@gmail")

    # Testes para verificar a inserção de dados no modelo

    def test_numeroRecados(self):
        """a quantidade de recados salvo deve ser três"""
        a1 = Recados.objects.all()
        self.assertEqual(a1.count(), 3)

    def test_numeroCursos(self):
        """a qunatidade de cursos deve ser três"""
        a2 = Cursos.objects.all()
        self.assertEqual(a2.count(), 3)

    def test_numeroProjetos(self):
        """a quantidade de projetos salvos deve ser três"""
        a3 = Projetos.objects.all()
        self.assertEqual(a3.count(), 3)

    # teste de rotas

    def test_index(self):
        """teste rota index """
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cursos(self):
        """teste rota cursos"""
        c = Client()
        response = c.get("/cursos/")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """teste rota login"""
        c = Client()
        response = c.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_projetos(self):
        """teste de rota de projetos"""
        c = Client()
        response = c.get("/projetos/")
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

    def test_alterarCursos(self):
        """alterando um curso"""
        curso = Cursos.objects.get(tituloCursos="iii")
        curso.descricaoCursos = "modificado"
        curso.save()
        curso2 = Cursos.objects.filter(descricaoCursos="modificado")
        self.assertEqual(curso2.count(), 1)

    def test_excluirCursos(self):
        """Excluindo um curso"""
        curso = Cursos.objects.get(tituloCursos="iii")
        curso.delete()
        cursos = Cursos.objects.all()
        self.assertEqual(cursos.count(), 2)

    # modelo Projetos

    def test_tituloProjetos(self):
        """alterando um projeto"""
        projeto = Projetos.objects.get(tituloProjetos="rrr")
        projeto.descricaoProjetos = "modificado"
        projeto.save()
        projeto2 = Projetos.objects.filter(descricaoProjetos="modificado")
        self.assertEqual(projeto2.count(), 1)

    def test_excluindoProjeto(self):
        """Excluindo um porjeto"""
        projeto = Projetos.objects.get(tituloProjetos="rrr")
        projeto.delete()
        projetos = Projetos.objects.all()
        self.assertEqual(projetos.count(), 2)
