from django.db import models

class ApiKey(models.Model):
    user = models.OneToOneField('Usuario', on_delete=models.CASCADE)
    key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"API Key para {self.user.nombre}"

    class Meta:
        db_table = 'api_keys'


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=5)
    es_proveedor = models.BooleanField(default=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    token_autenticacion = models.CharField(max_length=36)
    fecha_creacion = models.DateTimeField()
    ultima_actividad = models.DateTimeField()
    activo = models.BooleanField(default=True)
    avatar = models.CharField(max_length=500)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuarios'


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    proveedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=5000)
    destacado = models.BooleanField(default=False)
    disponible = models.BooleanField(default=True)
    sku = models.CharField(max_length=36)
    marca = models.CharField(max_length=100)
    valoraciones = models.FloatField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'


class Venta(models.Model):
    venta_id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField()
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=100)
    direccion_facturacion = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ventas'


class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    estado = models.CharField(max_length=20)
    direccion_envio = models.CharField(max_length=200)
    fecha_entrega_esperada = models.DateTimeField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pedidos'


class Inventario(models.Model):
    inventario_id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)
    fecha_llegada = models.DateTimeField()
    estado_producto = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'inventario'


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'chats'


class Mensaje(models.Model):
    mensaje_id = models.AutoField(primary_key=True)
    texto = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje {self.id} enviado por {self.usuario.nombre}"

    class Meta:
        db_table = 'mensajes'


class ComentarioProducto(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField()
    me_gusta = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comentario {self.comentario_id} en {self.producto.nombre}"

    class Meta:
        db_table = 'comentarios_productos'


class Notificacion(models.Model):
    notificacion_id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)

    def __str__(self):
        return f"Notificación {self.notificacion_id} para {self.usuario.nombre}"

    class Meta:
        db_table = 'notificaciones'


class Resena(models.Model):
    resena_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='resenas_hechas', on_delete=models.CASCADE)
    asesor_o_proveedor = models.ForeignKey(Usuario, related_name='resenas_recibidas', on_delete=models.CASCADE)
    texto = models.TextField()
    puntuacion = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return f"Reseña {self.resena_id} de {self.usuario.nombre} a {self.asesor_o_proveedor.nombre}"

    class Meta:
        db_table = 'resenas'
