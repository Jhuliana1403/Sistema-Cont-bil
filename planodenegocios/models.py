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

# Plano financeiro - equipe própria
class Funcionario(models.Model):
    cargo = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    salario_inicial = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def valor_inicial(self):
        return self.quantidade * self.salario_inicial

    def __str__(self):
        return self.cargo

class SalarioMensal(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    mes = models.PositiveSmallIntegerField()  # 1 a 36 (3 anos)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Encargo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    percentual = models.DecimalField(max_digits=5, decimal_places=2)  # ex: 30.00

    def calcular_valor_mes(self, mes):
        salario = SalarioMensal.objects.get(funcionario=self.funcionario, mes=mes).valor
        return salario * (self.percentual / 100)

class Beneficio(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[('alimentacao', 'Alimentação'), ('transporte', 'Transporte')])
    mes = models.PositiveSmallIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class EncargoGlobal(models.Model):  # era EncargosOutrosCustos
    percentual = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

class DespesaMensal(models.Model):  # era CustoMensal
    mes = models.PositiveSmallIntegerField()  # 1 a 60
    tipo = models.CharField(max_length=20, choices=[('alimentacao', 'Alimentação'), ('transporte', 'Transporte')])
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

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
