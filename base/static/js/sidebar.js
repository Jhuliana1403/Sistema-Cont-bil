document.addEventListener('DOMContentLoaded', function () {
  // Pega todos os itens da sidebar
  const sidebarItems = document.querySelectorAll('.sidebar-item');

  // Adiciona um evento de clique em cada item da sidebar
  sidebarItems.forEach(item => {
    const title = item.querySelector('.sidebar-item-title'); // Supondo que o título tenha a classe 'sidebar-item-title'

    // Verifica se o título existe antes de adicionar o evento de clique
    if (title) {
      title.addEventListener('click', function () {
        // Alterna a classe 'active' no item da sidebar
        item.classList.toggle('active');
      });
    }
  });
});
