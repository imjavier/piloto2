// Selecciona el formulario con el ID "uploadForm" y agrega un event listener para el evento "submit"
/*document.getElementById("uploadForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Obtiene el formulario
    var formData = new FormData(this);

    // Crea una nueva instancia de XMLHttpRequest para enviar la solicitud al servidor
    var xhr = new XMLHttpRequest();

    // Configura la solicitud HTTP POST para enviar los datos al servidor en segundo plano
    xhr.open("POST", "/upload", true);

    // Define una función que se ejecutará cuando la solicitud se complete
    xhr.onload = function () {
        // Verifica si la solicitud se completó correctamente (estado HTTP 200)
        if (xhr.status === 200) {
            // Imprime un mensaje en la consola si los archivos se subieron correctamente
            console.log("Archivos subidos exitosamente");
        } else {
            // Imprime un mensaje de error en la consola si ocurrió un error al subir los archivos
            console.error("Error al subir archivos");
        }
    };

    // Envía la solicitud al servidor con los datos del formulario (objetos FormData)
    xhr.send(formData);
});*/

document.getElementById('audioForm').addEventListener('submit', function (event) {
    var modelSelect = document.getElementById('modelSelect');
    var fileInput = document.getElementById('fileInput');

    if (modelSelect.value === '' || fileInput.files.length === 0) {
        event.preventDefault(); // Prevent form submission

        if (modelSelect.value === '') {
            modelSelect.classList.add('is-invalid');
        } else {
            modelSelect.classList.remove('is-invalid');
            modelSelect.classList.add('is-valid');
        }

        if (fileInput.files.length === 0) {
            fileInput.classList.add('is-invalid');
        } else {
            fileInput.classList.remove('is-invalid');
            fileInput.classList.add('is-valid');
        }
    } else {
        modelSelect.classList.remove('is-invalid');
        modelSelect.classList.add('is-valid');
        fileInput.classList.remove('is-invalid');
        fileInput.classList.add('is-valid');
    }
    alert('holaaaaa')
});