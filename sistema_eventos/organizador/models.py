from django.db import models

class Organizador(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models,models.EmailField()
    cnjp = models.CharField(max_length=14)

    def __srt__(self):
        return self.nome