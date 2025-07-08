// Abas: Investimento Inicial / Ampliações
const btnInvestimento = document.getElementById('btn-investimento');
const btnAmpliacoes = document.getElementById('btn-ampliacoes');
const conteudoInvestimento = document.getElementById('conteudo-investimento');
const conteudoAmpliacoes = document.getElementById('conteudo-ampliacao');

function ativarAba(aba) {
  if (aba === 'investimento') {
    btnInvestimento?.classList.add('tab-btn-active');
    btnAmpliacoes?.classList.remove('tab-btn-active');
    conteudoInvestimento?.classList.remove('d-none');
    conteudoAmpliacoes?.classList.add('d-none');
  } else {
    btnAmpliacoes?.classList.add('tab-btn-active');
    btnInvestimento?.classList.remove('tab-btn-active');
    conteudoInvestimento?.classList.add('d-none');
    conteudoAmpliacoes?.classList.remove('d-none');
  }
}

if (btnInvestimento && btnAmpliacoes) {
  btnInvestimento.addEventListener('click', () => ativarAba('investimento'));
  btnAmpliacoes.addEventListener('click', () => ativarAba('ampliacao'));
}

// Abas: Produto ou Serviço / Custo de Produção
const btnProdutoServico = document.getElementById('btn-produto-servico');
const btnCustoProducao = document.getElementById('btn-custo-producao');
const conteudoProdutoServico = document.getElementById('conteudo-produto-servico');
const conteudoCustoProducao = document.getElementById('conteudo-custo-producao');

function ativarAbaFormulario(aba) {
  if (aba === 'produto') {
    btnProdutoServico?.classList.add('tab-btn-active');
    btnCustoProducao?.classList.remove('tab-btn-active');
    conteudoProdutoServico?.classList.remove('d-none');
    conteudoCustoProducao?.classList.add('d-none');
  } else {
    btnCustoProducao?.classList.add('tab-btn-active');
    btnProdutoServico?.classList.remove('tab-btn-active');
    conteudoProdutoServico?.classList.add('d-none');
    conteudoCustoProducao?.classList.remove('d-none');
  }
}

if (btnProdutoServico && btnCustoProducao) {
  btnProdutoServico.addEventListener('click', () => ativarAbaFormulario('produto'));
  btnCustoProducao.addEventListener('click', () => ativarAbaFormulario('custo'));
}
