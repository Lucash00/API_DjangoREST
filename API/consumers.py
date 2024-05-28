import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.authtoken.models import Token
from .models import Usuario, Chat

class TokenAuthConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Lógica de autenticación por token al conectar
        token_key = self.scope['query_string'].decode('utf-8').split('=')[1]
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            # Autenticar al usuario
            self.scope['user'] = user
            await self.accept()
        except Token.DoesNotExist:
            await self.send(text_data=json.dumps({
                'error': 'Autenticación fallida. Token inválido.'
            }))
            await self.close()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        # Unirse a la sala de chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Salir de la sala de chat
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')  # Obtener el mensaje del diccionario

        if message:  # Verificar si el mensaje no está vacío
            # Enviar mensaje a la sala de chat si contiene contenido
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        else:
            # Enviar un mensaje de error al cliente si el mensaje está vacío
            await self.send(text_data=json.dumps({
                'error': 'El mensaje no puede estar vacío.'
            }))

    async def chat_message(self, event):
        message = event['message']
        # Enviar mensaje de vuelta al cliente
        await self.send(text_data=json.dumps({
            'message': message
        }))

class NotificacionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Conectar al grupo de notificaciones
        await self.channel_layer.group_add("notificaciones", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Desconectar del grupo de notificaciones
        await self.channel_layer.group_discard("notificaciones", self.channel_name)

    async def receive(self, text_data):
        # Aquí puedes implementar la lógica para recibir y procesar notificaciones en tiempo real
        pass

    async def enviar_notificacion(self, event):
        # Método para enviar notificaciones a los clientes conectados
        notificacion = event['notificacion']

        # Enviar la notificación al cliente
        await self.send(text_data=json.dumps({
            'notificacion': notificacion
        }))
