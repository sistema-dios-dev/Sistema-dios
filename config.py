import os

class Config:
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
    
    # Modo operación
    DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
    GOD_MODE = True
    
    # Límites de riesgo
    MAX_RISK_PER_TRADE = 0.02  # 2%
    DAILY_LOSS_LIMIT = 0.1     # 10%
    
    # Bookmakers config
    BOOKMAKERS = {
        'bet365': {'active': True, 'weight': 0.3},
        'pinnacle': {'active': True, 'weight': 0.4},
        'williamhill': {'active': True, 'weight': 0.2},
        'betfair': {'active': True, 'weight': 0.1}
    }
