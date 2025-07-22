# Importa as funções necessárias do Django para renderizar templates e redirecionar requisições
from django.shortcuts import render, redirect, get_object_or_404

from decimal import Decimal
# Importa o modelo Investimento do arquivo models.py
from .models import Investimento, CreditoTributario, ValorMensalDistribuicao, DistribuicaoLucro, Socio, Empresa, AlternativasEstrategicas, Cronograma, FatoresCriticosSucesso, GestaoQualidade, Ampliacoes, ProdutoServico, CustoProducao, Funcionario, EncargoGlobal, DespesaAdministrativa, DespesaMensal, ResumoExecutivo, HistoricoMotivacao, ModeloNegocio, CaracteristicasBeneficios, EstagioDesenvolvimento, AnaliseSetor, MercadoPotencial, AnaliseConcorrencia, Posicionamento, FocoSegmentacao, PlanoPenetracaoMercado, ProdutosServicosInsumos, DescricaoLegalEstruturaSocietaria, Equipe, TerceirizacaoEquipeApoio, DistribuicaoComercializacao, AliancasParcerias, PesquisaDesenvolvimentoInovacao, AnaliseRiscos

from django.contrib import messages

from django.db.models import Sum

from django.forms import modelformset_factory

from datetime import date

# Resumo Executivo
def index(request):
    resumo, created = ResumoExecutivo.objects.get_or_create(id=1)

    if request.method == "POST":
        resumo.texto = request.POST.get("texto", "")
        resumo.save()
        return redirect("inicio")  

    return render(request, "planodenegocios/textos/index.html", {"resumo": resumo})

#O negócio

def historico(request):
    historico, created = HistoricoMotivacao.objects.get_or_create(id=1)

    if request.method == "POST":
        historico.texto = request.POST.get("texto", "")
        historico.save()
        return redirect("historico")  # nome da URL

    return render(request, "planodenegocios/textos/o negocio/historico.html", {"historico": historico})


def modelo(request):
    modelo, created = ModeloNegocio.objects.get_or_create(id=1)

    if request.method == "POST":
        modelo.texto = request.POST.get("texto", "")
        modelo.save()
        return redirect("modelo")  # nome da URL

    return render(request, "planodenegocios/textos/o negocio/modelo.html", {"modelo": modelo})

#Produtos e Serviços
def caracteristicas(request):
    caracteristicas, created = CaracteristicasBeneficios.objects.get_or_create(id=1)

    if request.method == "POST":
        caracteristicas.texto = request.POST.get("texto", "")
        caracteristicas.save()
        return redirect("caracteristicas")  

    return render(request, "planodenegocios/textos/produtos e serviços/caracteristicas.html", {"caracteristicas": caracteristicas})

def estagio(request):
    estagio, created = EstagioDesenvolvimento.objects.get_or_create(id=1)

    if request.method == "POST":
        estagio.texto = request.POST.get("texto", "")
        estagio.save()
        return redirect("estagio")  

    return render(request, "planodenegocios/textos/produtos e serviços/estagio.html", {"estagio": estagio})

#Ambiente de negócio
def analise_setor(request):
    analise, created = AnaliseSetor.objects.get_or_create(id=1)

    if request.method == "POST":
        analise.texto = request.POST.get("texto", "")
        analise.save()
        return redirect("analise_setor")  
    return render(request, "planodenegocios/textos/o ambiente de negócio/analise_setor.html", {"analise": analise})

def mercado_potencial(request):
    mercado, created = MercadoPotencial.objects.get_or_create(id=1)

    if request.method == "POST":
        texto = request.POST.get("texto", "")
        mercado.texto = texto
        mercado.save()
        messages.success(request, "Mercado potencial salvo com sucesso!")
        return redirect("mercado_potencial") 

    return render(request, "planodenegocios/textos/o ambiente de negócio/mercado_potencial.html", {"mercado": mercado})

def analise_concorrencia(request):
    analise, created = AnaliseConcorrencia.objects.get_or_create(id=1)

    if request.method == "POST":
        texto = request.POST.get("texto", "")
        analise.texto = texto
        analise.save()
        messages.success(request, "Análise de concorrência salva com sucesso!")
        return redirect("analise_concorrencia")  

    return render(request, "planodenegocios/textos/o ambiente de negócio/analise_concorrencia.html", {"analise": analise})

#Estratégias de Marketing
def posicionamento(request):
    pos, created = Posicionamento.objects.get_or_create(id=1)

    if request.method == "POST":
        texto = request.POST.get("texto", "")
        pos.texto = texto
        pos.save()
        messages.success(request, "Posicionamento salvo com sucesso!")
        return redirect("posicionamento") 

    return render(request, "planodenegocios/textos/estratégias de marketing/posicionamento.html", {"posicionamento": pos})


def foco(request):
    foco, created = FocoSegmentacao.objects.get_or_create(id=1)

    if request.method == "POST":
        foco.texto = request.POST.get("texto", "")
        foco.save()
        return redirect("foco")  

    return render(request, "planodenegocios/textos/estratégias de marketing/focosegmentacao.html", {"foco": foco})


def plano(request):
    plano, created = PlanoPenetracaoMercado.objects.get_or_create(id=1)

    if request.method == "POST":
        plano.texto = request.POST.get("texto", "")
        plano.save()
        return redirect("plano")  

    return render(request, "planodenegocios/textos/estratégias de marketing/plano.html", {"plano": plano})

def distribuicao(request):
    distribuicao, created = DistribuicaoComercializacao.objects.get_or_create(id=1)
    
    if request.method == "POST":
        distribuicao.texto = request.POST.get("texto", "")
        distribuicao.save()
        return redirect("distribuicao") 

    return render(request, "planodenegocios/textos/estratégias de marketing/distribuicao.html", {"distribuicao": distribuicao})

#Administração e Gestão
def producao(request):
    psi, created = ProdutosServicosInsumos.objects.get_or_create(id=1)

    if request.method == "POST":
        psi.texto = request.POST.get("texto", "")
        psi.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("producao")

    return render(request, "planodenegocios/textos/administração e gestão/producao.html", {
        "psi": psi
    })

def descricao(request):
    desc, created = DescricaoLegalEstruturaSocietaria.objects.get_or_create(id=1)

    if request.method == "POST":
        desc.texto = request.POST.get("texto", "")
        desc.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("descricao")

    return render(request, "planodenegocios/textos/administração e gestão/descricao.html", {
        "desc": desc
    })

def equipe(request):
    equipe, created = Equipe.objects.get_or_create(id=1)

    if request.method == "POST":
        equipe.texto = request.POST.get("texto", "")
        equipe.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("equipe")

    return render(request, "planodenegocios/textos/administração e gestão/equipe.html", {
        "equipe": equipe
    })


def terceirizacao(request):
    apoio, created = TerceirizacaoEquipeApoio.objects.get_or_create(id=1)

    if request.method == "POST":
        apoio.texto = request.POST.get("texto", "")
        apoio.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("terceirizacao")

    return render(request, "planodenegocios/textos/administração e gestão/terceirizacao.html", {
        "apoio": apoio
    })

def alianca(request):
    alianças, created = AliancasParcerias.objects.get_or_create(id=1)

    if request.method == "POST":
        alianças.texto = request.POST.get("texto", "")
        alianças.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("alianca")

    return render(request, "planodenegocios/textos/administração e gestão/alianca.html", {
        "aliancas": alianças
    })

def pesquisa(request):
    pdi, created = PesquisaDesenvolvimentoInovacao.objects.get_or_create(id=1)

    if request.method == "POST":
        pdi.texto = request.POST.get("texto", "")
        pdi.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("pesquisa")

    return render(request, "planodenegocios/textos/administração e gestão/pesquisa.html", {
        "pdi": pdi
    })

def qualidade(request):
    gestao, created = GestaoQualidade.objects.get_or_create(id=1)

    if request.method == "POST":
        gestao.texto = request.POST.get("texto", "")
        gestao.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("qualidade")

    return render(request, "planodenegocios/textos/administração e gestão/qualidade.html", {
        "gestao": gestao
    })

#Plano de Implantação
def risco(request):
    analise, created = AnaliseRiscos.objects.get_or_create(id=1)

    if request.method == "POST":
        analise.texto = request.POST.get("texto", "")
        analise.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("risco")

    return render(request, "planodenegocios/textos/plano de implantação/analiseriscos.html", {
        "analise": analise
    })

def fatores(request):
    fatores, created = FatoresCriticosSucesso.objects.get_or_create(id=1)

    if request.method == "POST":
        fatores.texto = request.POST.get("texto", "")
        fatores.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("fatores")

    return render(request, "planodenegocios/textos/plano de implantação/fatores.html", {
        "fatores": fatores
    })

def cronograma(request):
    cronograma_obj, created = Cronograma.objects.get_or_create(id=1)

    if request.method == "POST":
        cronograma_obj.texto = request.POST.get("texto", "")
        cronograma_obj.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("cronograma")

    return render(request, "planodenegocios/textos/plano de implantação/cronograma.html", {
        "cronograma": cronograma_obj
    })

def alternativa(request):
    alt, created = AlternativasEstrategicas.objects.get_or_create(id=1)

    if request.method == "POST":
        alt.texto = request.POST.get("texto", "")
        alt.save()
        messages.success(request, "Texto salvo com sucesso.")
        return redirect("alternativa")

    return render(request, "planodenegocios/textos/plano de implantação/alternativa.html", {
        "alt": alt
    })

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


#Despesas administrativas
def despesas(request):
    # Redireciona para o mês 1 por padrão
    return redirect('despesas_mes', mes=1)

def despesas_mes(request, mes=None):
    if mes is None:
        mes = 1

    despesas = DespesaAdministrativa.objects.filter(mes=mes)
    total_mes = despesas.aggregate(Sum('valor'))['valor__sum'] or 0
    total_geral = DespesaAdministrativa.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    meses = list(range(1, 13))

    return render(request, 'planodenegocios/despesas.html', {
        'despesas': despesas,
        'total_mes': total_mes,
        'total_geral': total_geral,
        'mes_selecionado': mes,
        'meses': meses,
    })

def cadastrar_despesa(request, mes=None):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        mes = mes or request.POST.get('mes')
        DespesaAdministrativa.objects.create(nome=nome, valor=valor, mes=mes)
        return redirect('despesas_mes', mes=mes)

    return render(request, 'planodenegocios/cadastrar_despesa.html', {
        'mes': mes,
    })

def editar_despesa(request, id, mes=None):
    despesa = get_object_or_404(DespesaAdministrativa, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        valor = request.POST.get('valor', '').strip()
        mes_post = request.POST.get('mes')  # Pega o mês enviado no form

        if not nome or not valor:
            messages.error(request, "Preencha todos os campos.")
            return redirect('editar_despesa', id=id, mes=mes_post or mes)

        try:
            valor_float = float(valor)
            despesa.nome = nome
            despesa.valor = valor_float
            despesa.save()
            messages.success(request, "Despesa atualizada com sucesso!")
            # Redireciona para a página do mês enviado no form (POST)
            return redirect('despesas_mes', mes=mes_post or mes)
        except ValueError:
            messages.error(request, "Valor inválido.")
            return redirect('editar_despesa', id=id, mes=mes_post or mes)

    # GET request: usa o mes recebido pela URL ou o mês da despesa
    return render(request, 'planodenegocios/editar_despesa.html', {
        'despesa': despesa,
        'mes': mes or despesa.mes,
    })

def excluir_despesa(request, mes, id):
    despesa = get_object_or_404(DespesaAdministrativa, id=id)
    despesa.delete()
    return redirect('despesas_mes', mes=mes)

#Crédito tributário de despesas administrativas

def credito_tributario_view(request):
    despesas = DespesaAdministrativa.objects.all()
    # Carrega todos os créditos já cadastrados em um dicionário para lookup rápido
    creditos = {c.despesa_id: c for c in CreditoTributario.objects.all()}

    if request.method == 'POST':
        for despesa in despesas:
            aliquota_str = request.POST.get(f'aliquota_{despesa.id}', '').strip()
            try:
                aliquota = Decimal(aliquota_str) if aliquota_str else Decimal('0')
            except:
                aliquota = Decimal('0')

            if aliquota > 0:
                # Atualiza ou cria apenas para a despesa em questão
                if despesa.id in creditos:
                    credito = creditos[despesa.id]
                    credito.aliquota = aliquota
                    credito.save()
                else:
                    CreditoTributario.objects.create(despesa=despesa, aliquota=aliquota)
            else:
                # NÃO altera nada se o valor é 0 (mantém o que já tinha no banco)
                pass

        return redirect('credito_tributario')  # use o nome correto da URL

    # Prepara os dados para o formulário
    despesas_com_creditos = []
    for despesa in despesas:
        aliquota = creditos[despesa.id].aliquota if despesa.id in creditos else Decimal('0.00')
        despesas_com_creditos.append({'despesa': despesa, 'aliquota': aliquota})

    # Prepara o resumo
    lista_calculos = []
    for credito in CreditoTributario.objects.select_related('despesa'):
        valor_credito = (credito.despesa.valor * credito.aliquota) / Decimal('100.00')
        lista_calculos.append({
            'nome': credito.despesa.nome,
            'valor_despesa': credito.despesa.valor,
            'aliquota': credito.aliquota,
            'valor_credito': valor_credito,
        })

    return render(request, 'planodenegocios/credito_tributario.html', {
        'despesas_com_creditos': despesas_com_creditos,
        'lista_calculos': lista_calculos,
    })

#Valores
def remumeração_dos_socios(request):
    if request.method == 'POST':
        # Limpa todas as distribuições existentes para evitar duplicados
        DistribuicaoLucro.objects.all().delete()
        empresa_obj = Empresa.objects.first()

        # Pega todos os sócios e valores enviados no POST
        socios_valores = []
        for key, value in request.POST.items():
            if key.startswith('socio_'):
                # Extrai o índice do campo para pegar o valor correspondente
                index = key.split('_')[1]
                nome_socio = value.strip()
                valor_str = request.POST.get(f'valor_{index}', '0').replace(',', '.').strip()
                try:
                    valor = float(valor_str) if valor_str else 0
                except ValueError:
                    valor = 0

                if nome_socio:  # só processa se o nome não for vazio
                    socios_valores.append((nome_socio, valor))

        # Salva os sócios e suas distribuições
        for nome_socio, valor in socios_valores:
            socio_obj, created = Socio.objects.get_or_create(nome=nome_socio)
            DistribuicaoLucro.objects.create(
                socio=socio_obj,
                valor_inicial=valor,
                mes_referencia=date.today(), # ou outra data que fizer sentido
                empresa=empresa_obj
            )

        # Redireciona para a mesma página para mostrar os dados atualizados
        return redirect('remumeração_dos_socios')  # ajuste o nome da url conforme seu urls.py

    else:
        # No GET, recupera todas as distribuições para mostrar no form
        distribuicoes = DistribuicaoLucro.objects.select_related('socio').all()
        return render(request, 'planodenegocios/remumeração_dos_socios.html', {
            'distribuicoes': distribuicoes
        })

def distribuicao_valores_view(request):
    distribuicoes = DistribuicaoLucro.objects.all().select_related('socio')
    socios_valores = []

    for dist in distribuicoes:
        # Garante que os 12 valores mensais existem
        if not dist.valores_mensais.exists():
            for mes in range(1, 13):
                ValorMensalDistribuicao.objects.create(
                    distribuicao=dist,
                    mes=mes,
                    valor=dist.valor_inicial,
                    constante=True
                )

        valores_mensais = ValorMensalDistribuicao.objects.filter(distribuicao=dist).order_by('mes')
        valores = [f"{v.valor:.2f}".replace('.', ',') for v in valores_mensais]
        
        socios_valores.append({
            'nome': dist.socio.nome,
            'valores': valores,
        })

    return render(request, 'planodenegocios/valores.html', {
        'socios_valores': socios_valores,
        'meses': range(1, 13)
    })