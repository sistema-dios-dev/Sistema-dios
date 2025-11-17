import os
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

def main():
    if not TELEGRAM_TOKEN:
        print('❌ ERROR: No hay token de Telegram')
        return
        
    try:
        application = Application.builder().token(TELEGRAM_TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("status", status))
        
        print('🚀 Iniciando bot...')
        application.run_polling()
        
    except Exception as e:
        print(f'❌ Error: {e}')

if __name__ == "__main__":
    main()
