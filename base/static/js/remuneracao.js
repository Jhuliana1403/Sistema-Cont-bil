// Define o contador iniciando no número de linhas já existentes + 1
let contador = 1; // valor inicial será atualizado pelo template via dataset

function adicionarLinha() {
  const tabela = document.querySelector("#tabela-socios tbody");
  const novaLinha = document.createElement("tr");
  novaLinha.innerHTML = `
    <td>
      <input type="text" name="socio_${contador}" class="form-control form-control-sm" placeholder="Digite o nome do sócio">
    </td>
    <td>
      <div class="input-group input-group-sm">
        <span class="input-group-text">R$</span>
        <input type="text" name="valor_${contador}" class="form-control text-end" placeholder="0,00">
      </div>
    </td>
    <td>
      <button type="button" class="btn btn-outline-danger btn-sm" onclick="removerLinha(this)">
        <i class="bi bi-trash-fill"></i>
      </button>
    </td>
  `;
  tabela.appendChild(novaLinha);
  contador++;
}

function removerLinha(botao) {
  const linha = botao.closest("tr");
  linha.remove();
}

// Atualiza contador com valor inicial vindo do template
document.addEventListener("DOMContentLoaded", function () {
  const tabela = document.querySelector("#tabela-socios");
  if (tabela) {
    const linhasExistentes = tabela.querySelectorAll("tbody tr").length;
    contador = linhasExistentes + 1;
  }
});
