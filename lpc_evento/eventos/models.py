from django.db import models
from django.contrib.auth.models import User




class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=64, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return '{}, {}, {}'.format(self.logradouro, self.cidade, self.uf)

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    usuario = models.OneToOneField(User)
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=128)
    mae = models.CharField(max_length=128)
    pai = models.CharField(max_length=128)

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=10)
    realizador = models.ForeignKey(PessoaFisica)
    endereco = models.ForeignKey(Endereco, null=True)
    logo = models.CharField(max_length=64)
    data_de_inicio = models.DateTimeField(blank=True, null=True)
    data_de_fim = models.DateTimeField(blank=True, null=True)

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento)
    pessoa = models.ForeignKey(PessoaFisica)
    data_de_inscricao = models.DateTimeField(blank=True, null=True)
    preco = models.FloatField(max_length=10)
