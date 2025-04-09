import click
import os
from tvDatafeed import TvDatafeed, Interval
import sys

# Add the project root to Python path to make imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import from local modules
from src.utils.validators import validate_symbol, validate_exchange, validate_interval, validate_output_file
from src.utils.formatters import format_data
from src.models.interval import Interval as IntervalEnum
from src.data_extractor import extract_and_save_data
from src.config import Config

@click.group()
def main():
    """TradingView Data Fetcher CLI - Extract and save financial data."""
    pass

@main.command('fetch')
@click.option('--symbol', '-s', required=True, help='Symbol to fetch data for (e.g., LTCUSDT)')
@click.option('--exchange', '-e', required=True, help='Exchange to fetch data from (e.g., BINANCE, NSE, MCX)')
@click.option('--interval', '-i', required=True, 
              type=click.Choice(['1m', '3m', '5m', '15m', '30m', '45m', '1h', '2h', '3h', '4h', '1d', '1w', '1M']), 
              help='Time interval for data')
@click.option('--bars', '-b', default=10000, type=int, help='Number of bars to fetch (default: 10000)')
@click.option('--output', '-o', default='data.csv', help='Output file name (default: data.csv)')
@click.option('--format', '-f', type=click.Choice(['csv', 'json', 'excel']), default='csv', 
              help='Output file format (default: csv)')
@click.option('--futures', is_flag=True, help='Fetch futures contract data')
@click.option('--contract', default=1, type=int, help='Future contract number (used with --futures)')
@click.option('--extended', is_flag=True, help='Include extended session data')
def fetch(symbol, exchange, interval, bars, output, format, futures, contract, extended):
    """Fetch historical data from TradingView."""
    try:
        # Map interval string to Interval enum
        interval_map = {
            '1m': Interval.in_1_minute,
            '3m': Interval.in_3_minute,
            '5m': Interval.in_5_minute,
            '15m': Interval.in_15_minute,
            '30m': Interval.in_30_minute,
            '45m': Interval.in_45_minute,
            '1h': Interval.in_1_hour,
            '2h': Interval.in_2_hour,
            '3h': Interval.in_3_hour,
            '4h': Interval.in_4_hour,
            '1d': Interval.in_daily,
            '1w': Interval.in_weekly,
            '1M': Interval.in_monthly
        }
        
        tv_interval = interval_map.get(interval)
        
        # Initialize TvDatafeed
        tv = TvDatafeed()
        
        # Fetch data
        click.echo(f"Fetching {bars} bars of {interval} data for {symbol} from {exchange}...")
        
        if futures:
            click.echo(f"Using futures contract #{contract}")
            data = tv.get_hist(symbol=symbol, exchange=exchange, interval=tv_interval, 
                             n_bars=bars, fut_contract=contract, extended_session=extended)
        else:
            data = tv.get_hist(symbol=symbol, exchange=exchange, interval=tv_interval, 
                             n_bars=bars, extended_session=extended)
        
        if data is not None and not data.empty:
            # Ensure the output directory exists
            output_dir = os.path.dirname(output)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            # Save data in the requested format
            if format == 'csv':
                data.to_csv(output)
            elif format == 'json':
                data.to_json(output)
            elif format == 'excel':
                data.to_excel(output)
                
            click.echo(click.style(f"✓ Data extraction successful! Saved to {output}", fg="green"))
        else:
            click.echo(click.style("✗ No data returned from TradingView", fg="red"))
            
    except Exception as e:
        click.echo(click.style(f"✗ Error: {str(e)}", fg="red"))

@main.command('info')
def info():
    """Display information about available options."""
    click.echo("Available Exchanges: BINANCE, NSE, MCX")
    click.echo("Available Intervals: 1m, 3m, 5m, 15m, 30m, 45m, 1h, 2h, 3h, 4h, 1d, 1w, 1M")
    
    config = Config()
    defaults = config.get_default_settings()
    click.echo("\nDefault Settings:")
    for key, value in defaults.items():
        click.echo(f"  - {key}: {value}")

if __name__ == "__main__":
    main()