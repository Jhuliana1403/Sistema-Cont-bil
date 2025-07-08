# Importa as funções necessárias do Django para renderizar templates e redirecionar requisições
from django.shortcuts import render, redirect, get_object_or_404

# Importa o modelo Investimento do arquivo models.py
from .models import Investimento, Ampliacoes, ProdutoServico, CustoProducao

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
