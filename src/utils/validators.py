import os

def validate_symbol(symbol):
    """Validate the trading symbol."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    return True

def validate_exchange(exchange):
    """Validate the exchange name."""
    valid_exchanges = ['BINANCE', 'NSE', 'MCX']
    if exchange.upper() not in valid_exchanges:
        raise ValueError(f"Exchange must be one of {', '.join(valid_exchanges)}")
    return True

def validate_interval(interval):
    """Validate the time interval."""
    valid_intervals = ['1m', '3m', '5m', '15m', '30m', '45m', '1h', '2h', '3h', '4h', '1d', '1w', '1M']
    if interval not in valid_intervals:
        raise ValueError(f"Interval must be one of {', '.join(valid_intervals)}")
    return True

def validate_output_file(output_file):
    """Validate the output file path."""
    # Check if directory exists and is writeable
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except:
            raise ValueError(f"Cannot create directory: {output_dir}")
    return True