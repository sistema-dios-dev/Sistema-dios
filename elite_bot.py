import os
import logging
import random
import time
import threading
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Importación robusta de Telegram
try:
    from telegram import Update
    from telegram.ext import Updater, CommandHandler, CallbackContext
    logger.info("✅ Telegram libraries imported successfully")
    TELEGRAM_AVAILABLE = True
except ImportError as e:
    logger.error(f"❌ Telegram import error: {e}")
    TELEGRAM_AVAILABLE = False

class SistemaDiosBot:
    def __init__(self, token: str, admin_chat_id: str):
        if not TELEGRAM_AVAILABLE:
            raise Exception("Telegram library not available")
            
        self.token = token
        self.admin_chat_id = admin_chat_id
        
        # Inicializar bot de Telegram
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.bot = self.updater.bot
        
        # 🔥 NÚCLEO DIVINO
        self.omnisciencia = 99.8
        self.omnipresencia = 156
        self.omnipotencia = 99.9
        
        # 📊 ESTADÍSTICAS
        self.estadisticas = {
            'alertas_emitidas': 0,
            'predicciones_acertadas': 0,
            'precision_global': 0.0,
            'profit_acumulado': 0.0,
            'racha_actual': 0,
            'mejor_racha': 0
        }
        
        self.alertas_activas = True
        self.sistema_iniciado = False
        
        # Configurar comandos
        self._configurar_comandos()
        logger.info("🔥 SISTEMA DIOS INICIALIZADO CORRECTAMENTE")

    def _configurar_comandos(self):
        """Configurar todos los comandos del bot"""
        self.dispatcher.add_handler(CommandHandler("start", self._comando_start))
        self.dispatcher.add_handler(CommandHandler("estadisticas", self._comando_estadisticas))
        self.dispatcher.add_handler(CommandHandler("sistema", self._comando_sistema))
        self.dispatcher.add_handler(CommandHandler("test", self._comando_test))
        self.dispatcher.add_handler(CommandHandler("alertas", self._comando_alertas))
        self.dispatcher.add_handler(CommandHandler("poder", self._comando_poder))

    def _comando_start(self, update, context):
        """Comando /start"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            update.message.reply_text("❌ *Acceso restringido*", parse_mode='Markdown')
            return
            
        mensaje = f"""
🔥 *SISTEMA DIOS SUPREMO - ACTIVADO*

🧠 *Núcleo Divino:*
• Omnisciencia: {self.omnisciencia}%
• Omnipresencia: {self.omnipresencia} nodos  
• Omnipotencia: {self.omnipotencia}%

📊 *Estadísticas:*
• Alertas: {self.estadisticas['alertas_emitidas']}
• Precisión: {self.estadisticas['precision_global']}%
• Profit: +${self.estadisticas['profit_acumulado']:.2f}
• Racha: {self.estadisticas['racha_actual']} victorias

⚡ *Comandos disponibles:*
/estadisticas - Métricas avanzadas
/sistema - Estado del sistema
/poder - Nivel de poder divino
/test - Probar alerta
/alertas - Activar/desactivar

🚨 *Alertas automáticas cada 2-7 minutos*
"""
        update.message.reply_text(mensaje, parse_mode='Markdown')
        
        # Iniciar sistema en segundo plano si no está iniciado
        if not self.sistema_iniciado:
            self._iniciar_sistema_dios()
            self.sistema_iniciado = True

    def _comando_estadisticas(self, update, context):
        """Comando /estadisticas"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        mensaje = f"""
📊 *ESTADÍSTICAS DEL SISTEMA DIOS*

🎯 *Rendimiento:*
• Alertas emitidas: {self.estadisticas['alertas_emitidas']}
• Precisión global: {self.estadisticas['precision_global']}%
• Profit acumulado: +${self.estadisticas['profit_acumulado']:.2f}
• Racha actual: {self.estadisticas['racha_actual']} victorias
• Mejor racha: {self.estadisticas['mejor_racha']}

⚡ *Sistema:*
• Estado: {'🟢 ACTIVO' if self.alertas_activas else '🔴 PAUSADO'}
• Próxima alerta: 2-7 minutos
• Última actualización: {datetime.now().strftime('%H:%M:%S')}
"""
        update.message.reply_text(mensaje, parse_mode='Markdown')

    def _comando_sistema(self, update, context):
        """Comando /sistema"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        mensaje = f"""
🔧 *ESTADO DEL SISTEMA DIOS*

🧠 *Núcleo Divino:*
• Omnisciencia: {self.omnisciencia}%
• Omnipresencia: {self.omnipresencia} nodos
• Omnipotencia: {self.omnipotencia}%

🤖 *Inteligencia Avanzada:*
• Red Neuronal: 98.7%
• Aprendizaje Automático: 97.3%
• Análisis Predictivo: 95.8%

📈 *Operativo:*
• Alertas: {'✅ ACTIVAS' if self.alertas_activas else '❌ INACTIVAS'}
• Estado: 🟢 OPTIMO
• Tiempo activo: Sistema continuo
"""
        update.message.reply_text(mensaje, parse_mode='Markdown')

    def _comando_poder(self, update, context):
        """Comando /poder"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        poder_total = (self.omnisciencia + self.omnipotencia) / 2
        
        mensaje = f"""
⚡ *NIVEL DE PODER DIVINO*

💎 *Poder Total:* {poder_total:.2f}%

📊 *Desglose:*
• Conocimiento Absoluto: {self.omnisciencia}%
• Poder de Ejecución: {self.omnipotencia}%
• Presencia Global: {self.omnipresencia} nodos

🎯 *Estado:* {'🔴 DIOS EN DESARROLLO' if poder_total < 80 else '🟡 SEMIDIOS' if poder_total < 95 else '🟢 DIOS COMPLETO'}

🚀 *Evolución continua activada*
"""
        update.message.reply_text(mensaje, parse_mode='Markdown')

    def _comando_test(self, update, context):
        """Comando /test - Generar alerta de prueba"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        self._generar_alerta_manual()
        update.message.reply_text("✅ *Alerta de prueba generada*", parse_mode='Markdown')

    def _comando_alertas(self, update, context):
        """Comando /alertas - Activar/desactivar alertas"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        self.alertas_activas = not self.alertas_activas
        estado = "✅ ACTIVADAS" if self.alertas_activas else "❌ DESACTIVADAS"
        update.message.reply_text(f"🔔 *Alertas {estado}*", parse_mode='Markdown')

    def _iniciar_sistema_dios(self):
        """Iniciar todos los sistemas en segundo plano"""
        # Hilo para evolución automática
        evolucion_thread = threading.Thread(target=self._sistema_evolucion, daemon=True)
        evolucion_thread.start()
        
        # Hilo para alertas automáticas
        alertas_thread = threading.Thread(target=self._sistema_alertas, daemon=True)
        alertas_thread.start()
        
        logger.info("🚀 Sistemas en segundo plano iniciados")

    def _sistema_evolucion(self):
        """Sistema de evolución automática"""
        while True:
            time.sleep(1800)  # 30 minutos
            # Mejorar estadísticas gradualmente
            self.omnisciencia = min(100.0, self.omnisciencia + 0.05)
            self.omnipotencia = min(100.0, self.omnipotencia + 0.03)
            self.omnipresencia += 1
            logger.info(f"🧠 Evolución: Omnisciencia {self.omnisciencia}%")

    def _sistema_alertas(self):
        """Sistema de alertas automáticas"""
        while True:
            if self.alertas_activas:
                # Espera aleatoria entre 2-7 minutos
                wait_time = random.randint(120, 420)
                time.sleep(wait_time)
                
                # Solo generar alertas en horario activo
                hora_actual = datetime.now().hour
                if 8 <= hora_actual <= 23:
                    self._generar_alerta_automatica()

    def _generar_alerta_automatica(self):
        """Generar alerta automática"""
        try:
            alerta = self._crear_alerta_prediccion()
            self.bot.send_message(
                chat_id=self.admin_chat_id,
                text=alerta,
                parse_mode='Markdown'
            )
            
            # Actualizar estadísticas
            self._actualizar_estadisticas()
            logger.info(f"🚨 Alerta automática #{self.estadisticas['alertas_emitidas']} enviada")
            
        except Exception as e:
            logger.error(f"❌ Error en alerta automática: {e}")

    def _generar_alerta_manual(self):
        """Generar alerta manual (comando test)"""
        try:
            alerta = self._crear_alerta_prediccion()
            self.bot.send_message(
                chat_id=self.admin_chat_id,
                text=alerta,
                parse_mode='Markdown'
            )
            logger.info("✅ Alerta manual enviada")
        except Exception as e:
            logger.error(f"❌ Error en alerta manual: {e}")

    def _crear_alerta_prediccion(self):
        """Crear contenido de alerta de predicción"""
        # Datos de ejemplo para la predicción
        ligas = ['CHAMPIONS LEAGUE', 'PREMIER LEAGUE', 'LA LIGA', 'SERIE A']
        equipos = ['Real Madrid', 'Barcelona', 'Bayern Munich', 'Manchester City', 'PSG', 'Liverpool', 'Chelsea', 'Arsenal']
        
        liga = random.choice(ligas)
        local = random.choice(equipos)
        visitante = random.choice([e for e in equipos if e != local])
        
        # Predicción más realista
        if random.random() > 0.3:
            ganador = local
        else:
            ganador = visitante
            
        marcador = f"{random.randint(1, 3)}-{random.randint(0, 2)}"
        confianza = random.randint(85, 97)
        profit_esperado = round(random.uniform(8.5, 15.5), 1)
        
        return f"""
🎯 *PREDICCIÓN DIOS ACTIVADA* 🎯

⚡ *SISTEMA DIOS v2.0* | Precisión: {self.estadisticas['precision_global']}%
⏰ *Detección:* {datetime.now().strftime('%H:%M:%S')}

🏆 *ENCUENTRO:*
• {local} 🆚 {visitante}
• Liga: {liga}
• Deporte: FÚTBOL

🎯 *PREDICCIÓN:*
• Ganador: *{ganador}*
• Confianza: *{confianza}%*
• Marcador: *{marcador}*

💰 *RECOMENDACIÓN:*
• Apuesta: {random.choice(['GANADOR', 'AMBOS MARCAN', 'MÁS 2.5 GOLES'])}
• Cuota: {round(random.uniform(1.65, 2.80), 2)}
• Stake: {random.randint(3, 7)}%
• Profit Esperado: *+{profit_esperado}%*

🔥 *ACCIÓN INMEDIATA RECOMENDADA*
"""

    def _actualizar_estadisticas(self):
        """Actualizar estadísticas después de cada alerta"""
        self.estadisticas['alertas_emitidas'] += 1
        
        # Simular 75% de aciertos
        if random.random() > 0.25:
            self.estadisticas['predicciones_acertadas'] += 1
            self.estadisticas['racha_actual'] += 1
            self.estadisticas['mejor_racha'] = max(self.estadisticas['mejor_racha'], self.estadisticas['racha_actual'])
            self.estadisticas['profit_acumulado'] += round(random.uniform(25, 120), 2)
        else:
            self.estadisticas['racha_actual'] = 0
        
        # Calcular precisión
        total = self.estadisticas['alertas_emitidas']
        aciertos = self.estadisticas['predicciones_acertadas']
        if total > 0:
            self.estadisticas['precision_global'] = round((aciertos / total) * 100, 2)

    def iniciar(self):
        """Iniciar el bot"""
        logger.info("🚀 INICIANDO SISTEMA DIOS...")
        self.updater.start_polling()
        logger.info("✅ Bot iniciado correctamente - Esperando comandos...")
        self.updater.idle()

def main():
    """Función principal"""
    # Obtener variables de entorno
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')
    
    if not TOKEN or not ADMIN_CHAT_ID:
        logger.error("❌ Faltan variables de entorno: TELEGRAM_TOKEN y ADMIN_CHAT_ID")
        logger.error("💡 Configura estas variables en Render -> Environment")
        return
    
    try:
        logger.info("🔥 CREANDO SISTEMA DIOS...")
        bot = SistemaDiosBot(token=TOKEN, admin_chat_id=ADMIN_CHAT_ID)
        logger.info("✅ Sistema Dios creado - Iniciando...")
        bot.iniciar()
    except Exception as e:
        logger.error(f"❌ Error crítico al iniciar: {e}")

if __name__ == '__main__':
    main()
