import sqlite3
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class EliteDatabase:
    """Gestor de base de datos para trading élite"""
    
    def __init__(self, db_path="sistema_dios_elite.db"):
        self.db_path = db_path
        self.init_elite_database()
    
    def init_elite_database(self):
        """Inicializar base de datos élite"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Tabla de eventos élite
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS elite_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id TEXT UNIQUE,
                    sport TEXT,
                    league TEXT,
                    home_team TEXT,
                    away_team TEXT,
                    event_date DATETIME,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabla de señales de trading
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trading_signals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id TEXT,
                    signal_type TEXT,
                    confidence REAL,
                    odds REAL,
                    stake_suggested REAL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            logger.info("✅ Base de datos élite inicializada")
            
        except Exception as e:
            logger.error(f"❌ Error base de datos élite: {e}")
        finally:
            conn.close()
    
    def save_elite_event(self, event_data):
        """Guardar evento élite"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO elite_events 
                (event_id, sport, league, home_team, away_team, event_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                event_data['event_id'],
                event_data['sport'],
                event_data.get('league', 'Unknown'),
                event_data['home_team'],
                event_data['away_team'],
                event_data['event_date']
            ))
            
            conn.commit()
            return True
        except Exception as e:
            logger.error(f"Error guardando evento élite: {e}")
            return False
        finally:
            conn.close()
