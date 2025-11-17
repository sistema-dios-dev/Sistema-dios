#!/usr/bin/env python3
"""
Sistema Dios - Módulos Elite
Bot de Trading Avanzado
"""

from flask import Flask, request, jsonify
import os
import logging
from datetime import datetime

# Importar módulos élite
from config.elite_settings import elite_config
from modules.elite_trading import EliteDatabase

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Inicializar componentes élite
elite_db = EliteDatabase()

@app.route('/')
def home():
    return "🏆 SISTEMA DIOS - MÓDULOS ELITE 🚀"

@app.route('/elite/health')
def elite_health():
    """Health check módulos élite"""
    return jsonify({
        'status': 'elite_online',
        'timestamp': datetime.now().isoformat(),
        'version': 'sistema_dios_elite_v1.0',
        'modules': {
            'database': 'active',
            'config': 'active'
        }
    })

@app.route('/elite/test')
def elite_test():
    """Probar módulos élite"""
    try:
        # Probar base de datos élite
        test_event = {
            'event_id': f'elite_test_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
            'sport': 'football',
            'league': 'Test League',
            'home_team': 'Elite Home',
            'away_team': 'Elite Away',
            'event_date': datetime.now().isoformat()
        }
        
        success = elite_db.save_elite_event(test_event)
        
        return jsonify({
            'success': success,
            'message': 'Prueba módulos élite completada',
            'config': elite_config.get_elite_summary(),
            'test_event_saved': success
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/elite/webhook', methods=['POST'])
def elite_webhook():
    """Webhook para comandos élite"""
    try:
        data = request.get_json()
        logger.info(f"Webhook élite recibido: {data}")
        
        return jsonify({
            'status': 'elite_webhook_processed',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error en webhook élite: {e}")
        return jsonify({'error': str(e)}), 500

def initialize_elite_system():
    """Inicializar sistema élite"""
    logger.info("🚀 INICIANDO MÓDULOS ELITE - SISTEMA DIOS")
    
    # Verificar configuración
    if elite_config.ELITE_TELEGRAM_TOKEN == 'default_elite_token':
        logger.warning("⚠️ ELITE_TELEGRAM_TOKEN no configurado")
    
    logger.info(f"🏆 Configuración élite: {elite_config.get_elite_summary()}")
    logger.info("✅ Módulos élite inicializados correctamente")

if __name__ == '__main__':
    initialize_elite_system()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=elite_config.ELITE_DEBUG)
