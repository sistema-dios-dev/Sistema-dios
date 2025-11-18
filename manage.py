#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("TELEGRAM_TOKEN", "")
    from elite_bot import DivineTradingBot
    import asyncio

    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        print("❌ Error: TELEGRAM_TOKEN no configurado")
        sys.exit(1)
    
    print("🛠️  Iniciando Sistema Dios en modo gestión...")
    bot = DivineTradingBot(token)
    asyncio.run(bot.run())

if __name__ == "__main__":
    main()


