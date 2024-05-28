// contenido.js

function mostrarContenido(id) {
    // Oculta todos los contenidos de la derecha
    var contenidoDerecha = document.getElementById("contenido-derecha");
    contenidoDerecha.innerHTML = ""; // Limpiar el contenido actual

    // Genera y muestra el contenido correspondiente al ID recibido
    var contenido;
    if (id === 'contenido1') {
        contenido = '<p>Contenido de la Sección 1</p>';
    } else if (id === 'contenido2') {
        contenido = '<p>Contenido de la Sección 2</p>';
    }
    contenidoDerecha.innerHTML = contenido;
}
