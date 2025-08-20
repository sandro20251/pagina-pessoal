document.addEventListener('DOMContentLoaded', function () {
    let editBtns = document.querySelectorAll('.editBtn'); // pega todos os botões
    let parte13 = document.querySelector('#parte13');     // formulário alvo

    editBtns.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            // alterna entre mostrar e ocultar
            parte13.classList.toggle('hide');
        });
    });
});