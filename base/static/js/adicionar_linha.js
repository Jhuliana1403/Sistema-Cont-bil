function adicionarLinha() {
  const tabela = document.getElementById("tabela-investimentos");
  const linha = document.createElement("tr");

  linha.innerHTML = `
    <td><input type="date" class="form-control" name="data[]" required></td>
    <td><input type="text" class="form-control" name="descricao[]" required></td>
    <td><input type="number" class="form-control quantidade" name="quantidade[]" min="0" value="0" required></td>
    <td><input type="number" class="form-control valor_unitario" name="valor_unitario[]" min="0" step="0.01" value="0.00" required></td>
    <td><input type="number" class="form-control" name="depreciacao[]" min="0" step="0.01" value="0" required></td>
    <td><input type="number" class="form-control" name="credito[]" min="0" step="0.01" value="0" required></td>
    <td>
      <button type="button" class="btn btn-outline-danger btn-sm" onclick="removerLinha(this)"><i class="bi bi-trash-fill"></i></button>
    </td>
  `;

  tabela.appendChild(linha);
  atualizarEventosInputs(linha); 
  atualizarTotal();
}

function removerLinha(botao) {
  const linha = botao.closest("tr");
  linha.remove();
  atualizarTotal();
}

function atualizarEventosInputs(linha) {
  const qtdInput = linha.querySelector(".quantidade");
  const valInput = linha.querySelector(".valor_unitario");

  qtdInput.addEventListener("input", atualizarTotal);
  valInput.addEventListener("input", atualizarTotal);
}

function atualizarTotal() {
  let total = 0;
  const linhas = document.querySelectorAll("#tabela-investimentos tr");

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
