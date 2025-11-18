import os
import asyncio
import logging

# Configurar logging simple
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    try:
        token = os.environ.get('TELEGRAM_TOKEN')
        if not token:
            logger.error("❌ TELEGRAM_TOKEN no encontrado")
            logger.info("💡 Configura TELEGRAM_TOKEN en las variables de entorno de Render")
            return
        
        logger.info("🚀 INICIANDO SISTEMA DIOS EN RENDER...")
        
        # Importar después de verificar el token
        from elite_bot import DivineTradingBot
        
        bot = DivineTradingBot(token)
        await bot.run()
        
    except Exception as e:
        logger.error(f"❌ Error crítico: {e}")
        # Mantener el contenedor vivo para que Render no lo marque como fallido
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
