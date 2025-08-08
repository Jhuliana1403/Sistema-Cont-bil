from django.db import models
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

class DespesaAdministrativa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mes = models.IntegerField(choices=[(i, f'{i:02d}') for i in range(1, 13)], default=1)

    def __str__(self):
        return self.nome

class CreditoTributario(models.Model):
    despesa = models.ForeignKey(DespesaAdministrativa, on_delete=models.CASCADE)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # percentual, ex: 12.50

    def __str__(self):
        return f"{self.despesa.nome} - {self.aliquota}%"


class ResumoExecutivo(models.Model):
    texto = models.TextField("Resumo Executivo")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resumo Executivo ({self.atualizado_em:%d/%m/%Y %H:%M})"


class HistoricoMotivacao(models.Model):
    texto = models.TextField("Histórico e Motivação")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Histórico e Motivação ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class ModeloNegocio(models.Model):
    texto = models.TextField("Modelo de Negócio")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Modelo de Negócio ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class CaracteristicasBeneficios(models.Model):
    texto = models.TextField("Características e Benefícios")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Características e Benefícios ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class EstagioDesenvolvimento(models.Model):
    texto = models.TextField("Estágio de Desenvolvimento")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estágio de Desenvolvimento ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class AnaliseSetor(models.Model):
    texto = models.TextField("Análise de Setor")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Análise de Setor ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class MercadoPotencial(models.Model):
    texto = models.TextField("Mercado Potencial")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mercado Potencial ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class AnaliseConcorrencia(models.Model):
    texto = models.TextField("Análise de Concorrência")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Análise de Concorrência ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class Posicionamento(models.Model):
    texto = models.TextField("Posicionamento")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Posicionamento ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class FocoSegmentacao(models.Model):
    texto = models.TextField("Foco e Segmentação")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Foco e Segmentação ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class PlanoPenetracaoMercado(models.Model):
    texto = models.TextField("Plano de Penetração no Mercado")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plano de Penetração ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class DistribuicaoComercializacao(models.Model):
    texto = models.TextField("Distribuição e Comercialização")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Distribuição e Comercialização ({self.atualizado_em:%d/%m/%Y %H:%M})"
    

class ProdutosServicosInsumos(models.Model):
    texto = models.TextField("Produtos, Serviços e Insumos")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Produtos, Serviços e Insumos ({self.atualizado_em:%d/%m/%Y %H:%M})"
    
class DescricaoLegalEstruturaSocietaria(models.Model):
    texto = models.TextField("Descrição Legal e Estrutura Societária")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Descrição Legal ({self.atualizado_em:%d/%m/%Y %H:%M})"

class Equipe(models.Model):
    texto = models.TextField("Equipe")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Equipe ({self.atualizado_em:%d/%m/%Y %H:%M})"

class TerceirizacaoEquipeApoio(models.Model):
    texto = models.TextField("Terceirização e Equipe de Apoio Externo")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Terceirização/Apoio ({self.atualizado_em:%d/%m/%Y %H:%M})"

class AliancasParcerias(models.Model):
    texto = models.TextField("Alianças e Parcerias")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alianças e Parcerias ({self.atualizado_em:%d/%m/%Y %H:%M})"

class PesquisaDesenvolvimentoInovacao(models.Model):
    texto = models.TextField("Pesquisa, Desenvolvimento e Inovação")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pesquisa e Inovação ({self.atualizado_em:%d/%m/%Y %H:%M})"

class GestaoQualidade(models.Model):
    texto = models.TextField("Gestão da Qualidade")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Gestão da Qualidade ({self.atualizado_em:%d/%m/%Y %H:%M})"

class AnaliseRiscos(models.Model):
    texto = models.TextField("Análise de Riscos")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Análise de Riscos ({self.atualizado_em:%d/%m/%Y %H:%M})"

class FatoresCriticosSucesso(models.Model):
    texto = models.TextField("Fatores Críticos de Sucesso")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fatores Críticos de Sucesso ({self.atualizado_em:%d/%m/%Y %H:%M})"

class Cronograma(models.Model):
    texto = models.TextField("Cronograma")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cronograma ({self.atualizado_em:%d/%m/%Y %H:%M})"

class AlternativasEstrategicas(models.Model):
    texto = models.TextField("Alternativas Estratégicas")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alternativas Estratégicas ({self.atualizado_em:%d/%m/%Y %H:%M})"



# TELA RECEITAS
class ReceitaOperacional(models.Model):
    """
    Quantidade projetada de venda no mês 1 para cada Produto/Serviço.
    """
    item = models.ForeignKey(
        'planodenegocios.ProdutoServico',
        on_delete=models.CASCADE,
        related_name='receitas'
    )
    mes_referencia = models.PositiveSmallIntegerField(default=1)  # mês 1 (igual à planilha)
    quantidade_inicial = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        default=0
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item', 'mes_referencia'],
                name='uniq_receita_item_mes'
            )
        ]
        verbose_name = 'Receita operacional'
        verbose_name_plural = 'Receitas operacionais'

    def __str__(self):
        return f'{self.item.nome} (mês {self.mes_referencia})'

    @property
    def unidade(self):
        # vem direto do ProdutoServico
        return self.item.unidade_venda

    @property
    def faturamento_inicial(self):
        # quantidade * preço de venda cadastrado no ProdutoServico
        preco = self.item.preco_venda or 0
        qtd = self.quantidade_inicial or 0
        return qtd * preco


class ReceitaNaoOperacional(models.Model):
    """
    Valor global para 'Outras receitas' do mês 1.
    """
    descricao = models.CharField(max_length=120, default='Outras receitas')
    mes_referencia = models.PositiveSmallIntegerField(default=1)
    valor_inicial = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        default=0
    )

    class Meta:
        verbose_name = 'Receita não operacional'
        verbose_name_plural = 'Receitas não operacionais'

    def __str__(self):
        return f'{self.descricao} (mês {self.mes_referencia})'

#IMPOSTOS
class ImpostoLucro(models.Model):
    """Alíquota média de impostos sobre o lucro para 5 anos."""
    aliquota_ano1 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano2 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano3 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano4 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano5 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])

    def __str__(self):
        return "Impostos sobre o lucro (5 anos)"


class ImpostoVendaItem(models.Model):
    """Alíquotas sobre vendas por produto/serviço para 5 anos."""
    item = models.ForeignKey('planodenegocios.ProdutoServico', on_delete=models.CASCADE, related_name='impostos_venda')
    aliquota_ano1 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano2 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano3 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano4 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])
    aliquota_ano5 = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))])

    class Meta:
        unique_together = ('item',)  # um registro por produto

    def __str__(self):
        return f"Impostos de venda - {self.item.nome}"

