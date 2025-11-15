import discord
import asyncio
import os
from config import BOT_TOKEN, DEBUG

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'✅ Bot conectado como {self.user}')
        print(f'🆔 ID: {self.user.id}')
        print('🚀 Bot funcionando en la nube! ☁️')
        
        # Cambiar estado del bot
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="en la nube ☁️"
            )
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('!hola'):
            await message.channel.send(f'¡Hola {message.author.mention}! 🤖 Funciono en la nube! ☁️')

async def main():
    print('🌐 Iniciando bot en modo producción...')
    
    # Para la nube, necesitamos usar el token de las variables de entorno
    token = os.getenv('BOT_TOKEN', BOT_TOKEN)
    
    if not token or token == 'tu_token_aqui':
        print('❌ ERROR: No hay token configurado')
        print('💡 Ve a Railway → Variables → Agrega BOT_TOKEN')
        return
    
    bot = MyBot()
    try:
        await bot.start(token)
    except Exception as e:
        print(f'❌ Error: {e}')

if _name_ == "_main_":
    asyncio.run(main())