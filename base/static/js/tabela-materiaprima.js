document.addEventListener('DOMContentLoaded', function () {
  const btnAddColuna = document.getElementById('btn-adicionar-coluna');
  const btnAddProduto = document.getElementById('btn-adicionar-produto');
  const tabela = document.getElementById('tabela-investimentos');
  const theadTr = tabela.querySelector('thead tr');
  const tbody = tabela.querySelector('tbody');

  // IDs fixos para categorias iniciais
  let categorias = ['materia_prima', 'frete', 'embalagem'];
  let titulosCategorias = {
    materia_prima: 'Matéria-prima e outros custos',
    frete: 'Frete (R$)',
    embalagem: 'Embalagem'
  };

  // Adicionar nova categoria (nova linha)
  btnAddColuna.addEventListener('click', function () {
    const titulo = document.getElementById('input-novo-titulo-coluna').value.trim();
    if (!titulo) {
      alert('Informe o nome da nova categoria!');
      return;
    }

    // Gerar id único para categoria (lowercase, underscore, remove caracteres especiais)
    let baseId = titulo.toLowerCase().replace(/\s+/g, '_').replace(/[^\w_]/g, '');
    let novoId = baseId;
    let i = 1;
    while (categorias.includes(novoId)) {
      novoId = baseId + '_' + i;
      i++;
    }
    categorias.push(novoId);
    titulosCategorias[novoId] = titulo;

    // Criar nova linha na tbody
    const tr = document.createElement('tr');
    tr.innerHTML = `<th>${titulo}</th>`;

    // Quantidade de produtos atuais (colunas - 1 porque a primeira coluna é o título)
    const numProdutos = theadTr.children.length - 1;

    for (let j = 0; j < numProdutos; j++) {
      // Aqui cria input do tipo texto para as categorias adicionais
      tr.innerHTML += `<td><input type="text" name="${novoId}_${j + 1}" class="form-control"></td>`;
    }

    // Adicionar a linha na tabela
    tbody.appendChild(tr);

    // Limpar input
    document.getElementById('input-novo-titulo-coluna').value = '';
  });

  // Adicionar novo produto (nova coluna)
  btnAddProduto.addEventListener('click', function () {
    const inputNomeProduto = document.getElementById('input-nome-novo-produto');
    const nomeProduto = inputNomeProduto.value.trim();

    if (!nomeProduto) {
      alert('Informe o nome do novo produto!');
      inputNomeProduto.focus();
      return;
    }

    // Verificar se produto já existe no header para evitar duplicação
    const produtosExistentes = Array.from(theadTr.children).map(th => th.textContent.toLowerCase());
    if (produtosExistentes.includes(nomeProduto.toLowerCase())) {
      alert('Produto já existe na tabela!');
      inputNomeProduto.focus();
      return;
    }

    const numProdutos = theadTr.children.length - 1;
    const novoProdutoNumero = numProdutos + 1;

    // Criar novo th com nome informado
    const th = document.createElement('th');
    th.textContent = nomeProduto;
    theadTr.appendChild(th);

    // Para cada linha da tbody adicionar uma nova td com input
    tbody.querySelectorAll('tr').forEach((tr, index) => {
      const nomeCategoria = categorias[index] || `categoria_${index}`;
      const tipoInput = (nomeCategoria === 'frete') ? 'number' : 'text';

      const td = document.createElement('td');
      td.innerHTML = `<input type="${tipoInput}" step="0.01" name="${nomeCategoria}_${novoProdutoNumero}" class="form-control">`;
      tr.appendChild(td);
    });

    // Limpar e focar input
    inputNomeProduto.value = '';
    inputNomeProduto.focus();
  });
});
