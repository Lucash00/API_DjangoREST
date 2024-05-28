from django.urls import reverse
from django.shortcuts import render
from rest_framework import viewsets, pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from rest_framework.decorators import action
from django.template.loader import render_to_string

# Generar viewsets automáticamente para todos los modelos con filtrado dinámico
class DynamicFilterViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        queryset = self.queryset
        filter_params = self.request.query_params.dict()

        # Eliminar parámetros especiales que no son campos del modelo
        special_params = ['page', 'page_size', 'ordering']
        for param in special_params:
            filter_params.pop(param, None)

        # Aplicar filtros dinámicos a la consulta
        if filter_params:
            queryset = queryset.filter(**filter_params)

        return queryset

# Generar viewsets automáticamente para todos los modelos
for model, serializer in [(Rol, RolSerializer), (Usuario, UsuarioSerializer), 
                          (Producto, ProductoSerializer), (Venta, VentaSerializer), 
                          (Pedido, PedidoSerializer), (Inventario, InventarioSerializer), 
                          (Chat, ChatSerializer), (Mensaje, MensajeSerializer), 
                          (Notificacion, NotificacionSerializer)]:
    viewset_name = f'{model._meta.db_table.capitalize()}ViewSet'
    viewset_class = type(viewset_name, (DynamicFilterViewSet,), {
        'queryset': model.objects.all(),
        'serializer_class': serializer,
    })

    # Asignar el viewset generado a una variable global
    globals()[viewset_name] = viewset_class


def inicio(request):
    # Renderiza tu propia plantilla 'inicio.html'
    return render(request, 'inicio.html')

# Vista para mostrar todos los endpoints
def endpoints(request):
    # Obtener los nombres de las tablas de los modelos
    table_names = [model._meta.verbose_name_plural.capitalize() for model in [Rol, Usuario, Producto, Venta, Pedido, Inventario, Chat, Mensaje, Notificacion]]

    # Obtener los enlaces de los métodos CRUD para cada modelo
    table_endpoints = {}
    for model in [Rol, Usuario, Producto, Venta, Pedido, Inventario, Chat, Mensaje, Notificacion]:
        viewset_name = f'{model._meta.db_table.capitalize()}ViewSet'
        viewset = globals()[viewset_name]

        # Obtener todos los métodos permitidos en el viewset
        methods = [method.lower() for method in viewset.http_method_names if method.lower() != 'options']

        # Construir los enlaces para cada método
        endpoints = {}
        for method in methods:
            # Para los métodos GET, permitir filtros adicionales
            if method == 'get':
                endpoint_url = reverse(f'{model._meta.db_table.lower()}-list')
                # Agregar parámetros de filtro a la URL
                endpoint_url += '?'
                # Ejemplo de filtro: ?nombre=valor
                endpoint_url += '&'.join([f'{param}={value}' for param, value in request.GET.items()])
            else:
                # Para otros métodos, simplemente usar la URL base
                endpoint_url = reverse(f'{model._meta.db_table.lower()}-list')

            endpoints[method.upper()] = endpoint_url

        table_endpoints[model._meta.verbose_name_plural.capitalize()] = endpoints

    # Renderizar la plantilla 'endpoints.html' con los enlaces generados
    return render(request, 'endpoints.html', {'table_endpoints': table_endpoints})



# Define la vista para la autenticación y generación de tokens
@api_view(['POST'])
def obtener_token(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Autenticar al usuario
        user = authenticate(username=username, password=password)

        if user:
            # Si el usuario existe, generar un token y devolverlo en la respuesta
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Si la autenticación falla, devolver un mensaje de error
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # Si el método de solicitud no es POST, devolver un mensaje de error
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

