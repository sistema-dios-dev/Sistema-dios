import logging
import sys

def setup_logger(name='SistemaDios'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.ERROR)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

class DivineLogger:
    def __init__(self):
        self.logger = setup_logger()
    
    def log_miracle(self, message):
        self.logger.info(f"✨ MILAGRO: {message}")
    
    def log_intervention(self, message):
        self.logger.info(f"🔮 INTERVENCIÓN: {message}")
