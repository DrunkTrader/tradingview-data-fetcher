from click.testing import CliRunner
import pytest
from src.cli import main

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_help(runner):
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'Usage:' in result.output

def test_cli_valid_input(runner):
    result = runner.invoke(main, ['--symbol', 'LTCUSDT', '--exchange', 'BINANCE', '--interval', '1D', '--output', 'ltc_data.csv'])
    assert result.exit_code == 0
    assert 'Data extraction successful' in result.output

def test_cli_invalid_symbol(runner):
    result = runner.invoke(main, ['--symbol', 'INVALID_SYMBOL', '--exchange', 'BINANCE', '--interval', '1D', '--output', 'ltc_data.csv'])
    assert result.exit_code != 0
    assert 'Invalid symbol' in result.output

def test_cli_invalid_exchange(runner):
    result = runner.invoke(main, ['--symbol', 'LTCUSDT', '--exchange', 'INVALID_EXCHANGE', '--interval', '1D', '--output', 'ltc_data.csv'])
    assert result.exit_code != 0
    assert 'Invalid exchange' in result.output

def test_cli_invalid_interval(runner):
    result = runner.invoke(main, ['--symbol', 'LTCUSDT', '--exchange', 'BINANCE', '--interval', 'INVALID_INTERVAL', '--output', 'ltc_data.csv'])
    assert result.exit_code != 0
    assert 'Invalid interval' in result.output