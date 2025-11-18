class Betfair:
    def __init__(self):
        self.name = "Betfair"
        self.commission = 0.05  # 5% mercado primario
    
    def get_odds(self, event):
        return {
            'event': event, 
            'odds': {
                'home': 2.08,
                'draw': 3.35,
                'away': 3.25
            }
        }
