# Importa as funções necessárias do Django para renderizar templates e redirecionar requisições
from django.shortcuts import render, redirect, get_object_or_404

# Importa o modelo Investimento do arquivo models.py
from .models import Investimento

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

# (DUPLICADA) View da análise de setor (já foi declarada acima)
def analise_setor(request):
    return render(request, 'planodenegocios/analise_setor.html')

# (DUPLICADA) View de mercado potencial (já foi declarada acima)
def mercado_potencial(request):
    return render(request, 'planodenegocios/mercado_potencial.html')

# (DUPLICADA) View da análise da concorrência (já foi declarada acima)
def analise_concorrencia(request):
    return render(request, 'planodenegocios/analise_concorrencia.html')

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
    # Verifica se o método da requisição é POST (formulário enviado)
    if request.method == 'POST':
        # Pega o valor do campo 'descricao' do formulário
        descricao = request.POST.get('descricao')

        # Captura e converte os valores do formulário, usando 0 como valor padrão
        quantidade = int(request.POST.get('quantidade') or 0)
        valor_unitario = float(request.POST.get('valor_unitario') or 0)
        total = quantidade * valor_unitario  # Calcula o valor total

        # Cria e salva um novo objeto Investimento no banco de dados
        Investimento.objects.create(
            data=request.POST.get('data'),
            descricao=descricao,
            quantidade=quantidade,
            valor_unitario=valor_unitario,
            depreciacao=float(request.POST.get('depreciacao') or 0),
            credito=float(request.POST.get('credito') or 0),
            total=total
        )

        # Após salvar, redireciona para a mesma página (evita reenvio do formulário ao recarregar)
        return redirect('investimento')

    # Se não for POST, ou seja, for uma requisição GET, carrega todos os investimentos
    investimentos = Investimento.objects.all()
    total = sum(item.total for item in investimentos)  # Soma total dos investimentos

    # Renderiza a página de investimentos com os dados
    return render(request, 'planodenegocios/investimento.html', {
        'investimentos': investimentos,
        'total': total
    })

def excluir_investimento(request, investimento_id):
    investimento = get_object_or_404(Investimento, id=investimento_id)  
    investimento.delete()
    messages.success(request, f'O investimento "{investimento.descricao}" foi excluído com sucesso!')
    return redirect('investimento')  # Certifique-se de que 'investimento' é o nome da URL correta
