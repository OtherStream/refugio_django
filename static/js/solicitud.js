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
    
    const comprobanteInput = document.getElementById('id_comprobante');
    const ineInput = document.getElementById('id_ine');
    
    let currentAnimalId = null;

    animalModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        currentAnimalId = button.getAttribute('data-id');
        const animalNombre = button.getAttribute('data-nombre');

        mensajeAdopcion.innerHTML = `Se está haciendo una solicitud por <strong>${animalNombre}</strong>.`;
        
        mensajeResultado.style.display = 'none';
        mensajeResultado.textContent = '';
        enviarSolicitudBtn.disabled = false;
        comprobanteInput.value = null; 
        ineInput.value = null; 
    });

    enviarSolicitudBtn.addEventListener('click', async function () {
        
        if (!currentAnimalId) {
            mensajeResultado.textContent = 'Error: No se encontró el ID del animal.';
            mensajeResultado.className = 'mt-3 text-center text-danger';
            mensajeResultado.style.display = 'block';
            return;
        }

        const comprobanteFile = comprobanteInput.files[0];
        const ineFile = ineInput.files[0];

        if (!comprobanteFile || !ineFile) {
            mensajeResultado.textContent = 'Por favor, sube ambos archivos (INE y Comprobante).';
            mensajeResultado.className = 'mt-3 text-center text-danger';
            mensajeResultado.style.display = 'block';
            return; 
        }

        enviarSolicitudBtn.disabled = true;

        const formData = new FormData();
        formData.append('animal_id', currentAnimalId); 
        formData.append('comprobante_domicilio', comprobanteFile);
        formData.append('ine', ineFile);
        

        try {
            const response = await fetch('/adopciones/solicitud/crear/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken 
                },
                body: formData 
            });

            const data = await response.json();

            mensajeResultado.textContent = data.message;
            if (data.success) {
                mensajeResultado.className = 'mt-3 text-center text-success';
            } else {
                mensajeResultado.className = 'mt-3 text-center text-danger';
                enviarSolicitudBtn.disabled = false;
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