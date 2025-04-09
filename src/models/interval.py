from enum import Enum

class Interval(Enum):
    MINUTE_1 = '1m'
    MINUTE_3 = '3m'
    MINUTE_5 = '5m'
    MINUTE_15 = '15m'
    MINUTE_30 = '30m'
    MINUTE_45 = '45m'
    HOUR_1 = '1h'
    HOUR_2 = '2h'
    HOUR_3 = '3h'
    HOUR_4 = '4h'
    DAY_1 = '1d'
    WEEK_1 = '1w'
    MONTH_1 = '1M'
    
    @classmethod
    def list_intervals(cls):
        return [e.value for e in cls]