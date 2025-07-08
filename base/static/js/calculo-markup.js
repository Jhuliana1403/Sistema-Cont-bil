document.addEventListener("DOMContentLoaded", function () {
  const precoVendaInput = document.getElementById("precoVenda");
  const precoCompraInput = document.getElementById("precoCompra");
  const markupInput = document.getElementById("markup");

  function calcularMarkup() {
    const precoVenda = parseFloat(precoVendaInput.value.replace(",", ".")) || 0;
    const precoCompra = parseFloat(precoCompraInput.value.replace(",", ".")) || 0;

    if (precoCompra > 0) {
      const markup = ((precoVenda - precoCompra) / precoCompra) * 100;
      markupInput.value = markup.toFixed(2);
    } else {
      markupInput.value = "";
    }
  }

  precoVendaInput.addEventListener("input", calcularMarkup);
  precoCompraInput.addEventListener("input", calcularMarkup);
});
