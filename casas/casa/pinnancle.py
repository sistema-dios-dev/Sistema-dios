class Pinnacle:
    def __init__(self):
        self.name = "Pinnacle"
        self.commission = 0.02  # 2% - más bajo
    
    def get_odds(self, event):
        return {
            'event': event,
            'odds': {
                'home': 2.15,
                'draw': 3.5,
                'away': 3.3
            },
            'timestamp': '2024-01-01 12:00:00'
        }
