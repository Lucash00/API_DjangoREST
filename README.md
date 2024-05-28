# API Django REST

Este es un proyecto de API desarrollado utilizando Django y Django REST Framework. Proporciona una interfaz para interactuar con una base de datos a través de endpoints RESTful.

## Requisitos

- Python 3.x
- Django
- Django REST Framework

## Instalación

1. Clona este repositorio en tu máquina local.

2. Instala las dependencias del proyecto utilizando el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

4. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

Puedes acceder a la API a través de los siguientes endpoints:

- **Documentación con Redoc**: [URL de Redoc]
- **Documentación con Swagger**: [URL de Swagger]
- **Obtener token de autenticación**: `/api/token/`
- **Listar todos los roles**: `/api/roles/`
- **Listar todos los usuarios**: `/api/users/`
- **Listar todos los productos**: `/api/products/`
- **Listar todas las ventas**: `/api/sales/`
- **Listar todos los pedidos**: `/api/orders/`
- **Listar todo el inventario**: `/api/inventory/`
- **Listar todos los chats**: `/api/chats/`
- **Listar todos los mensajes**: `/api/messages/`
- **Listar todas las notificaciones**: `/api/notifications/`

Puedes usar estas URL directamente en tu navegador o con herramientas como Postman para realizar peticiones HTTP.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes consultar el archivo `LICENSE.txt` para más detalles.
