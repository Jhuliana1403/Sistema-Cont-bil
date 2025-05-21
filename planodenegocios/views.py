from django.shortcuts import render

def index(request):
    return render(request, 'planodenegocios/index.html')

def analise_setor(request):
    return render(request, 'planodenegocios/analise_setor.html')

def mercado_potencial(request):
    return render(request, 'planodenegocios/mercado_potencial.html')

def analise_concorrencia(request):
    return render(request, 'planodenegocios/analise_concorrencia.html')

def posicionamento(request):
    return render(request, 'planodenegocios/posicionamento.html')

def foco(request):
    return render(request, 'planodenegocios/focosegmentacao.html')

def plano(request):
    return render(request, 'planodenegocios/plano.html')

def distribuicao(request):
    return render(request, 'planodenegocios/distribuicao.html')

