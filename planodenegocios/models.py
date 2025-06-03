from django.db import models

class Investimento(models.Model):
    data = models.DateField(null=True, blank=True)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    depreciacao = models.DecimalField(max_digits=5, decimal_places=2)
    credito = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.descricao
    
class Investimento_ampliacoes(models.Model):
    data = models.DateField(null=True, blank=True)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    depreciacao = models.DecimalField(max_digits=5, decimal_places=2)
    credito = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.descricao