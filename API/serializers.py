from rest_framework import serializers
from .models import Usuario, Producto, Venta, Pedido, Inventario, Rol, ApiKey, Chat, Mensaje, Notificacion


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


# Define una función para generar los Serializers
def generate_serializer_all(model_class):
    class Meta:
        model = model_class
        fields = '__all__'

    class_name = f"{model_class.__name__}Serializer"
    return type(class_name, (CustomSerializer,), {'Meta': Meta})


# Crea los Serializers utilizando la función generate_serializer_all
RolSerializer = generate_serializer_all(Rol)
UsuarioSerializer = generate_serializer_all(Usuario)
ProductoSerializer = generate_serializer_all(Producto)
VentaSerializer = generate_serializer_all(Venta)
PedidoSerializer = generate_serializer_all(Pedido)
InventarioSerializer = generate_serializer_all(Inventario)
ApiKeySerializer = generate_serializer_all(ApiKey)
ChatSerializer = generate_serializer_all(Chat)
MensajeSerializer = generate_serializer_all(Mensaje)
NotificacionSerializer = generate_serializer_all(Notificacion)
