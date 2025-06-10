from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.index, name='inicio'),

    # Análises de mercado
    path('analise-setor/', views.analise_setor, name='analise_setor'),
    path('mercado-potencial/', views.mercado_potencial, name='mercado_potencial'),
    path('analise-concorrencia/', views.analise_concorrencia, name='analise_concorrencia'),

    # Marketing
    path('marketing/posicionamento/', views.posicionamento, name='posicionamento'),
    path('marketing/focosegmentacao/', views.foco, name='foco'),
    path('marketing/plano/', views.plano, name='plano'),
    path('marketing/distribuicao/', views.distribuicao, name='distribuicao'),

    # Histórico e Modelo de Negócio
    path('historico/', views.historico, name='historico'),
    path('modelo/', views.modelo, name='modelo'),
    path('caracteristicas/', views.caracteristicas, name='caracteristicas'),
    path('estagio/', views.estagio, name='estagio'),

    # Investimentos e ampliações
    path('investimento/', views.investimento, name='investimento'),
    path('investimento/excluir/<int:investimento_id>/', views.excluir_investimento, name='excluir_investimento'),
    path('ampliacoes/excluir/<int:ampliacao_id>/', views.excluir_ampliacao, name='excluir_ampliacao'),

    # Equipe própia
    path('equipe-propria/', views.equipe_propria, name='equipe_propria'),

]
