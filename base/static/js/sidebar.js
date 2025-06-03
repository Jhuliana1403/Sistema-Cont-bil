document.addEventListener('DOMContentLoaded', function () {
  const sidebarItems = document.querySelectorAll('.sidebar-item');

  // Função para salvar no localStorage o índice ativo, ou null
  function saveActiveIndex(index) {
    if (index === null) {
      localStorage.removeItem('sidebarActiveIndex');
    } else {
      localStorage.setItem('sidebarActiveIndex', index);
    }
  }

  // Ao carregar, verifica se tem índice salvo e abre o item
  const savedIndex = localStorage.getItem('sidebarActiveIndex');
  if (savedIndex !== null && sidebarItems[savedIndex]) {
    sidebarItems[savedIndex].classList.add('active');
  }

  sidebarItems.forEach((item, index) => {
    const title = item.querySelector('.sidebar-item-title');

    if (title) {
      title.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        if (isActive) {
          // Se já está ativo, fecha e remove o registro
          item.classList.remove('active');
          saveActiveIndex(null);
        } else {
          // Fecha todos os outros e abre o atual
          sidebarItems.forEach(i => i.classList.remove('active'));
          item.classList.add('active');
          saveActiveIndex(index);
        }
      });
    }
  });
});
