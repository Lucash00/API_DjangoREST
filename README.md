API Django REST
Este es un proyecto de API desarrollado utilizando Django y Django REST Framework. Proporciona una interfaz para interactuar con una base de datos a través de endpoints RESTful.

Requisitos
Python 3.x
Django
Django REST Framework
Instalación
Clona este repositorio en tu máquina local.

Instala las dependencias del proyecto utilizando el siguiente comando:

bash
Copiar código
pip install -r requirements.txt
Ejecuta las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate
Inicia el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Uso
Puedes acceder a la API a través de los siguientes endpoints:

Documentación con Redoc
Documentación con Swagger
Obtener token de autenticación
Listar todos los roles
Listar todos los usuarios
Listar todos los productos
Listar todas las ventas
Listar todos los pedidos
Listar todo el inventario
Listar todos los chats
Listar todos los mensajes
Listar todas las notificaciones
Puedes usar estas URL directamente en tu navegador o con herramientas como Postman para realizar peticiones HTTP.

Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

Realiza un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -am 'Agrega una nueva característica').
Sube tus cambios a tu repositorio remoto (fork) (git push origin feature/nueva-caracteristica).
Abre un Pull Request.