# TradingView Data Fetcher

![TradingView Data Fetcher](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview
The TradingView Data Fetcher is a powerful command-line interface (CLI) tool that extracts historical market data from TradingView through the TvDatafeed library. This tool provides traders, analysts, and researchers with easy access to financial market data for various instruments across multiple exchanges and timeframes.

## Key Features
- **Multi-Exchange Support**: Extract data from popular exchanges including BINANCE, NSE, MCX, and many more
- **Flexible Time Intervals**: Access data in various timeframes including:
  - Minute intervals (1m, 3m, 5m, 15m, 30m, 45m)
  - Hourly intervals (1h, 2h, 3h, 4h)
  - Daily, weekly, and monthly intervals (1d, 1w, 1M)
- **Futures Support**: Fetch data for futures contracts with configurable contract numbers
- **Multiple Output Formats**: Save data in CSV, JSON, or Excel formats
- **Extended Session Data**: Option to include or exclude extended market hours
- **Data Validation**: Built-in validation for symbols, exchanges, and intervals
- **User-Friendly CLI**: Simple and intuitive command-line interface with comprehensive help documentation

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/drunktrader/tradingview-data-fetcher.git
   cd tradingview-data-fetcher
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) For development:
   ```
   pip install -e .
   ```

## Usage

### Basic Command Structure
```
python -m tradingview-data-fetcher.src.cli fetch [OPTIONS]
```

### Available Commands
- `fetch`: Extract and save financial market data
- `info`: Display information about available options and default settings

### Command-Line Options for 'fetch'
| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--symbol` | `-s` | Yes | Trading symbol (e.g., LTCUSDT, NIFTY, CRUDEOIL) |
| `--exchange` | `-e` | Yes | Exchange name (e.g., BINANCE, NSE, MCX) |
| `--interval` | `-i` | Yes | Time interval (1m, 3m, 5m, 15m, 30m, 45m, 1h, 2h, 3h, 4h, 1d, 1w, 1M) |
| `--bars` | `-b` | No | Number of bars/candles to fetch (default: 10000) |
| `--output` | `-o` | No | Output file path (default: data.csv) |
| `--format` | `-f` | No | Output file format: csv, json, excel (default: csv) |
| `--futures` | | No | Flag to fetch futures contract data |
| `--contract` | | No | Future contract number (used with --futures, default: 1) |
| `--extended` | | No | Flag to include extended session data |

### Examples

#### Fetch daily data for LTCUSDT from Binance
```
python -m tradingview-data-fetcher.src.cli fetch --symbol LTCUSDT --exchange BINANCE --interval 1d --output data/ltc_daily.csv
```

#### Fetch 5-minute data for NIFTY from NSE
```
python -m tradingview-data-fetcher.src.cli fetch --symbol NIFTY --exchange NSE --interval 5m --output data/nifty_5min.csv
```

#### Fetch hourly futures data for crude oil in JSON format
```
python -m tradingview-data-fetcher.src.cli fetch --symbol CRUDEOIL --exchange MCX --interval 1h --futures --contract 1 --output data/crudeoil_futures_1h.json --format json
```

#### Display information about available options
```
python -m tradingview-data-fetcher.src.cli info
```

## Directory Structure

```
tradingview-data-fetcher/
├── tradingview-data-fetcher/
│   ├── src/                      # Source code
│   │   ├── __init__.py           # Package initialization
│   │   ├── cli.py                # Command-line interface implementation
│   │   ├── data_extractor.py     # Core data extraction functionality
│   │   ├── config.py             # Configuration settings
│   │   ├── utils/                # Utility modules
│   │   │   ├── __init__.py
│   │   │   ├── validators.py     # Input validation functions
│   │   │   └── formatters.py     # Data formatting utilities
│   │   └── models/               # Data models
│   │       ├── __init__.py
│   │       └── interval.py       # Time interval definitions
│   ├── data/                     # Default directory for saved data
│   │   └── .gitkeep
│   ├── tests/                    # Unit tests
│   │   ├── __init__.py
│   │   ├── test_cli.py           # CLI tests
│   │   └── test_data_extractor.py # Data extractor tests
│   ├── requirements.txt          # Project dependencies
│   ├── setup.py                  # Package setup script
│   ├── README.md                 # Project documentation
│   └── .gitignore                # Git ignore rules
└── .venv/                        # Virtual environment (not tracked in git)
```

## Data Output Format

The tool exports financial data with the following columns:
- **Date/Time**: Timestamp for each bar/candle
- **Symbol**: Trading symbol with exchange prefix
- **Open**: Opening price
- **High**: Highest price during the period
- **Low**: Lowest price during the period
- **Close**: Closing price
- **Volume**: Trading volume

Example CSV output:
```
datetime,symbol,open,high,low,close,volume
2023-04-01 00:00:00,BINANCE:LTCUSDT,90.12,92.45,89.78,91.23,12345.0
2023-04-02 00:00:00,BINANCE:LTCUSDT,91.23,93.01,90.55,92.67,23456.0
...
```

## Troubleshooting

### Common Issues

1. **Module not found errors**:
   - Make sure all required packages are installed: `pip install -r requirements.txt`
   - Ensure you're running the command from the project root directory

2. **Authentication errors**:
   - Update credentials in `config.py` if needed

3. **Rate limiting**:
   - Reduce number of requests by fetching fewer bars
   - Add delays between multiple requests

## Development and Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and add tests
4. Run tests: `pytest`
5. Commit your changes: `git commit -m "Add new feature"`
6. Push to your branch: `git push origin feature/new-feature`
7. Create a Pull Request

### Development Setup
```
pip install -e ".[dev]"
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The [TvDatafeed](https://github.com/rongardF/tvdatafeed) library by rongardF for providing the core functionality to fetch data from TradingView
- All contributors and users of this tool

---

*Disclaimer: This tool is not officially affiliated with TradingView. Use responsibly and in accordance with TradingView's terms of service.*