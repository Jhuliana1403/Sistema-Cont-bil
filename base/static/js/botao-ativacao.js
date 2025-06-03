  const btnInvestimento = document.getElementById('btn-investimento');
  const btnAmpliacoes = document.getElementById('btn-ampliacoes');
  const conteudoInvestimento = document.getElementById('conteudo-investimento');
  const conteudoAmpliacoes = document.getElementById('conteudo-ampliacoes');

  function ativarAba(aba) {
    if(aba === 'investimento') {
      btnInvestimento.classList.add('tab-btn-active');
      btnAmpliacoes.classList.remove('tab-btn-active');
      conteudoInvestimento.style.display = 'block';
      conteudoAmpliacoes.style.display = 'none';
    } else {
      btnAmpliacoes.classList.add('tab-btn-active');
      btnInvestimento.classList.remove('tab-btn-active');
      conteudoInvestimento.style.display = 'none';
      conteudoAmpliacoes.style.display = 'block';
    }
  }

  btnInvestimento.addEventListener('click', () => ativarAba('investimento'));
  btnAmpliacoes.addEventListener('click', () => ativarAba('ampliacoes'));