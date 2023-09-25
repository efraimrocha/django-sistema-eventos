from django.db import models

class Participante(models.Model):
    nome_usuario = models.CharField(max_length=255)
    email = models,models.EmailField()

    def __srt__(self):
        return self.nome_usuario