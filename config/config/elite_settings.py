import os

class EliteConfig:
    """Configuración para módulos élite del Sistema Dios"""
    
    def __init__(self):
        # Telegram Elite
        self.ELITE_TELEGRAM_TOKEN = os.getenv('ELITE_TELEGRAM_TOKEN', 'default_elite_token')
        
        # Trading Elite
        self.ELITE_TRADING_MODE = os.getenv('ELITE_TRADING_MODE', 'SIMULATION')
        self.ELITE_MAX_RISK = float(os.getenv('ELITE_MAX_RISK', '3.0'))
        
        # Sistema
        self.ELITE_DEBUG = os.getenv('ELITE_DEBUG', 'True').lower() == 'true'
        
    def get_elite_summary(self):
        """Resumen configuración élite"""
        return {
            'sistema': 'Sistema Dios - Módulos Elite',
            'modo': self.ELITE_TRADING_MODE,
            'riesgo_maximo': f"{self.ELITE_MAX_RISK}%",
            'debug': self.ELITE_DEBUG
        }

# Configuración global élite
elite_config = EliteConfig()
