document.addEventListener('DOMContentLoaded', function () {
    const tipoSelect = document.querySelector('select[name="tipo_de_produto"]');
    const margemContainer = document.getElementById('margem-lucro-container');

    function verificarTipo() {
      const valor = tipoSelect.value;
      if (valor === 'Produto de Terceiros') {
        margemContainer.style.display = 'block';
      } else {
        margemContainer.style.display = 'none';
      }
    }

    tipoSelect.addEventListener('change', verificarTipo);
    verificarTipo(); 
  });