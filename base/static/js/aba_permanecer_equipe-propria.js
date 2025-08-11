    function mostrarAba(idAba, btn) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('d-none'));
      document.getElementById(idAba).classList.remove('d-none');

      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('tab-btn-active'));
      btn.classList.add('tab-btn-active');
    }