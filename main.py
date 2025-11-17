import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🚀 Sistema Dios Bot - ACTIVO')

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('✅ Bot funcionando correctamente')

async def main():
    if not TELEGRAM_TOKEN:
        print('❌ ERROR: No hay token de Telegram')
        return
        
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    print('🚀 Iniciando bot...')
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
