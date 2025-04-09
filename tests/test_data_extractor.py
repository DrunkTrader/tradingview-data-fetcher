import unittest
from src.data_extractor import TvDatafeed, Interval
import os

class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        self.tv = TvDatafeed()

    def test_get_hist_valid_data(self):
        data = self.tv.get_hist('LTCUSDT', 'BINANCE', Interval.in_daily, 100)
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_get_hist_invalid_symbol(self):
        with self.assertRaises(Exception):
            self.tv.get_hist('INVALID_SYMBOL', 'BINANCE', Interval.in_daily, 100)

    def test_get_hist_invalid_exchange(self):
        with self.assertRaises(Exception):
            self.tv.get_hist('LTCUSDT', 'INVALID_EXCHANGE', Interval.in_daily, 100)

    def test_get_hist_invalid_interval(self):
        with self.assertRaises(Exception):
            self.tv.get_hist('LTCUSDT', 'BINANCE', 'INVALID_INTERVAL', 100)

    def test_save_data_to_csv(self):
        data = self.tv.get_hist('LTCUSDT', 'BINANCE', Interval.in_daily, 100)
        file_path = 'test_data.csv'
        data.to_csv(file_path)
        self.assertTrue(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()