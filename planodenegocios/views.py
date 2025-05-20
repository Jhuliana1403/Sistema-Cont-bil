from django.shortcuts import render

def index(request):
    return render(request, 'planodenegocios/index.html')

def posicionamento(request):
    return render(request, 'planodenegocios/posicionamento.html')

def foco(request):
    return render(request, 'planodenegocios/focosegmentacao.html')

def plano(request):
    return render(request, 'planodenegocios/plano.html')

def distribuicao(request):
    return render(request, 'planodenegocios/distribuicao.html')