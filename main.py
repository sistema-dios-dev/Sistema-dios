import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Token de Telegram desde variables de entorno
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    await update.message.reply_text(
        '🚀 **Sistema Dios Bot Activado**\n\n'
        '✅ Bot configurado correctamente\n'
        '🔧 Modo: DEMO\n'
        '📊 Risk: 5%\n\n'
        'Usa /status para ver el estado del sistema'
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /status"""
    await update.message.reply_text(
        '📊 **Estado del Sistema:**\n'
        '✅ Bot: ACTIVO\n'
        '🔧 Modo: DEMO\n'
        '⚡ Risk: 5%\n'
        '🔍 Debug: ACTIVADO\n\n'
        '🚀 Sistema listo para operar!'
    )

async def main():
    """Función principal"""
    if not TELEGRAM_TOKEN or TELEGRAM_TOKEN == 'tu_token_real_aqui':
        print('❌ ERROR: No hay token de Telegram configurado')
        return

    # Crear aplicación de Telegram
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Registrar comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    # Iniciar bot
    print('🚀 Iniciando Sistema Dios Bot...')
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
