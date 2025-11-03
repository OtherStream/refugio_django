// static/js/solicitud.js

// Función para obtener el token CSRF de la cookie de Django
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 10) === ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCSRFToken();


document.addEventListener('DOMContentLoaded', function () {
    const animalModal = document.getElementById('animalModal');
    const enviarSolicitudBtn = document.getElementById('enviar-solicitud');
    const mensajeResultado = document.getElementById('mensaje-resultado');
    const mensajeAdopcion = document.getElementById('mensaje-adopcion');
    
    let currentAnimalId = null;

    // 1. Escuchamos cuando el modal se está abriendo
    animalModal.addEventListener('show.bs.modal', function (event) {
        // 'event.relatedTarget' es el botón "Adoptar" que se presionó
        const button = event.relatedTarget;
        
        // 2. Obtenemos los datos del botón
        currentAnimalId = button.getAttribute('data-id');
        const animalNombre = button.getAttribute('data-nombre');

        // 3. Actualizamos el texto del modal
        mensajeAdopcion.innerHTML = `Se está haciendo una solicitud por <strong>${animalNombre}</strong>.`;
        
        // 4. Reseteamos el estado del modal
        mensajeResultado.style.display = 'none';
        mensajeResultado.textContent = '';
        enviarSolicitudBtn.disabled = false;
    });

    // 5. Escuchamos el clic en el botón "Enviar solicitud" DENTRO del modal
    enviarSolicitudBtn.addEventListener('click', async function () {
        
        if (!currentAnimalId) {
            mensajeResultado.textContent = 'Error: No se encontró el ID del animal.';
            mensajeResultado.style.display = 'block';
            return;
        }

        // Deshabilitamos el botón para evitar clics dobles
        enviarSolicitudBtn.disabled = true;

        try {
            // 6. Usamos fetch (con async/await) para llamar a la API de Django
            const response = await fetch('/adopciones/solicitud/crear/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken // ¡Token CSRF es OBLIGATORIO!
                },
                body: JSON.stringify({
                    'animal_id': currentAnimalId
                })
            });

            const data = await response.json();

            // 7. Mostramos la respuesta (exitosa o no) de Django
            mensajeResultado.textContent = data.message;
            if (data.success) {
                mensajeResultado.className = 'mt-3 text-center text-success';
            } else {
                mensajeResultado.className = 'mt-3 text-center text-danger';
                enviarSolicitudBtn.disabled = false; // Reactivamos si falló
            }
            mensajeResultado.style.display = 'block';

        } catch (error) {
            console.error('Error en fetch:', error);
            mensajeResultado.textContent = 'Error de conexión. Inténtalo de nuevo.';
            mensajeResultado.className = 'mt-3 text-center text-danger';
            mensajeResultado.style.display = 'block';
            enviarSolicitudBtn.disabled = false;
        }
    });
});