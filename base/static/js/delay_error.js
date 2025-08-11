setTimeout(function() {
    var messageBox = document.querySelector(".messages");
    if (messageBox) {
        messageBox.style.opacity = "0";
        setTimeout(() => messageBox.remove(), 500);
    }
}, 3000);