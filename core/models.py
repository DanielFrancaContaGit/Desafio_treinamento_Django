from django.db import models

# Create your models here.

class Canais(models.Model):
    primeiro = models.CharField(max_length=50)
    
    def __str__(self):
        return self.primeiro

class Frases(models.Model):
    frase = models.CharField(max_length=100)

    def __str__(self):
        return self.frase

class Habilidades(models.Model):
    habilidade = models.CharField(max_length=100)

    def __str__(self):
        return self.habilidade