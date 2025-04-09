from pathlib import Path

class Config:
    def __init__(self):
        self.username = 'YourTradingViewUsername'
        self.password = 'YourTradingViewPassword'
        self.default_symbol = 'LTCUSDT'
        self.default_exchange = 'BINANCE'
        self.default_interval = '1D'
        self.output_directory = Path('data')
        self.output_format = 'csv'

    def get_credentials(self):
        return self.username, self.password

    def get_default_settings(self):
        return {
            'symbol': self.default_symbol,
            'exchange': self.default_exchange,
            'interval': self.default_interval,
            'output_directory': self.output_directory,
            'output_format': self.output_format
        }