from django.db import models

# Create your models here.


class Projetos(models.Model):

    tituloProjetos = models.CharField(max_length=64)
    descricaoProjetos = models.CharField(max_length=1000)
    linkProjetos = models.URLField()
    tecnologiasProjetos = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.tituloProjetos}-{self.linkProjetos}"


class Cursos(models.Model):
    tituloCursos = models.CharField(max_length=64)
    instituicaoCursos = models.CharField(max_length=64)
    anoCursos = models.IntegerField()
    descricaoCursos = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.tituloCursos}- {self.anoCursos}"


class Recados(models.Model):
    nomeRecados = models.CharField(max_length=64)
    assuntoRecados = models.CharField(max_length=64)
    emailRecados = models.EmailField()
    mensagemRecados = models.CharField(max_length=1000)
    dataRecados = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomeRecados}- {self.assuntoRecados}"
