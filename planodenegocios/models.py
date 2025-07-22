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
    
class Empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=100)

    def __str__(self):
        return self.nome
    
class Socio(models.Model):
    """
    Cadastro muito simples de sócios.
    Você pode trocar por um relacionamento com o usuário do Django,
    se já existir um módulo de pessoas/usuários no seu sistema.
    """
    nome = models.CharField('Nome do sócio', max_length=100)

    def __str__(self):
        return self.nome


class DistribuicaoLucro(models.Model):
    socio = models.ForeignKey(
        Socio,
        verbose_name='Sócio',
        on_delete=models.CASCADE,
        related_name='distribuicoes'
        
    )
    valor_inicial = models.DecimalField(
        'Valor inicial (mês 1)',
        max_digits=12,
        decimal_places=2,
        default=0
    )
    empresa = models.ForeignKey(
        Empresa,  # ou Projeto
        on_delete=models.CASCADE,
        related_name='distribuicoes_lucro'
    )
    mes_referencia = models.DateField('Mês de Referência')  # ex: 2025-07-01

    class Meta:
        verbose_name = 'Remuneração dos Sócios – Lucros e Dividendos'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.socio} - {self.mes_referencia.strftime('%m/%Y')} - R$ {self.valor_inicial}"

class ValorMensalDistribuicao(models.Model):
    distribuicao = models.ForeignKey(
        'DistribuicaoLucro',  # referencia a remuneração
        on_delete=models.CASCADE,
        related_name='valores_mensais'
    )
    mes = models.PositiveIntegerField()  # 1 a 12
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    constante = models.BooleanField(default=True)  # Se os valores são constantes

    class Meta:
        verbose_name = 'Valor Mensal da Distribuição'
        verbose_name_plural = 'Valores Mensais das Distribuições'

    def __str__(self):
        return f"{self.distribuicao.socio.nome} - Mês {self.mes}: R$ {self.valor}"