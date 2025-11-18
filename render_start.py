import os
import asyncio
from elite_bot import DivineTradingBot

async def main():
    token = os.environ.get('TELEGRAM_TOKEN')
    if not token:
        print("❌ Error: TELEGRAM_TOKEN no encontrado en Render")
        return
    
    print("🚀 INICIANDO SISTEMA DIOS EN RENDER...")
    bot = DivineTradingBot(token)
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
