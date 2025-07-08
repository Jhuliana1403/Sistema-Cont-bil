function adicionarLinhaEquipe() {
  const tabela = document.getElementById("tabela-equipe").querySelector("tbody");
  const linha = document.createElement("tr");

  linha.innerHTML = `
    <td><input type="text" class="form-control" name="cargo" required></td>
    <td><input type="number" class="form-control quantidade" name="quantidade" min="0" value="0" required></td>
    <td><input type="number" class="form-control salario" name="salario_inicial" min="0" step="0.01" value="0.00" required></td>
    <td class="valor-inicial">R$ 0.00</td>
    <td>
      <button type="button" class="btn btn-outline-danger btn-sm remover-linha"><i class="bi bi-trash-fill"></i></button>
    </td>
  `;

  tabela.appendChild(linha);
  atualizarEventosInputsEquipe(linha);
  atualizarTotalEquipe();
}

function removerLinha(botao) {
  const linha = botao.closest("tr");
  linha.remove();
  atualizarTotalEquipe();
}

function atualizarEventosInputsEquipe(linha) {
  linha.querySelector(".quantidade").addEventListener("input", () => atualizarValorLinha(linha));
  linha.querySelector(".salario").addEventListener("input", () => atualizarValorLinha(linha));
  linha.querySelector(".remover-linha").addEventListener("click", function () {
    removerLinha(this);
  });
}

function atualizarValorLinha(linha) {
  const qtd = parseFloat(linha.querySelector(".quantidade").value) || 0;
  const sal = parseFloat(linha.querySelector(".salario").value) || 0;
  const total = qtd * sal;

  linha.querySelector(".valor-inicial").textContent = `R$ ${total.toFixed(2)}`;
  atualizarTotalEquipe();
}

function atualizarTotalEquipe() {
  let totalSalario = 0;
  let totalColaboradores = 0;
  const linhas = document.querySelectorAll("#tabela-equipe tbody tr");

  linhas.forEach(linha => {
    const qtd = parseFloat(linha.querySelector(".quantidade").value) || 0;
    const sal = parseFloat(linha.querySelector(".salario").value) || 0;
    totalColaboradores += qtd;
    totalSalario += qtd * sal;
  });

  document.getElementById("total-colaboradores").textContent = totalColaboradores;
  document.getElementById("total-salario").textContent = totalSalario.toFixed(2);
}

// Controle das abas (Equipe / Valores)
function ativarAbaEquipeValores(aba) {
  const btnEquipe = document.getElementById('btn-equipe');
  const btnValores = document.getElementById('btn-valores');
  const conteudoEquipe = document.getElementById('conteudo-equipe');
  const conteudoValores = document.getElementById('conteudo-valores');

  if (aba === 'equipe') {
    btnEquipe.classList.add('tab-btn-active');
    btnValores.classList.remove('tab-btn-active');
    conteudoEquipe.classList.remove('d-none');
    conteudoValores.classList.add('d-none');
  } else {
    btnValores.classList.add('tab-btn-active');
    btnEquipe.classList.remove('tab-btn-active');
    conteudoEquipe.classList.add('d-none');
    conteudoValores.classList.remove('d-none');
  }
}

document.getElementById('btn-equipe').addEventListener('click', () => ativarAbaEquipeValores('equipe'));
document.getElementById('btn-valores').addEventListener('click', () => ativarAbaEquipeValores('valores'));
