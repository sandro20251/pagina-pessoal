from django.test import TestCase
from .models import Recados, Cursos, Projetos
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
