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
    path('investimento/editar/<int:investimento_id>/', views.editar_investimento, name='editar_investimento'),
    path('ampliacao/editar/<int:ampliacao_id>/', views.editar_ampliacao, name='editar_ampliacao'),

    path('investimento/excluir/<int:investimento_id>/', views.excluir_investimento, name='excluir_investimento'),
    path('ampliacoes/excluir/<int:ampliacao_id>/', views.excluir_ampliacao, name='excluir_ampliacao'),

    # Equipe própia
    path('equipe-propria/', views.equipe_propria, name='equipe_propria'),
    path('equipe_propria/editar/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),


    #Prestadores de Serviço
    path('terceiros/', views.terceiros, name='terceiros'),
    path('terceiros/excluir/<int:pk>/', views.excluir_terceiro, name='excluir_terceiro'),
    path('terceiros/excluir-todos/', views.excluir_todos_terceiros, name='excluir_todos_terceiros'),
    path('terceiros/editar/<int:id>/', views.editar_terceiro, name='editar_terceiro'),

    #Produtos e Serviços
    path('cadastrar_produtoservicos/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('produtoservicos/', views.produto, name='produto'),
    path('excluir_produtoservicos/<int:produto_id>', views.excluir_produto, name='excluir_produto'),

    path('despesas/', views.despesas, name='despesas'),  # redireciona para mês 1
    path('despesas/<int:mes>/', views.despesas_mes, name='despesas_mes'),
    path('despesas/cadastrar/<int:mes>/', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('despesas/editar/<int:mes>/<int:id>/', views.editar_despesa, name='editar_despesa'),
    path('despesas/excluir/<int:mes>/<int:id>/', views.excluir_despesa, name='excluir_despesa'),
    path('despesas/credito-tributario/', views.credito_tributario_view, name='credito_tributario'),

    #Valores
    path('remuneracao_dos_socios/', views.remuneracao_dos_socios, name='remuneracao_dos_socios'),
    path('valores/', views.distribuicao_valores_view, name='valores'),
    path('remuneracao_dos_socios/editar/<int:socio_id>/', views.editar_remuneracao_socio, name='editar_remuneracao_socio'),
    path('remuneracao_dos_socios/excluir/<int:pk>/', views.excluir_distribuicao, name='excluir_distribuicao'),

    #Visão Geral
    path('relatório_geral/', views.visao_geral, name='relatorio_geral'),

    #Relatório de PDF's
    path('relatorio/pdf/', views.gerar_relatorio_pdf, name='relatorio_pdf'), 

    #despesas
    path('receitas/', views.receitas, name='receitas'),

    #impostos
    path('impostos/', views.impostos, name='impostos')
]
