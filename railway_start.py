import os
from elite_bot import DivineTradingBot
import asyncio

async def start_bot():
    token = os.environ.get('TELEGRAM_TOKEN')
    if not token:
        raise ValueError("❌ TELEGRAM_TOKEN no configurado en Railway")
    
    bot = DivineTradingBot(token)
    await bot.run()

if __name__ == "__main__":
    asyncio.run(start_bot())
