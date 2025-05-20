from django.shortcuts import render

def index(request):
    return render(request, 'planodenegocios/index.html')

def analise_setor(request):
    return render(request, 'planodenegocios/analise_setor.html')

def mercado_potencial(request):
    return render(request, 'planodenegocios/mercado_potencial.html')

def analise_concorrencia(request):
    return render(request, 'planodenegocios/analise_concorrencia.html')