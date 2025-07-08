from django.db import models

#Aba de investimento
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
    
class Ampliacoes(models.Model):
    data = models.DateField(null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    depreciacao = models.DecimalField(max_digits=5, decimal_places=2)
    credito = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.descricao

# Aba de Produto e Serviço
class ProdutoServico(models.Model):
    TIPO_CHOICES = [
        ('servico', 'Serviço'),
        ('terceiros', 'Produto de terceiros'),
        ('fabricacao', 'Fabricação própria'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)
    unidade_venda = models.CharField(max_length=20)
    margem_lucro = models.DecimalField(max_digits=5, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_varia = models.BooleanField(default=False, null= True)

    def custo_total(self):
        return sum([c.custo_unitario for c in self.custos.all()])

    def preco_sugerido(self):
        total = self.custo_total()
        return total * (1 + self.margem_lucro / 100)

    def __str__(self):
        return self.nome

class CustoProducao(models.Model):
    produto = models.CharField(max_length=255)
    frete = models.DecimalField(max_digits=10, decimal_places=2)
    embalagem = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome}"