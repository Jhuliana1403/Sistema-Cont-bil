# Importa as funções necessárias do Django para renderizar templates e redirecionar requisições
from django.shortcuts import render, redirect, get_object_or_404

from decimal import Decimal
# Importa o modelo Investimento do arquivo models.py
from .models import Investimento, CreditoTributario, AlternativasEstrategicas, Terceiro, Cronograma, FatoresCriticosSucesso, GestaoQualidade, Ampliacoes, ProdutoServico, CustoProducao, Funcionario, EncargoGlobal, DespesaAdministrativa, DespesaMensal, ResumoExecutivo, HistoricoMotivacao, ModeloNegocio, CaracteristicasBeneficios, EstagioDesenvolvimento, AnaliseSetor, MercadoPotencial, AnaliseConcorrencia, Posicionamento, FocoSegmentacao, PlanoPenetracaoMercado, ProdutosServicosInsumos, DescricaoLegalEstruturaSocietaria, Equipe, TerceirizacaoEquipeApoio, DistribuicaoComercializacao, AliancasParcerias, PesquisaDesenvolvimentoInovacao, AnaliseRiscos

from django.contrib import messages

from django.db.models import Sum

from django.forms import modelformset_factory

#Bibliotecas para a geração de pdf
from io import BytesIO
from django.http import FileResponse
from django.contrib.staticfiles import finders

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Frame, PageTemplate)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, gray


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

#Plano Financeiro
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

#Prestadores de Serviço
def terceiros(request):
    if request.method == "POST":
        nome = request.POST.get('nome', '').strip()
        quantidade = request.POST.get('quantidade', '0').strip()
        remuneracao = request.POST.get('remuneracao', '0').replace(',', '.').strip()

        if nome and quantidade.isdigit() and remuneracao:
            try:
                qtd_int = int(quantidade)
                rem_dec = float(remuneracao)
                if qtd_int > 0 and rem_dec >= 0:
                    Terceiro.objects.create(
                        nome=nome,
                        quantidade=qtd_int,
                        remuneracao=rem_dec,
                    )
                    return redirect('terceiros')
            except ValueError:
                pass

    terceiros = Terceiro.objects.all().order_by('nome')

    total_contratos = sum(t.quantidade for t in terceiros)
    soma_remuneracoes = sum(t.valor_inicial for t in terceiros)

    return render(request, 'planodenegocios/terceiros.html', {
        'terceiros': terceiros,
        'total_contratos': total_contratos,
        'soma_remuneracoes': soma_remuneracoes,
    })


def excluir_terceiro(request, pk):
    terceiro = get_object_or_404(Terceiro, pk=pk)
    terceiro.delete()
    return redirect('terceiros')


def excluir_todos_terceiros(request):
    Terceiro.objects.all().delete()
    return redirect('terceiros') 

#Produtos e Serviços
def produto(request):
    produtos = ProdutoServico.objects.all()  

    return render(request, "planodenegocios/produto.html", {
        'produtos': produtos  
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

#Visão Geral
def visao_geral(request):
    resumo = ResumoExecutivo.objects.first()
    historico = HistoricoMotivacao.objects.first()
    modelo = ModeloNegocio.objects.first()
    caracteristicas = CaracteristicasBeneficios.objects.first()
    estagio = EstagioDesenvolvimento.objects.first()
    setor = AnaliseSetor.objects.first()
    mercado = MercadoPotencial.objects.first()
    concorrencia = AnaliseConcorrencia.objects.first()
    posicionamento = Posicionamento.objects.first()
    foco = FocoSegmentacao.objects.first()
    plano = PlanoPenetracaoMercado.objects.first()
    distribuicao = DistribuicaoComercializacao.objects.first()
    producao = ProdutosServicosInsumos.objects.first()
    descricao = DescricaoLegalEstruturaSocietaria.objects.first()
    equipe = Posicionamento.objects.first()
    terceirizacao = TerceirizacaoEquipeApoio.objects.first()
    alianca = AliancasParcerias.objects.first()
    pesquisa = PesquisaDesenvolvimentoInovacao.objects.first()
    qualidade = GestaoQualidade.objects.first()
    risco = AnaliseRiscos.objects.first()
    fatores = FatoresCriticosSucesso.objects.first()
    cronograma = Cronograma.objects.first()
    alt = AlternativasEstrategicas.objects.first()

    sections = [
        ('Resumo Executivo', resumo),
        ('Histórico e Motivação', historico),
        ('Modelo de Negócio', modelo),
        ('Características e Benefícios', caracteristicas),
        ('Estágio de Desenvolvimento', estagio),
        ('Análise do Setor', setor),
        ('Mercado Potencial', mercado),
        ('Concorrência', concorrencia),
        ('Posicionamento', posicionamento),
        ('Foco', foco),
        ('Plano de Penetração no Mercado', plano),
        ('Distribuição e Comercialização', distribuicao),
        ('Produtos, Serviços e Insumos', producao),
        ('Descrição Legal e Estrutura Societária', descricao),
        ('Equipe', equipe),
        ('Terceiros', terceirizacao),
        ('Alianças e Parcerias', alianca),
        ('Pesquisa, Desenvolvimento e Inovação', pesquisa),
        ('Gestão de Qualidade', qualidade),
        ('Análise de Riscos', risco),
        ('Fatores Críticos de Sucesso', fatores),
        ('Cronograma', cronograma),
        ('Alternativas Estratégicas', alt),
    ]

    funcionarios = Funcionario.objects.all()
    funcionarios_data = []
    for f in funcionarios:
        total_mensal = f.quantidade * f.salario_inicial
        funcionarios_data.append({
            'nome': f.cargo,  # corrigido aqui
            'quantidade': f.quantidade,
            'salario_inicial': f.salario_inicial,
            'total_mensal': total_mensal,
        })


    context = {
        'sections': sections,
        'investimentos': Investimento.objects.all(),
        'total_investimentos': sum(i.total for i in Investimento.objects.all()),
        'terceiros': Terceiro.objects.all(),
        'total_terceiros': sum(t.quantidade for t in Terceiro.objects.all()),
        'total_remuneracoes': sum(t.valor_inicial for t in Terceiro.objects.all()),
        'funcionarios': funcionarios_data,
        'total_funcionarios': sum(f['quantidade'] for f in funcionarios_data),
        'total_salarios': sum(f['total_mensal'] for f in funcionarios_data),
        'produtos': ProdutoServico.objects.all(),
        'custos': {c.produto: c for c in CustoProducao.objects.all()},
        'despesas': DespesaAdministrativa.objects.all(),
        'total_despesas': sum(d.valor for d in DespesaAdministrativa.objects.all()),
        'creditos': CreditoTributario.objects.select_related('despesa').all(),
        'total_credito': sum(((c.despesa.valor * c.aliquota) / 100) for c in CreditoTributario.objects.select_related('despesa').all()),
    }

    return render(request, 'planodenegocios/visao_geral.html', context)

#PDF
class WatermarkCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        self.logo_path = kwargs.pop('logo_path', None)
        super().__init__(*args, **kwargs)

    def draw_watermark(self):
        if self.logo_path:
            w, h = A4
            logo_size = 14*cm
            self.saveState()
            self.setFillAlpha(0.1)
            x = (w - logo_size) / 1.5
            y = (h - logo_size) / 1.5
            self.drawImage(self.logo_path, x, y, width=logo_size, height=logo_size, mask='auto')
            self.restoreState()

    def draw_header(self):
        if self.logo_path:
            self.drawImage(self.logo_path, 2*cm, A4[1] - 3.5*cm, width=2.5*cm, height=2.5*cm, mask='auto')
        self.setFont('Helvetica-Bold', 18)
        self.setFillColor(HexColor("#1B365D"))  # azul escuro elegante
        self.drawCentredString(A4[0]/2, A4[1] - 2.5*cm, "Plano de Negócios - Empreenda+")

    def draw_footer(self):
        self.setFont('Helvetica', 9)
        self.setFillColor(gray)
        self.drawCentredString(A4[0]/2, 1.7*cm, f'Página {self.getPageNumber()}')

    def showPage(self):
        self.draw_watermark()
        self.draw_header()
        self.draw_footer()
        super().showPage()

    def save(self):
        self.draw_watermark()
        self.draw_header()
        self.draw_footer()
        super().save()
        
def gerar_relatorio_pdf(request):
    buffer = BytesIO()
    logo_path = finders.find('img/logo-favicon.png')

    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=2.5*cm, leftMargin=2.5*cm,
                            topMargin=4*cm, bottomMargin=3*cm)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Heading2Custom', parent=styles['Heading2'], fontSize=14,
                              leading=18, textColor=HexColor("#1B365D")))
    styles.add(ParagraphStyle(name='Heading3Custom', parent=styles['Heading3'], fontSize=12,
                              leading=14, textColor=gray))
    styles.add(ParagraphStyle(name='BodyTextCustom', parent=styles['Normal'], fontSize=11,
                              leading=15, alignment=TA_JUSTIFY))

    elementos = []

    def add_section(title, content):
        elementos.append(Paragraph(title, styles['Heading2Custom']))
        elementos.append(Paragraph(content, styles['BodyTextCustom']))

    def add_subsection(title, content):
        elementos.append(Paragraph(title, styles['Heading3Custom']))
        elementos.append(Paragraph(content, styles['BodyTextCustom']))

    if resumo := ResumoExecutivo.objects.first():
        add_section("Resumo Executivo", resumo.texto)

    if historico := HistoricoMotivacao.objects.first():
        add_section("Histórico e Motivação", historico.texto)

    if modelo := ModeloNegocio.objects.first():
        add_section("Modelo de Negócio", modelo.texto)

    caracteristicas = CaracteristicasBeneficios.objects.first()
    estagio = EstagioDesenvolvimento.objects.first()
    if caracteristicas or estagio:
        if caracteristicas:
            add_section("Características e Benefícios", caracteristicas.texto)
        if estagio:
            add_section("Estágio de Desenvolvimento", estagio.texto)

    if setor := AnaliseSetor.objects.first():
        add_section("Análise do Setor", setor.texto)

    if mercado := MercadoPotencial.objects.first():
        add_section("Mercado Potencial", mercado.texto)

    if concorrencia := AnaliseConcorrencia.objects.first():
        add_section("Concorrência", concorrencia.texto)

    if pos := Posicionamento.objects.first():
        add_section("Posicionamento", pos.texto)

    if foco := FocoSegmentacao.objects.first():
        add_section("Foco", foco.texto)

    if plano := PlanoPenetracaoMercado.objects.first():
        add_section("Plano de Penetração no Mercado", plano.texto)

    if distribuicao := DistribuicaoComercializacao.objects.first():
        add_section("Distribuição e Comercialização", distribuicao.texto)

    if producao := ProdutosServicosInsumos.objects.first():
        add_section("Produtos, Serviços e Insumos", producao.texto)

    if descricao := DescricaoLegalEstruturaSocietaria.objects.first():
        add_section("Descrição Legal e Estrutura Societária", descricao.texto)

    if equipe := Posicionamento.objects.first():
        add_section("Equipe", equipe.texto)

    if terceirizacao := TerceirizacaoEquipeApoio.objects.first():
        add_section("Terceiros", terceirizacao.texto)

    if alianca := AliancasParcerias.objects.first():
        add_section("Alianças e Parcerias", alianca.texto)

    if pesquisa := PesquisaDesenvolvimentoInovacao.objects.first():
        add_section("Pesquisa, Desenvolvimento e Inovação", pesquisa.texto)

    if qualidade := GestaoQualidade.objects.first():
        add_section("Gestão de Qualidade", qualidade.texto)

    if risco := AnaliseRiscos.objects.first():
        add_section("Análise de Riscos", risco.texto)

    if fatores := FatoresCriticosSucesso.objects.first():
        add_section("Fatores Críticos de Sucesso", fatores.texto)

    if cronograma := Cronograma.objects.first():
        add_section("Cronograma", cronograma.texto)

    if alt := AlternativasEstrategicas.objects.first():
        add_section("Alternativas Estratégicas", alt.texto)

    # Plano Financeiro - Investimentos
    investimentos = Investimento.objects.all()
    if investimentos.exists():
        total = sum(item.total for item in investimentos)
        add_section("Plano Financeiro", "")  # título principal, conteúdo vazio
        add_section("Investimentos", f"Total investido: R$ {total:,.2f}")

    # Prestadores de Serviço
    terceiros = Terceiro.objects.all()
    if terceiros.exists():
        total_remuneracoes = sum(t.valor_inicial for t in terceiros)
        total_terceiros = sum(t.quantidade for t in terceiros)
        add_section("Prestadores de Serviços", 
                    f"Total de Terceiros: {total_terceiros}\nValor Total Inicial: R$ {total_remuneracoes:,.2f}")

    # Equipe Própria
    funcionarios = Funcionario.objects.all()
    if funcionarios.exists():
        total_funcionarios = sum(f.quantidade for f in funcionarios)
        total_salarios = sum(f.quantidade * f.salario_inicial for f in funcionarios)
        add_section("Equipe Própria", 
                    f"Total de Funcionários: {total_funcionarios}\nTotal de Salários Mensais: R$ {total_salarios:,.2f}")

    # Produtos e Serviços Detalhados
    produtos = ProdutoServico.objects.all()
    if produtos.exists():
        add_section("Produtos e Serviços", "")
        for produto in produtos:
            elementos.append(Paragraph(
                f"<b>Nome:</b> {produto.nome} | <b>Tipo:</b> {produto.tipo} | <b>Unidade:</b> {produto.unidade_venda}",
                styles['BodyTextCustom']))
            elementos.append(Paragraph(
                f"<b>Preço de Venda:</b> R$ {produto.preco_venda:,.2f} | <b>Margem de Lucro:</b> {produto.margem_lucro:.2f}%",
                styles['BodyTextCustom']))

            custo = CustoProducao.objects.filter(produto=produto.nome).first()
            if custo:
                elementos.append(Paragraph(
                    f"<b>Frete:</b> R$ {custo.frete:,.2f} | <b>Embalagem:</b> {custo.embalagem or 'N/A'}",
                    styles['BodyTextCustom']))

    # Despesas Administrativas
    despesas = DespesaAdministrativa.objects.all()
    if despesas.exists():
        total_despesas = sum(d.valor for d in despesas)
        add_section("Despesas Administrativas", "")
        for d in despesas:
            elementos.append(Paragraph(f"{d.nome} (Mês {d.mes}) - R$ {d.valor:,.2f}", styles['BodyTextCustom']))
        elementos.append(Paragraph(f"Total Geral: R$ {total_despesas:,.2f}", styles['BodyTextCustom']))

    # Créditos Tributários
    creditos = CreditoTributario.objects.select_related('despesa').all()
    if creditos.exists():
        total_credito = Decimal('0')
        add_section("Créditos Tributários sobre Despesas", "")
        for c in creditos:
            valor_credito = (c.despesa.valor * c.aliquota) / Decimal('100')
            total_credito += valor_credito
            elementos.append(Paragraph(
                f"{c.despesa.nome} - Alíquota: {c.aliquota}% | Crédito: R$ {valor_credito:,.2f}", styles['BodyTextCustom']))
        elementos.append(Paragraph(f"Total de Créditos: R$ {total_credito:,.2f}", styles['BodyTextCustom']))


    doc.build(elementos, canvasmaker=lambda *args, **kwargs: WatermarkCanvas(*args, logo_path=logo_path, **kwargs))
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='plano_de_negocios.pdf')
