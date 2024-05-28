from django.contrib import admin
from .models import *

# Define una función para generar las clases ModelAdmin
def generate_admin(model):
    class Meta:
        model = model
        fields = '__all__'

    class_name = f"{model.__name__}Admin"
    attrs = {'Meta': Meta}
    return type(class_name, (admin.ModelAdmin,), attrs)

# Registrar automáticamente todas las clases ModelAdmin generadas
for model in [Usuario, Producto, Venta, Pedido, Inventario, Rol]:
    admin_class = generate_admin(model)
    admin.site.register(model, admin_class)
