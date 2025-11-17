import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('🚀 Sistema Dios Bot - ACTIVO')

def status(update: Update, context: CallbackContext):
    update.message.reply_text('✅ Bot funcionando correctamente')

def main():
    if not TELEGRAM_TOKEN:
        print('❌ ERROR: No hay token de Telegram')
        return
        
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("status", status))
    
    print('🚀 Iniciando bot...')
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
