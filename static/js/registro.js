document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formRegistro");

const nombreInput = document.getElementById("id_first_name");
const apellidosInput = document.getElementById("id_last_name");
const telefonoInput = document.getElementById("id_telefono");
const direccionInput = document.getElementById("id_direccion");
const edadInput = document.getElementById("id_edad");
const sexoInput = document.getElementById("id_sexo");
const usuarioInput = document.getElementById("id_username");
const passInput = document.getElementById("id_password");

    const errorNombre = document.getElementById("errorNombre");
    const errorApellidos = document.getElementById("errorApellidos");
    const errorTipoUsuario = document.getElementById("errorTipoUsuario");
    const errorTelefono = document.getElementById("errorTelefono");
    const errorDireccion = document.getElementById("errorDireccion");
    const errorEdad = document.getElementById("errorEdad");
    const errorSexo = document.getElementById("errorSexo");
    const errorUsuario = document.getElementById("errorUsuario");
    const errorPass = document.getElementById("errorPass");

    // Validación en tiempo real
    nombreInput.addEventListener("input", function () {
        let val = nombreInput.value.trim();
        if (val.length < 3) {
            errorNombre.innerText = "El nombre debe tener al menos 3 caracteres.";
            nombreInput.classList.add("is-invalid");
        } else {
            errorNombre.innerText = "";
            nombreInput.classList.remove("is-invalid");
        }
    });

    apellidosInput.addEventListener("input", function () {
        let val = apellidosInput.value.trim();
        if (val.length < 3) {
            errorApellidos.innerText = "Los apellidos deben tener al menos 3 caracteres.";
            apellidosInput.classList.add("is-invalid");
        } else {
            errorApellidos.innerText = "";
            apellidosInput.classList.remove("is-invalid");
        }
    });

    telefonoInput.addEventListener("input", function () {
        let val = telefonoInput.value.trim();
        if (!/^\d{10}$/.test(val)) {
            errorTelefono.innerText = "El teléfono debe tener 10 dígitos.";
            telefonoInput.classList.add("is-invalid");
        } else {
            errorTelefono.innerText = "";
            telefonoInput.classList.remove("is-invalid");
        }
    });

    direccionInput.addEventListener("input", function () {
        let val = direccionInput.value.trim();
        if (val.length < 5) {
            errorDireccion.innerText = "La dirección debe tener al menos 5 caracteres.";
            direccionInput.classList.add("is-invalid");
        } else {
            errorDireccion.innerText = "";
            direccionInput.classList.remove("is-invalid");
        }
    });

    edadInput.addEventListener("input", function () {
        let val = parseInt(edadInput.value);
        if (isNaN(val) || val < 15 || val > 90) {
            errorEdad.innerText = "Edad debe ser entre 15 y 90.";
            edadInput.classList.add("is-invalid");
        } else {
            errorEdad.innerText = "";
            edadInput.classList.remove("is-invalid");
        }
    });
    sexoInput.addEventListener("change", function () {
        if (sexoInput.value === "") {
            errorSexo.innerText = "Selecciona un sexo.";
            sexoInput.classList.add("is-invalid");
        } else {
            errorSexo.innerText = "";
            sexoInput.classList.remove("is-invalid");
        }
    });
    usuarioInput.addEventListener("input", function () {
        let val = usuarioInput.value.trim();
        if (val.length < 4 || !/^[a-zA-Z0-9_]+$/.test(val)) {
            errorUsuario.innerText = "El usuario debe tener al menos 4 caracteres y solo contener letras, números o guiones bajos.";
            usuarioInput.classList.add("is-invalid");
        } else {
            errorUsuario.innerText = "";
            usuarioInput.classList.remove("is-invalid");
        } 
    });

    passInput.addEventListener("input", function () {
        let val = passInput.value.trim();
        if (val.length < 4) {
            errorPass.innerText = "La contraseña debe tener al menos 4 caracteres.";
            passInput.classList.add("is-invalid");
        } else {
            errorPass.innerText = "";
            passInput.classList.remove("is-invalid");
        }
    });
    if (tipoUsuarioInput) { 
        tipoUsuarioInput.addEventListener("change", function () {
            if (tipoUsuarioInput.value === "") {
                errorTipoUsuario.innerText = "Debes seleccionar un tipo de usuario.";
                tipoUsuarioInput.classList.add("is-invalid");
            } else {
                errorTipoUsuario.innerText = "";
                tipoUsuarioInput.classList.remove("is-invalid");
            }
        });
    }


    // Validación
    form.addEventListener("submit", function (event) {
        let isValid = true;

        // Nombre
        if (nombreInput.value.trim().length < 3) {
            errorNombre.innerText = "El nombre es obligatorio y debe tener mínimo 3 caracteres.";
            nombreInput.classList.add("is-invalid");
            isValid = false;
        }

        // Apellidos
        if (apellidosInput.value.trim().length < 3) {
            errorApellidos.innerText = "Los apellidos son obligatorios.";
            apellidosInput.classList.add("is-invalid");
            isValid = false;
        }

        // Tipo de usuario
        if (rolInput.value === "") {
            errorRol.innerText = "Debes seleccionar un tipo de usuario.";
            rolInput.classList.add("is-invalid");
            isValid = false;
        }

        // Teléfono
        if (!/^\d{10}$/.test(telefonoInput.value.trim())) {
            errorTelefono.innerText = "Teléfono inválido.";
            telefonoInput.classList.add("is-invalid");
            isValid = false;
        }

        // Dirección
        if (direccionInput.value.trim().length < 5) {
            errorDireccion.innerText = "La dirección debe tener al menos 5 caracteres.";
            direccionInput.classList.add("is-invalid");
            isValid = false;
        }

        // Edad
        const edadVal = parseInt(edadInput.value);
        if (isNaN(edadVal) || edadVal < 1 || edadVal > 90) {
            errorEdad.innerText = "Edad fuera de rango.";
            edadInput.classList.add("is-invalid");
            isValid = false;
        }

        // Sexo
        if (sexoInput.value === "") {
            errorSexo.innerText = "Selecciona un sexo.";
            sexoInput.classList.add("is-invalid");
            isValid = false;
        }

        // Usuario
        if (usuarioInput.value.trim().length < 4 || !/^[a-zA-Z0-9_]+$/.test(usuarioInput.value.trim())) {
            errorUsuario.innerText = "El usuario debe tener al menos 4 caracteres y solo contener letras, números o guiones bajos.";
            usuarioInput.classList.add("is-invalid");
            isValid = false;
        }

        // Contraseña
        if (passInput.value.trim().length < 4) {
            errorPass.innerText = "La contraseña debe tener al menos 4 caracteres.";
            passInput.classList.add("is-invalid");
            isValid = false;
        }

        // Tipo de usuario 
        if (tipoUsuarioInput && tipoUsuarioInput.value === "") {
            errorTipoUsuario.innerText = "Debes seleccionar un tipo de usuario.";
            tipoUsuarioInput.classList.add("is-invalid");
            isValid = false;
        }


        if (!isValid) {
            event.preventDefault();
        }
    });
});
