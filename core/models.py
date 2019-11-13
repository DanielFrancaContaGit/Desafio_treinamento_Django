from django.db import models

# Create your models here.

class Canais(models.Model):
    primeiro = models.CharField(max_length=50)

    class Meta:
        ordering = ['primeiro']
        verbose_name = 'canal'
        verbose_name_plural = 'canais'
    
    def __str__(self):
        return self.primeiro

class Frases(models.Model):
    frase = models.CharField(max_length=100)

    class Meta:
        ordering = ['frase']
        verbose_name = 'frase'
        verbose_name_plural = 'frases'

    def __str__(self):
        return self.frase

class Habilidades(models.Model):
    habilidade = models.CharField(max_length=100)

    class Meta:
        ordering = ['habilidade']
        verbose_name = 'habilidade'
        verbose_name_plural = 'habilidades'
    def __str__(self):
        return self.habilidade