from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = DefaultRouter()

# Registrar todos los viewsets generados automáticamente
for model in [Rol, Usuario, Producto, Venta, Pedido, Inventario, Chat, Mensaje, Notificacion]:
    viewset_name = f'{model._meta.db_table.capitalize()}ViewSet'
    basename = model._meta.db_table.lower()  # Definir el basename para el viewset
    router.register(prefix=model._meta.db_table, viewset=globals()[viewset_name], basename=model._meta.db_table.lower())

urlpatterns = [
    *router.urls,
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
