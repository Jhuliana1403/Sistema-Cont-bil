  document.addEventListener('DOMContentLoaded', function () {
    const sidebarItems = document.querySelectorAll('.sidebar-item');

    // Restaurar estado salvo
    const saved = JSON.parse(localStorage.getItem('openSidebarItems') || '[]');
    saved.forEach(index => {
      if (sidebarItems[index]) {
        sidebarItems[index].classList.add('active');
      }
    });

    // Adicionar eventos de clique
    sidebarItems.forEach((item, index) => {
      const title = item.querySelector('.sidebar-item-title');
      if (title) {
        title.addEventListener('click', function () {
          item.classList.toggle('active');
          saveSidebarState();
        });
      }
    });

    // Salvar estado
    function saveSidebarState() {
      const openItems = [];
      sidebarItems.forEach((item, index) => {
        if (item.classList.contains('active')) {
          openItems.push(index);
        }
      });
      localStorage.setItem('openSidebarItems', JSON.stringify(openItems));
    }
  });