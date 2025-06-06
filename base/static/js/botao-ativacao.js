const btnInvestimento = document.getElementById('btn-investimento');
const btnAmpliacoes = document.getElementById('btn-ampliacoes');
const conteudoInvestimento = document.getElementById('conteudo-investimento');
const conteudoAmpliacoes = document.getElementById('conteudo-ampliacao'); 

function ativarAba(aba) {
  if (aba === 'investimento') {
    btnInvestimento.classList.add('tab-btn-active');
    btnAmpliacoes.classList.remove('tab-btn-active');
    conteudoInvestimento.classList.remove('d-none');
    conteudoAmpliacoes.classList.add('d-none');
  } else {
    btnAmpliacoes.classList.add('tab-btn-active');
    btnInvestimento.classList.remove('tab-btn-active');
    conteudoInvestimento.classList.add('d-none');
    conteudoAmpliacoes.classList.remove('d-none');
  }
}

btnInvestimento.addEventListener('click', () => ativarAba('investimento'));
btnAmpliacoes.addEventListener('click', () => ativarAba('ampliacao'));
