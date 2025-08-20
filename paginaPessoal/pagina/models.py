from django.db import models

# Create your models here.

class Recados(models.Model):
    nomeRecados = models.CharField(max_length=64)
    assuntoRecados = models.CharField(max_length=64)
    emailRecados = models.EmailField()
    mensagemRecados = models.CharField(max_length=1000)
    dataRecados = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomeRecados}- {self.assuntoRecados}"
