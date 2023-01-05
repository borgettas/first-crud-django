from django.db import models

#desceve como o dado é salvo no db 
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome