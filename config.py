import os
from dotenv import load_dotenv

load_dotenv()

# Configuración del bot
BOT_TOKEN = os.getenv('BOT_TOKEN', 'tu_token_aqui')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')

# Configuración de APIs
API_KEY = os.getenv('API_KEY', '')

# Configuración del servidor
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
PORT = int(os.getenv('PORT', '8000'))