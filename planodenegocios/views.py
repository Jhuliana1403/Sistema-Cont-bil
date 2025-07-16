# Importa as funções necessárias do Django para renderizar templates e redirecionar requisições
from django.shortcuts import render, redirect, get_object_or_404

from decimal import Decimal
# Importa o modelo Investimento do arquivo models.py
from .models import Investimento, Ampliacoes, ProdutoServico, CustoProducao, Funcionario, EncargoGlobal, DespesaMensal

from django.contrib import messages

# View principal que renderiza a página inicial do plano de negócios
def index(request):
    return render(request, 'planodenegocios/index.html')

# View que renderiza a página de análise de setor
def analise_setor(request):
    return render(request, 'planodenegocios/analise_setor.html')

# View que renderiza a página de mercado potencial
def mercado_potencial(request):
    return render(request, 'planodenegocios/mercado_potencial.html')

# View que renderiza a página de análise da concorrência
def analise_concorrencia(request):
    return render(request, 'planodenegocios/analise_concorrencia.html')

# View que renderiza a página de posicionamento
def posicionamento(request):
    return render(request, 'planodenegocios/posicionamento.html')

# View que renderiza a página de foco e segmentação
def foco(request):
    return render(request, 'planodenegocios/focosegmentacao.html')

# View que renderiza a página do plano de marketing ou ações
def plano(request):
    return render(request, 'planodenegocios/plano.html')

# View que renderiza a página de distribuição
def distribuicao(request):
    return render(request, 'planodenegocios/distribuicao.html')

# View que renderiza a página de histórico da empresa ou projeto
def historico(request):
    return render(request, 'planodenegocios/historico.html')

# View que renderiza a página de modelo de negócio
def modelo(request):
    return render(request, 'planodenegocios/modelo.html')

# View que renderiza a página de características do produto ou serviço
def caracteristicas(request):
    return render(request, 'planodenegocios/caracteristicas.html')

# View que renderiza a página de estágio de desenvolvimento
def estagio(request):
    return render(request, 'planodenegocios/estagio.html')

#View do complemento da administração e  gestão
def producao(request):
    return render(request, 'planodenegocios/producao.html')

def descricao(request):
    return render(request, 'planodenegocios/descricao.html')

def equipe(request):
    return render(request, 'planodenegocios/equipe.html')

def terceirizacao(request):
    return render(request, 'planodenegocios/terceirizacao.html')

def alianca(request):
    return render(request, 'planodenegocios/alianca.html')

def pesquisa(request):
    return render(request, 'planodenegocios/pesquisa.html')

def qualidade(request):
    return render(request, 'planodenegocios/qualidade.html')

#Plano de Implantação
def risco(request):
    return render(request, 'planodenegocios/analiseriscos.html')

def fatores(request):
    return render(request, 'planodenegocios/fatores.html')

def cronograma(request):
    return render(request, 'planodenegocios/cronograma.html')

def alternativa(request):
    return render(request, 'planodenegocios/alternativa.html')

# View principal para a funcionalidade de investimentos
def investimento(request):
    if request.method == 'POST':
        if 'form-investimento' in request.POST:  # Marca no input hidden
            # pegar dados do formulário de investimento
            data = request.POST.get('data')
            descricao = request.POST.get('descricao')
            quantidade = request.POST.get('quantidade')
            valor_unitario = request.POST.get('valor_unitario')
            depreciacao = request.POST.get('depreciacao')
            credito = request.POST.get('credito')

            investimento = Investimento(
                data=data,
                descricao=descricao,
                quantidade=int(quantidade),
                valor_unitario=float(valor_unitario),
                depreciacao=float(depreciacao),
                credito=float(credito),
                total=float(quantidade) * float(valor_unitario)
            )
            investimento.save()
            messages.success(request, "Investimento salvo com sucesso!")
            return redirect('investimento')

        elif 'form-ampliacao' in request.POST:  # Marca no input hidden
            # pegar dados do formulário de ampliação
            data = request.POST.get('data_ampliacao')
            descricao = request.POST.get('descricao_ampliacao')
            quantidade = request.POST.get('quantidade_ampliacao')
            valor_unitario = request.POST.get('valor_unitario_ampliacao')
            depreciacao = request.POST.get('depreciacao_ampliacao')
            credito = request.POST.get('credito_ampliacao')

            ampliacao = Ampliacoes(
                data=data,
                descricao=descricao,
                quantidade=int(quantidade),
                valor_unitario=float(valor_unitario),
                depreciacao=float(depreciacao),
                credito=float(credito),
                total=float(quantidade) * float(valor_unitario)
            )
            ampliacao.save()
            messages.success(request, "Ampliação salva com sucesso!")
            return redirect('investimento')

    # GET - listar dados
    investimentos = Investimento.objects.all()
    total = sum(item.total for item in investimentos)

    ampliacoes = Ampliacoes.objects.all()
    total_ampliacao = sum(item.total for item in ampliacoes)

    return render(request, 'planodenegocios/investimento.html', {
        'investimentos': investimentos,
        'total': total,
        'ampliacoes': ampliacoes,
        'total_ampliacao': total_ampliacao,
    })

def excluir_investimento(request, investimento_id):
    investimento = get_object_or_404(Investimento, id=investimento_id)  
    investimento.delete()
    messages.success(request, f'O investimento "{investimento.descricao}" foi excluído com sucesso!')
    return redirect('investimento')

def excluir_ampliacao(request, ampliacao_id):
    ampliacao = get_object_or_404(Ampliacoes, id=ampliacao_id)
    ampliacao.delete()
    messages.success(request, f'A ampliação "{ampliacao.descricao}" foi excluída com sucesso!')
    return redirect('investimento')

def equipe_propria(request):
    if request.method == 'POST':
        # === Verifica se é o formulário de equipe ===
        if 'form-equipe' in request.POST:
            cargo = request.POST.get('cargo', '').strip()
            quantidade = request.POST.get('quantidade')
            salario = request.POST.get('salario_inicial')

            if not cargo or not quantidade or not salario:
                messages.error(request, "Todos os campos são obrigatórios.")
                return redirect('equipe_propria')

            try:
                quantidade = int(quantidade)
                salario = Decimal(salario)
            except (ValueError, TypeError):
                messages.error(request, "Quantidade e salário devem ser números válidos.")
                return redirect('equipe_propria')

            funcionario = Funcionario(
                cargo=cargo,
                quantidade=quantidade,
                salario_inicial=salario,
            )
            funcionario.save()
            messages.success(request, "Funcionário adicionado com sucesso!")
            return redirect('equipe_propria')

        # === Verifica se é o formulário de encargos ===
        elif 'form-encargos' in request.POST:
            # Percentual médio
            percentual = request.POST.get('percentual_encargos', '0').replace(',', '.')
            try:
                percentual = float(percentual)
                encargo, _ = EncargoGlobal.objects.get_or_create(id=1)
                encargo.percentual = percentual
                encargo.save()
                messages.success(request, "Encargos atualizados com sucesso!")
            except:
                messages.error(request, "Percentual inválido.")

            return redirect('equipe_propria')

    # === Parte comum (GET) ===
    funcionarios = Funcionario.objects.all()
    dados_funcionarios = []
    total_salario_mensal = Decimal('0')

    for f in funcionarios:
        total_mensal = f.salario_inicial * f.quantidade
        total_salario_mensal += total_mensal

        dados_funcionarios.append({
            'funcionario': f,
            'total_ano_i': total_mensal * 12,
            'total_ano_ii': total_mensal * 12,
            'total_ano_iii': total_mensal * 12,
            'total_ano_iv': total_mensal * 12,
            'total_ano_v': total_mensal * 12,
        })

    # === Encargos sociais médios ===
    encargo = EncargoGlobal.objects.first()
    percentual_encargos = encargo.percentual if encargo else Decimal('0')
    percentual_encargos_decimal = Decimal(percentual_encargos) / Decimal('100')
    total_encargos_ano = total_salario_mensal * percentual_encargos_decimal * Decimal('12')

    # === Despesas com alimentação e transporte ===
    despesas_alimentacao = DespesaMensal.objects.filter(tipo='alimentacao')
    despesas_transporte = DespesaMensal.objects.filter(tipo='transporte')

    # --- Mês a mês (1 a 12) ---
    salarios_mes = []
    encargos_mes = []
    subtotal_mes = []
    alimentacao_mes = []
    transporte_mes = []
    total_geral_mes = []

    for mes in range(1, 13):
        salario_mes = sum(f.salario_inicial * f.quantidade for f in funcionarios)
        encargo_mes = salario_mes * percentual_encargos_decimal
        alimentacao = sum(d.valor for d in despesas_alimentacao if d.mes == mes)
        transporte = sum(d.valor for d in despesas_transporte if d.mes == mes)

        subtotal = salario_mes + encargo_mes
        total = subtotal + alimentacao + transporte

        salarios_mes.append(salario_mes)
        encargos_mes.append(encargo_mes)
        subtotal_mes.append(subtotal)
        alimentacao_mes.append(alimentacao)
        transporte_mes.append(transporte)
        total_geral_mes.append(total)

    # --- Totais por ano (12 em 12) ---
    def agrupar_em_anos(lista):
        return [sum(lista[i*12:(i+1)*12]) for i in range(5)]

    totais_salario = agrupar_em_anos(salarios_mes)
    totais_encargos = agrupar_em_anos(encargos_mes)
    totais_subtotal = agrupar_em_anos(subtotal_mes)
    totais_alimentacao = agrupar_em_anos(alimentacao_mes)
    totais_transporte = agrupar_em_anos(transporte_mes)
    totais_geral = agrupar_em_anos(total_geral_mes)

    # --- Soma de colaboradores ---
    total_colaboradores = sum(f.quantidade for f in funcionarios)

    # === Render ===
    return render(request, 'planodenegocios/equipe_propria.html', {
        'funcionarios': funcionarios,
        'dados_funcionarios': dados_funcionarios,
        'total_salario': total_salario_mensal,
        'total_colaboradores': total_colaboradores,
        'meses': range(1, 13),
        'percentual_encargos': percentual_encargos,
        'total_encargos_ano': total_encargos_ano,
        'salarios_mes': salarios_mes,
        'encargos_mes': encargos_mes,
        'subtotal_mes': subtotal_mes,
        'alimentacao_mes': alimentacao_mes,
        'transporte_mes': transporte_mes,
        'total_geral_mes': total_geral_mes,
        'totais_salario': totais_salario,
        'totais_encargos': totais_encargos,
        'totais_subtotal': totais_subtotal,
        'totais_alimentacao': totais_alimentacao,
        'totais_transporte': totais_transporte,
        'totais_geral': totais_geral,
    })

#Produtos e Serviços
def produto(request):
    produtos = ProdutoServico.objects.all()  # Corrigido o nome da variável e da classe

    return render(request, "planodenegocios/produto.html", {
        'produtos': produtos  # Também corrigido o nome passado para o template
    })

def cadastrar_produto(request):
    markup = None

    def to_float(valor):
        try:
            return float(valor)
        except (TypeError, ValueError):
            return 0.0

    if request.method == "POST":
        tipo = request.POST.get("tipo_de_produto")
        nome = request.POST.get("nome_produto")
        unidade = request.POST.get("unidade_venda")

        preco_venda_inserido = to_float(request.POST.get("preco_venda"))
        preco_venda_calculado = to_float(request.POST.get("precoVenda"))
        preco_compra = to_float(request.POST.get("precoCompra"))
        preco_varia = bool(request.POST.get("preco_varia"))

        # Decidir qual preço_venda usar para salvar (exemplo: priorizar o inserido manualmente)
        preco_venda_final = preco_venda_inserido if preco_venda_inserido > 0 else preco_venda_calculado

        if preco_compra > 0:
            markup = ((preco_venda_final - preco_compra) / preco_compra) * 100

        frete = request.POST.get("novo_frete") or "0"
        embalagem = request.POST.get("nova_embalagem") or ""
        nova_materia_prima = request.POST.get("nova_materia_prima") or ""

        try:
            produto = ProdutoServico.objects.create(
                tipo=tipo,
                nome=nome,
                unidade_venda=unidade,
                margem_lucro=markup or 0,
                preco_venda=preco_venda_final,
                preco_varia=preco_varia
            )

            if frete != "0" or embalagem or nova_materia_prima:
                CustoProducao.objects.create(
                    produto=produto.nome,
                    frete=float(frete),
                    embalagem=embalagem
                )

            messages.success(request, "Produto, serviço ou insumo salvo com sucesso!")
            return redirect("produto")

        except Exception as e:
            messages.error(request, f"Erro ao salvar: {str(e)}")

    return render(request, "planodenegocios/cadastrar_produto.html", {'markup': markup})


def excluir_produto(request, produto_id):
    produto = get_object_or_404(ProdutoServico, id=produto_id)
    produto.delete()
    messages.success(request, f'O produto/serviço "{produto.nome}" foi excluída com sucesso!')
    return redirect('produto')

