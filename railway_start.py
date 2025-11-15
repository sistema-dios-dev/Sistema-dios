#!/usr/bin/env python3
import os
import sys
import subprocess

def start_bot():
    """Inicia el bot principal"""
    print("🚂 Iniciando bot en Railway...")
    try:
        # Importar y ejecutar el bot principal
        from main import main
        import asyncio
        
        print("✅ Módulos importados correctamente")
        asyncio.run(main())
        
    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")
        sys.exit(1)

if _name_ == "_main_":
    start_bot()