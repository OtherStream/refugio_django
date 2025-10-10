document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formLogin");
    const usuarioInput = document.getElementById("usuario");
    const passInput = document.getElementById("password");

    const errorUsuario = document.getElementById("errorUsuario");
    const errorPassword = document.getElementById("errorPassword");

    // Validación en tiempo real usuario
    usuarioInput.addEventListener("input", function () {
        let usuarioValue = usuarioInput.value.trim();

        if (usuarioValue === "") {
            errorUsuario.innerText = "El usuario es obligatorio.";
            usuarioInput.classList.add("is-invalid");
        } else {
            errorUsuario.innerText = "";
            usuarioInput.classList.remove("is-invalid");
        }
    });

    // Validación en tiempo real contraseña
    passInput.addEventListener("input", function () {
        let passValue = passInput.value.trim();

        if (passValue.length < 4 && passValue.length > 0) {
            errorPassword.innerText = "La contraseña debe tener al menos 4 caracteres.";
            passInput.classList.add("is-invalid");
        } else {
            errorPassword.innerText = "";
            passInput.classList.remove("is-invalid");
        }
    });

    // Validación 
    form.addEventListener("submit", function (event) {
        let isValid = true;

        // usuario
        let usuarioValue = usuarioInput.value.trim();
        if (usuarioValue === "") {
            errorUsuario.innerText = "El usuario es obligatorio.";
            usuarioInput.classList.add("is-invalid");
            isValid = false;
        } else {
            errorUsuario.innerText = "";
            usuarioInput.classList.remove("is-invalid");
        }

        // contraseña
        let passValue = passInput.value.trim();
        if (passValue.length < 4) {
            errorPassword.innerText = "La contraseña debe tener al menos 4 caracteres.";
            passInput.classList.add("is-invalid");
            isValid = false;
        } else {
            errorPassword.innerText = "";
            passInput.classList.remove("is-invalid");
        }
        if (!isValid) {
            event.preventDefault();
        }
    });

    // Mostrar el modal 
    const params = new URLSearchParams(window.location.search);
    if (params.has("error")) {
        const modal = new bootstrap.Modal(document.getElementById("modalError"));
        modal.show();
    }
    document.addEventListener('hidden.bs.modal', function () {
        document.body.classList.remove('modal-open');
        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
    });
});