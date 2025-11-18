class ArbitrajeStrategy:
    def __init__(self):
        self.min_profit = 0.02  # 2%
        self.max_wait_time = 5  # segundos
    
    def find_arbitrage_opportunities(self):
        """Encontrar oportunidades de arbitraje"""
        return [
            {
                'sport': '⚽ Football',
                'match': 'Team A vs Team B',
                'profit': 5.2,
                'bookmakers': ['Bet365', 'William Hill'],
                'stakes': [100, 95],
                'guaranteed_profit': 5.2
            }
        ]
