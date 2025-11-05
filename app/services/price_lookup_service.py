"""
Price Lookup Service (Feature 2)

Handles on-demand price queries for specific contracts (live or historical).

Capabilities:
- Live prices: 1-minute candle data
- Historical prices: 15-minute candle data
- Support futures and options contracts
- Handle natural language date/time

Example Queries:
- "What is the live price of NIFTY Futures?"
  -> Current LTP with timestamp

- "BANKNIFTY 49500 PE price on 15 Oct 2024 at 2:00 PM"
  -> Historical price at specific time

- "RELIANCE 2900 CE LTP now"
  -> Current call option price

Data Sources:
- Live: Real-time market data API (< 1s latency)
- Historical: Time-series database (InfluxDB)

Caching:
- Live prices: 1 minute TTL
- Historical prices: 1 hour TTL (immutable data)

Error Handling:
- Market closed: Return last available price with disclaimer
- Invalid contract: Suggest similar valid contracts
- Data unavailable: Offer alternative timeframes
"""

from typing import Dict, Optional
from datetime import datetime


class PriceLookupService:
    """Handles price lookup queries."""

    def __init__(self):
        """Initialize with data fetcher and cache."""
        pass

    def get_price(self, instrument: str, contract_type: str,
                  strike: Optional[int] = None, option_type: Optional[str] = None,
                  timestamp: Optional[datetime] = None) -> Dict:
        """
        Get price for specified contract.

        Args:
            instrument: Symbol (NIFTY, BANKNIFTY, etc.)
            contract_type: "futures" or "options"
            strike: Strike price (for options)
            option_type: "CE" or "PE" (for options)
            timestamp: Specific time for historical price, None for live

        Returns:
            dict: {
                "price": float,
                "timestamp": datetime,
                "volume": int,
                "change": float,
                "is_live": bool,
                "market_status": str  # open, closed, pre_open
            }
        """
        pass

    def get_live_price(self, contract_identifier: str) -> Optional[float]:
        """
        Fetch live price from market data API.

        Args:
            contract_identifier: Formatted contract ID

        Returns:
            float: Current LTP or None if unavailable
        """
        pass

    def get_historical_price(self, contract_identifier: str, timestamp: datetime) -> Optional[float]:
        """
        Fetch historical price from time-series database.

        Args:
            contract_identifier: Formatted contract ID
            timestamp: Requested time

        Returns:
            float: Price at timestamp or None if unavailable
        """
        pass

    def format_price_response(self, price_data: Dict, query: str) -> str:
        """
        Format price data into WhatsApp message.

        Args:
            price_data: Price information dict
            query: Original user query

        Returns:
            str: Formatted WhatsApp message
        """
        pass

    def suggest_alternatives(self, instrument: str) -> str:
        """Suggest alternative instruments if requested one not found."""
        pass
