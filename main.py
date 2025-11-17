import os
import logging
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app para el puerto web
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Sistema Dios Bot - ACTIVO"

@app.route('/health')
def health():
    return "🟢 Healthy"

# Token de Telegram desde variables de entorno
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    await update.message.reply_text(
        '🚀 **Sistema Dios Bot - ACTIVO**\n\n'
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

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /analyze"""
    await update.message.reply_text(
        '🔍 **Análisis Cuántico Iniciado**\n'
        '📈 Analizando oportunidades...\n'
        '⏳ Esto puede tomar unos segundos'
    )

def run_bot():
    """Ejecutar el bot de Telegram"""
    if not TELEGRAM_TOKEN:
        print('❌ ERROR: No hay token de Telegram')
        return
        
    try:
        application = Application.builder().token(TELEGRAM_TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("status", status))
        application.add_handler(CommandHandler("analyze", analyze))
        
        print('🚀 Iniciando bot de Telegram...')
        application.run_polling()
        
    except Exception as e:
        print(f'❌ Error en el bot: {e}')

def run_flask():
    """Ejecutar servidor Flask para el puerto"""
    port = int(os.environ.get('PORT', 10000))
    print(f'🌐 Iniciando servidor web en puerto {port}')
    app.run(host='0.0.0.0', port=port, debug=False)

def main():
    """Función principal"""
    print('🚀 Iniciando Sistema Dios Bot...')
    
    # Iniciar Flask en hilo separado
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Iniciar bot de Telegram (bloqueante)
    run_bot()

if __name__ == "__main__":
    main()
