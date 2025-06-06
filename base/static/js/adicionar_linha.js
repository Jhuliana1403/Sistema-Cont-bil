function adicionarInvestimento() {
  const tabela = document.getElementById("tabela-investimentos").querySelector("tbody");
  const linha = document.createElement("tr");

  linha.innerHTML = `
    <td><input type="date" class="form-control" name="data" required></td>
    <td><input type="text" class="form-control" name="descricao" required></td>
    <td><input type="number" class="form-control quantidade" name="quantidade" min="0" value="0" required></td>
    <td><input type="number" class="form-control valor_unitario" name="valor_unitario" min="0" step="0.01" value="0.00" required></td>
    <td><input type="number" class="form-control" name="depreciacao" min="0" step="0.01" value="0" required></td>
    <td><input type="number" class="form-control" name="credito" min="0" step="0.01" value="0" required></td>
    <td>
      <button type="button" class="btn btn-outline-danger btn-sm remover-linha"><i class="bi bi-trash-fill"></i></button>
    </td>
  `;

  tabela.appendChild(linha);
  atualizarEventosInputs(linha);
  atualizarTotal();
}

function adicionarLinhaAmpliacao() {
  const tabela = document.getElementById("tabela-ampliacao").querySelector("tbody");
  const linha = document.createElement("tr");

  linha.innerHTML = `
    <td><input type="date" class="form-control" name="data_ampliacao" required></td>
    <td><input type="text" class="form-control" name="descricao_ampliacao" required></td>
    <td><input type="number" class="form-control quantidade_ampliacao" name="quantidade_ampliacao" min="0" value="0" required></td>
    <td><input type="number" class="form-control valor_unitario_ampliacao" name="valor_unitario_ampliacao" min="0" step="0.01" value="0.00" required></td>
    <td><input type="number" class="form-control" name="depreciacao_ampliacao" min="0" step="0.01" value="0" required></td>
    <td><input type="number" class="form-control" name="credito_ampliacao" min="0" step="0.01" value="0" required></td>
    <td>
      <button type="button" class="btn btn-outline-danger btn-sm remover-linha"><i class="bi bi-trash-fill"></i></button>
    </td>
  `;

  tabela.appendChild(linha);
  atualizarEventosInputsAmpliacao(linha);
  atualizarTotalAmpliacao();
}

function removerLinha(botao) {
  const linha = botao.closest("tr");
  const tabelaId = linha.closest("table").id;

  linha.remove();

  if (tabelaId === "tabela-investimentos") {
    atualizarTotal();
  } else if (tabelaId === "tabela-ampliacao") {
    atualizarTotalAmpliacao();
  }
}

function atualizarEventosInputs(linha) {
  linha.querySelector(".quantidade").addEventListener("input", atualizarTotal);
  linha.querySelector(".valor_unitario").addEventListener("input", atualizarTotal);
  linha.querySelector(".remover-linha").addEventListener("click", function () {
    removerLinha(this);
  });
}

function atualizarEventosInputsAmpliacao(linha) {
  linha.querySelector(".quantidade_ampliacao").addEventListener("input", atualizarTotalAmpliacao);
  linha.querySelector(".valor_unitario_ampliacao").addEventListener("input", atualizarTotalAmpliacao);
  linha.querySelector(".remover-linha").addEventListener("click", function () {
    removerLinha(this);
  });
}

function atualizarTotal() {
  let total = 0;
  const linhas = document.querySelectorAll("#tabela-investimentos");

  linhas.forEach(linha => {
    const qtd = linha.querySelector(".quantidade");
    const val = linha.querySelector(".valor_unitario");

    if (qtd && val) {
      const q = parseFloat(qtd.value) || 0;
      const v = parseFloat(val.value) || 0;
      total += q * v;
    }
  });

  document.getElementById("total-geral").textContent = total.toFixed(2);
}

function atualizarTotalAmpliacao() {
  let total = 0;
  const linhas = document.querySelectorAll("#tabela-ampliacao tbody tr");

  linhas.forEach(linha => {
    const qtd = linha.querySelector(".quantidade_ampliacao");
    const val = linha.querySelector(".valor_unitario_ampliacao");

    if (qtd && val) {
      const q = parseFloat(qtd.value) || 0;
      const v = parseFloat(val.value) || 0;
      total += q * v;
    }
  });

  document.getElementById("total-geral-ampliacao").textContent = total.toFixed(2);
}
