  const form = document.querySelector('form');
  const editor = document.getElementById('editor-caracteristica');
  const textarea = document.getElementById('texto');

  form.addEventListener('submit', function() {
    textarea.value = editor.innerHTML.trim();
  });