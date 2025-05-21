# models.py atualizado com campo quantidade

from django.db import models

class Produtos(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False, verbose_name="Descrição")
    categoria = models.CharField(max_length=50, null=False, blank=False, verbose_name="Categoria")
    quantidade = models.PositiveIntegerField(default=0, verbose_name="Quantidade")

    def __str__(self):
        return f"{self.descricao} ({self.categoria})"
    
    

