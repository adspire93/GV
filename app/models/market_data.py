"""
Market Data Models

Represents market data structures (quotes, candles, options).
"""

from datetime import datetime
from typing import Optional


class Quote:
    """Live quote data."""

    def __init__(self, symbol: str, ltp: float):
        self.symbol = symbol
        self.ltp = ltp
        self.volume: int = 0
        self.change: float = 0.0
        self.change_percent: float = 0.0
        self.high: float = 0.0
        self.low: float = 0.0
        self.open: float = 0.0
        self.previous_close: float = 0.0
        self.timestamp = datetime.now()


class Candle:
    """OHLCV candle data."""

    def __init__(self, symbol: str, timestamp: datetime):
        self.symbol = symbol
        self.timestamp = timestamp
        self.open: float = 0.0
        self.high: float = 0.0
        self.low: float = 0.0
        self.close: float = 0.0
        self.volume: int = 0


class OptionContract:
    """Option contract data."""

    def __init__(self, symbol: str, strike: int, option_type: str, expiry: datetime):
        self.symbol = symbol
        self.strike = strike
        self.option_type = option_type  # CE or PE
        self.expiry = expiry
        self.ltp: float = 0.0
        self.iv: float = 0.0  # Implied Volatility
        self.delta: float = 0.0
        self.gamma: float = 0.0
        self.theta: float = 0.0
        self.vega: float = 0.0
        self.oi: int = 0  # Open Interest
        self.volume: int = 0


class FuturesContract:
    """Futures contract data."""

    def __init__(self, symbol: str, expiry: datetime):
        self.symbol = symbol
        self.expiry = expiry
        self.ltp: float = 0.0
        self.oi: int = 0  # Open Interest
        self.oi_change: float = 0.0
        self.volume: int = 0
        self.basis: float = 0.0  # Futures - Spot
