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

    #Administração e Gestão
    path('administracao/producao/', views.producao, name='producao'),
    path('administracao/descricao/', views.descricao, name='descricao'),
    path('administracao/equipe/', views.equipe, name='equipe'),
    path('administracao/terceirizacao/', views.terceirizacao, name='terceirizacao'),
    path('administracao/alianca/', views.alianca, name='alianca'),
    path('administracao/pesquisa/', views.pesquisa, name='pesquisa'),
    path('administracao/qualidade/', views.qualidade, name='qualidade'),

    #Plano de Implantação
    path('planodeimplantacao/analiserisco/', views.risco, name='risco'),
    path('planodeimplantacao/fatores/', views.fatores, name='fatores'),
    path('planodeimplantacao/cronograma/', views.cronograma, name='cronograma'),
    path('planodeimplantacao/alternativa/', views.alternativa, name='alternativa'),

    # Investimentos e ampliações
    path('investimento/', views.investimento, name='investimento'),
    path('investimento/excluir/<int:investimento_id>/', views.excluir_investimento, name='excluir_investimento'),
    path('ampliacoes/excluir/<int:ampliacao_id>/', views.excluir_ampliacao, name='excluir_ampliacao'),

    # Equipe própia
    path('equipe-propria/', views.equipe_propria, name='equipe_propria'),

    #Produtos e Serviços
    path('cadastrar_produtoservicos/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtoservicos/', views.produto, name='produto'),
    path('excluir_produtoservicos/<int:produto_id>', views.excluir_produto, name='excluir_produto'),

    path('despesas/', views.despesas, name='despesas'),  # redireciona para mês 1
    path('despesas/<int:mes>/', views.despesas_mes, name='despesas_mes'),
    path('despesas/cadastrar/<int:mes>/', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('despesas/editar/<int:mes>/<int:id>/', views.editar_despesa, name='editar_despesa'),
    path('despesas/excluir/<int:mes>/<int:id>/', views.excluir_despesa, name='excluir_despesa'),
    path('despesas/credito-tributario/', views.credito_tributario_view, name='credito_tributario'),

]
