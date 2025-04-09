from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import os

def fetch_data(symbol, exchange, interval, n_bars):
    tv = TvDatafeed()
    data = tv.get_hist(symbol=symbol, exchange=exchange, interval=interval, n_bars=n_bars)
    return data

def save_data_to_csv(data, filename):
    if data is not None and not data.empty:
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

def extract_and_save_data(symbol, exchange, interval, n_bars=10000, output_file=None, 
                         futures=False, contract=1, extended=False):
    """
    Extract data from TradingView and save it to a file.
    
    Args:
        symbol: Trading symbol
        exchange: Exchange name
        interval: Time interval
        n_bars: Number of bars to fetch
        output_file: Output file path or just filename (if no directory, saves to data folder)
        futures: Whether to fetch futures data
        contract: Future contract number
        extended: Whether to include extended session data
    
    Returns:
        DataFrame of fetched data
    """
    tv = TvDatafeed()
    
    # Fetch the data
    if futures:
        data = tv.get_hist(symbol=symbol, exchange=exchange, interval=interval, 
                         n_bars=n_bars, fut_contract=contract, extended_session=extended)
    else:
        data = tv.get_hist(symbol=symbol, exchange=exchange, interval=interval, 
                         n_bars=n_bars, extended_session=extended)
    
    # Define default data directory path (relative to project root)
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    
    # If no output file specified, create default path in data folder
    if output_file is None:
        # Create default filename with symbol, exchange and interval
        filename = f"{symbol}_{exchange}_{interval}.csv"
        # Ensure data directory exists
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        # Set full output path
        output_file = os.path.join(data_dir, filename)
    # If output_file is just a filename without directory, save to data folder
    elif os.path.basename(output_file) == output_file:
        # Ensure data directory exists
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        # Set full output path
        output_file = os.path.join(data_dir, output_file)
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the data
    if output_file.endswith('.csv'):
        data.to_csv(output_file)
    elif output_file.endswith('.json'):
        data.to_json(output_file)
    elif output_file.endswith('.xlsx'):
        data.to_excel(output_file)
    else:
        # Default to CSV if no recognized extension
        data.to_csv(output_file + '.csv')
        output_file = output_file + '.csv'
    
    print(f"Data saved to {output_file}")
    return data