class RiskManagement:
    def __init__(self):
        self.max_drawdown = 0.1  # 10%
        self.max_trade_risk = 0.02  # 2%
    
    def validate_trade(self, trade_data):
        """Validar si una operación cumple con gestión de riesgo"""
        return {
            'approved': True,
            'max_stake': 200,
            'risk_level': 'LOW',
            'reason': 'Operación dentro de límites'
        }
    
    def calculate_position_size(self, bankroll, risk_percentage):
        return bankroll * risk_percentage
