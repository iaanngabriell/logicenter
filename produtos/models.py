from django.db import models

# Create your models here.
class Produtos(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=50, unique=True, null=False, blank=False),
    quantidade = models.PositiveIntegerField(default=0),
    
    # Isso ajuda a mostrar o nome certinho quando a gente olhar na lista de brinquedos
    def __str__(self):
        return f"{self.descricao} ({self.categoria})"
