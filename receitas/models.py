from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Create your models here.
class Receita(models.Model):

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE) # criação do relacionamento receita/pessoa
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now(), blank=True)
    publicado = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)