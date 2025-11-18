from elite_bot import DivineTradingBot
import asyncio
import os

if __name__ == "__main__":
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        print("❌ Error: Configura TELEGRAM_TOKEN")
        print("💡 Ejecuta: export TELEGRAM_TOKEN='tu_token_aqui'")
        exit(1)
    
    print("🚀 Iniciando Sistema Dios de Trading...")
    bot = DivineTradingBot(token)
    asyncio.run(bot.run())
