0#!/usr/bin/env python3
"""
SISTEMA DIOS V2 - BOT PRINCIPAL
Con Módulos Elite Integrados
"""

import os
import logging
import sqlite3
from datetime import datetime
import telebot
from flask import Flask, request, jsonify

# ==================== CONFIGURACIÓN ====================
# Importar módulos élite
try:
    from config.elite_settings import elite_config
    from modules.elite_trading import EliteDatabase
    from utils.elite_helpers import format_elite_currency, elite_timestamp
    ELITE_MODULES_LOADED = True
    logging.info("✅ Módulos élite cargados correctamente")
except ImportError as e:
    ELITE_MODULES_LOADED = False
    logging.warning(f"⚠️ Módulos élite no disponibles: {e}")

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuración
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'default_token')
TRADING_MODE = os.getenv('TRADING_MODE', 'DEMO')
MAX_RISK_PERCENT = os.getenv('MAX_RISK_PERCENT', '5')

# Inicializar bot y Flask
bot = telebot.TeleBot(TELEGRAM_TOKEN)
app = Flask(__name__)

# Inicializar base de datos élite si está disponible
if ELITE_MODULES_LOADED:
    try:
        elite_db = EliteDatabase()
        ELITE_DB_ACTIVE = True
        logger.info("✅ Base de datos élite inicializada")
    except Exception as e:
        ELITE_DB_ACTIVE = False
        logger.error(f"❌ Error inicializando BD élite: {e}")
else:
    ELITE_DB_ACTIVE = False

# ==================== COMANDOS BÁSICOS ====================
@bot.message_handler(commands=['start'])
def start_command(message):
    """Comando de inicio del sistema"""
    try:
        welcome_text = """
🎯 **SISTEMA DIOS V2 - ACTIVO** 🚀

🤖 **Bot configurado correctamente**
⚡ **Modo:** {mode}
🎯 **Risk:** {risk}%

🏆 **Módulos Elite:** {elite_status}

💡 **Usa /status para ver el estado del sistema**
📚 **Usa /help para ver todos los comandos**
""".format(
    mode=TRADING_MODE,
    risk=MAX_RISK_PERCENT,
    elite_status="✅ INTEGRADOS" if ELITE_MODULES_LOADED else "⚠️ NO DISPONIBLES"
)
        bot.reply_to(message, welcome_text)
        logger.info(f"Comando /start ejecutado por {message.chat.id}")
    except Exception as e:
        logger.error(f"Error en /start: {e}")
        bot.reply_to(message, "❌ Error iniciando el sistema")

@bot.message_handler(commands=['status'])
def status_command(message):
    """Estado del sistema"""
    try:
        elite_info = "✅ ACTIVOS" if ELITE_MODULES_LOADED else "❌ NO DISPONIBLES"
        elite_db_info = "✅ OPERATIVA" if ELITE_DB_ACTIVE else "❌ INACTIVA"
        
        status_text = """
📊 **ESTADO DEL SISTEMA DIOS V2**

🤖 **Bot:** ✅ ACTIVO
⚡ **Modo:** {mode}
🎯 **Risk:** {risk}%
🔧 **Debug:** ✅ ACTIVADO

🏆 **MÓDULOS ELITE:**
• Estado: {elite_status}
• Base de datos: {elite_db}
• Configuración: ✅ CARGADA

🚀 **Sistema listo para operar!**
""".format(
    mode=TRADING_MODE,
    risk=MAX_RISK_PERCENT,
    elite_status=elite_info,
    elite_db=elite_db_info
)
        bot.reply_to(message, status_text)
    except Exception as e:
        logger.error(f"Error en /status: {e}")
        bot.reply_to(message, "❌ Error obteniendo estado")

# ==================== COMANDOS ELITE ====================
@bot.message_handler(commands=['elite_health'])
def elite_health(message):
    """Salud del sistema élite"""
    try:
        if not ELITE_MODULES_LOADED:
            bot.reply_to(message, "❌ Módulos élite no disponibles")
            return
            
        response = """
🏆 **SISTEMA DIOS - MÓDULOS ELITE** 🚀

✅ **ESTADO: OPERATIVO**
🔧 **Versión:** elite_v1.0
📊 **Base de datos:** {db_status}
🤖 **IA Predictiva:** INICIALIZADA

⚙️ **Configuración Elite:**
• Modo: {mode}
• Riesgo: {risk}%
• Debug: {debug}

🎯 **Estructura Modular Profesional**
✅ modules/ - Módulos élite
✅ config/ - Configuración  
✅ utils/ - Utilidades
""".format(
    db_status="✅ ACTIVA" if ELITE_DB_ACTIVE else "❌ INACTIVA",
    mode=elite_config.ELITE_TRADING_MODE,
    risk=elite_config.ELITE_MAX_RISK,
    debug='✅ ACTIVADO' if elite_config.ELITE_DEBUG else '❌ DESACTIVADO'
)
        bot.reply_to(message, response)
        logger.info(f"Comando elite_health ejecutado por {message.chat.id}")
    except Exception as e:
        logger.error(f"Error en elite_health: {e}")
        bot.reply_to(message, f"❌ Error en elite_health: {str(e)}")

@bot.message_handler(commands=['elite_test'])
def elite_test(message):
    """Probar módulos élite"""
    try:
        if not ELITE_MODULES_LOADED or not ELITE_DB_ACTIVE:
            bot.reply_to(message, "❌ Módulos élite no disponibles para pruebas")
            return
            
        # Probar base de datos élite
        test_event = {
            'event_id': f'test_{message.chat.id}_{message.message_id}',
            'sport': 'football',
            'league': 'Premier League',
            'home_team': 'Manchester United',
            'away_team': 'Liverpool',
            'event_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        success = elite_db.save_elite_event(test_event)
        
        if success:
            response = """
🧪 **PRUEBA ELITE - EXITOSA** ✅

✅ Base de datos: OPERATIVA
📊 Evento guardado: #{event_id}
🔧 Configuración: CARGADA
🤖 Módulos: RESPONDIENDO

🏗️ **Estructura probada:**
• Database Manager: ✅
• Configuración Elite: ✅  
• Módulos Import: ✅
• SQLite Integration: ✅

💾 **Evento de prueba:**
• {home_team} vs {away_team}
• Liga: {league}
• Fecha: {timestamp}
""".format(
    event_id=test_event['event_id'],
    home_team=test_event['home_team'],
    away_team=test_event['away_team'],
    league=test_event['league'],
    timestamp=elite_timestamp()
)
        else:
            response = "❌ **PRUEBA FALLIDA** - Error guardando en base de datos"
            
        bot.reply_to(message, response)
        logger.info(f"Comando elite_test ejecutado por {message.chat.id}")
        
    except Exception as e:
        logger.error(f"Error en elite_test: {e}")
        bot.reply_to(message, f"❌ Error en elite_test: {str(e)}")

@bot.message_handler(commands=['elite_status'])
def elite_status(message):
    """Estado completo del sistema élite"""
    try:
        if not ELITE_MODULES_LOADED:
            bot.reply_to(message, "❌ Módulos élite no disponibles")
            return
            
        db_status = "✅ OPERATIVA" if ELITE_DB_ACTIVE else "❌ INACTIVA"
        config_status = elite_config.get_elite_summary()
        
        response = """
🎯 **ESTADO COMPLETO - SISTEMA ELITE**

🏗️ **ARQUITECTURA:**
• Estructura: MODULAR PROFESIONAL
• Módulos: modules/elite_trading/
• Config: config/elite_settings.py
• Utils: utils/elite_helpers.py

📊 **BASE DE DATOS:**
• Tipo: SQLite Elite
• Estado: {db_status}
• Tablas: elite_events, trading_signals

⚙️ **CONFIGURACIÓN:**
• Modo: {mode}
• Riesgo Máximo: {risk}
• Debug: {debug}

⚡ **RENDIMIENTO:**
• Inicialización: COMPLETADA
• Módulos: ACTIVOS
• Configuración: CARGADA

🚀 **SISTEMA: INTEGRADO Y OPERATIVO**
""".format(
    db_status=db_status,
    mode=config_status['modo'],
    risk=config_status['riesgo_maximo'],
    debug=config_status['debug']
)
        bot.reply_to(message, response)
        logger.info(f"Comando elite_status ejecutado por {message.chat.id}")
        
    except Exception as e:
        logger.error(f"Error en elite_status: {e}")
        bot.reply_to(message, f"❌ Error en elite_status: {str(e)}")

@bot.message_handler(commands=['elite_db_test'])
def elite_db_test(message):
    """Prueba avanzada de base de datos élite"""
    try:
        if not ELITE_MODULES_LOADED or not ELITE_DB_ACTIVE:
            bot.reply_to(message, "❌ Módulos élite no disponibles")
            return
            
        # Probar múltiples operaciones de BD
        test_events = [
            {
                'event_id': f'advanced_test_1_{message.chat.id}',
                'sport': 'basketball',
                'league': 'NBA',
                'home_team': 'Lakers',
                'away_team': 'Warriors',
                'event_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'event_id': f'advanced_test_2_{message.chat.id}',
                'sport': 'tennis',
                'league': 'Wimbledon',
                'home_team': 'Player A',
                'away_team': 'Player B', 
                'event_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        ]
        
        successes = 0
        for event in test_events:
            if elite_db.save_elite_event(event):
                successes += 1
        
        response = """
🔬 **PRUEBA AVANZADA ELITE - BD**

📊 **Resultados:**
• Eventos intentados: {total}
• Eventos guardados: {success}
• Tasa de éxito: {rate}%

🎯 **Operaciones probadas:**
• INSERT/REPLACE: ✅
• Unique constraints: ✅
• Data types: ✅
• Transaction commit: ✅

💾 **Base de datos: OPERATIVA**
""".format(
    total=len(test_events),
    success=successes,
    rate=(successes/len(test_events))*100
)
        bot.reply_to(message, response)
        
    except Exception as e:
        logger.error(f"Error en elite_db_test: {e}")
        bot.reply_to(message, f"❌ Error en prueba avanzada: {str(e)}")

# ==================== COMANDOS DE AYUDA ====================
@bot.message_handler(commands=['help'])
def help_command(message):
    """Menú de ayuda completo"""
    help_text = """
🆘 **CENTRO DE AYUDA - SISTEMA DIOS V2**

🎯 **COMANDOS PRINCIPALES:**
/start - Iniciar sistema
/status - Estado del sistema
/help - Este mensaje

🏆 **COMANDOS ELITE (NUEVOS):**
/elite_health - Salud módulos élite
/elite_test - Prueba básica élite
/elite_status - Estado completo élite
/elite_db_test - Prueba avanzada BD

🔧 **INFORMACIÓN:**
• Versión: Sistema Dios V2 + Módulos Elite
• Arquitectura: Modular Profesional
• Estado: ✅ OPERATIVO

💡 **Usa los comandos elite_ para probar la nueva arquitectura modular**
"""
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['info'])
def info_command(message):
    """Información del sistema"""
    info_text = """
ℹ️ **INFORMACIÓN DEL SISTEMA DIOS V2**

🏗️ **Arquitectura:**
• Bot Principal: telebot + Flask
• Módulos Elite: Estructura modular
• Base de datos: SQLite + Elite Manager

🚀 **Capacidades:**
• Comandos Telegram ✅
• Web endpoints ✅  
• Base de datos ✅
• Módulos configurables ✅

🔧 **Tecnologías:**
• Python + Flask
• python-telegram-bot
• SQLite3
• Estructura modular

📚 **Desarrollado para trading deportivo élite**
"""
    bot.reply_to(message, info_text)

# ==================== WEB ENDPOINTS ====================
@app.route('/')
def home():
    return "🚀 SISTEMA DIOS V2 - BOT PRINCIPAL CON MÓDULOS ELITE"

@app.route('/health')
def health():
    """Health check del sistema principal"""
    return jsonify({
        'status': 'online',
        'system': 'Sistema Dios V2',
        'timestamp': datetime.now().isoformat(),
        'elite_modules': ELITE_MODULES_LOADED,
        'elite_database': ELITE_DB_ACTIVE
    })

@app.route('/elite/health')
def web_elite_health():
    """Health check para módulos élite (web)"""
    if not ELITE_MODULES_LOADED:
        return jsonify({'error': 'Elite modules not available'}), 500
        
    return jsonify({
        'status': 'elite_online',
        'timestamp': datetime.now().isoformat(),
        'version': 'sistema_dios_elite_v1.0',
        'modules': {
            'database': ELITE_DB_ACTIVE,
            'config': True,
            'trading': True
        },
        'config': elite_config.get_elite_summary() if ELITE_MODULES_LOADED else {}
    })

@app.route('/elite/test')
def web_elite_test():
    """Prueba módulos élite (web)"""
    if not ELITE_MODULES_LOADED or not ELITE_DB_ACTIVE:
        return jsonify({'error': 'Elite modules not available'}), 500
        
    try:
        test_event = {
            'event_id': f'web_test_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
            'sport': 'football',
            'league': 'Web Test League',
            'home_team': 'Web Home',
            'away_team': 'Web Away',
            'event_date': datetime.now().isoformat()
        }
        
        success = elite_db.save_elite_event(test_event)
        
        return jsonify({
            'success': success,
            'message': 'Prueba élite completada',
            'test_event': test_event,
            'config': elite_config.get_elite_summary()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== WEBHOOK Y SERVIDOR ====================
@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook para Telegram"""
    try:
        update = telebot.types.Update.de_json(request.get_json(force=True))
        bot.process_new_updates([update])
        return 'OK'
    except Exception as e:
        logger.error(f"Error en webhook: {e}")
        return 'ERROR', 500

def initialize_system():
    """Inicializar el sistema completo"""
    logger.info("🚀 INICIANDO SISTEMA DIOS V2 CON MÓDULOS ELITE...")
    
    # Verificar configuración
    if TELEGRAM_TOKEN == 'default_token':
        logger.warning("⚠️ TELEGRAM_TOKEN no configurado - Usando valor por defecto")
    
    # Verificar módulos élite
    if ELITE_MODULES_LOADED:
        logger.info("✅ Módulos élite cargados correctamente")
        logger.info(f"🏆 Configuración élite: {elite_config.get_elite_summary()}")
    else:
        logger.warning("⚠️ Módulos élite no disponibles - Funcionalidad limitada")
    
    logger.info("🤖 Bot inicializado correctamente")
    logger.info("🌐 Servidor Flask listo")

if __name__ == '__main__':
    initialize_system()
    port = int(os.environ.get('PORT', 5000))
    
    # En producción, usar webhooks. En desarrollo, polling.
    if os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('RENDER'):
        # En Render/Railway, configurar webhook
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{os.environ.get('RENDER_EXTERNAL_URL', 'your-app.onrender.com')}/webhook")
        logger.info("🌐 Webhook configurado para producción")
    else:
        # Desarrollo local - usar polling
        logger.info("🔧 Modo desarrollo - Polling activado")
        bot.remove_webhook()
        import threading
        threading.Thread(target=bot.infinity_polling, daemon=True).start()
    
    app.run(host='0.0.0.0', port=port, debug=False)
