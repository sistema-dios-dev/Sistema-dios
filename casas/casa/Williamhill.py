class WilliamHill:
    def __init__(self):
        self.name = "William Hill"
        self.commission = 0.06  # 6%
    
    def get_odds(self, event):
        return {
            'event': event,
            'odds': {
                'home': 2.05,
                'draw': 3.3,
                'away': 3.1
            }
        }
