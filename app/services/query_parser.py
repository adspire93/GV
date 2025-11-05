"""
Query Parser Service

Parses natural language user queries into structured data.
Extracts entities and determines user intent.

Capabilities:
- Natural language understanding
- Entity extraction (instrument, strike, date, action, quantity)
- Date/time parsing (yesterday, today morning, 15 Oct 2024 at 2 PM)
- Handle misspellings and variations

Example Queries:
- "NIFTY Futures" -> Snapshot request
- "BANKNIFTY 49500 PE price" -> Price lookup
- "What if I bought NIFTY yesterday?" -> Trade simulator
- "Show stocks above 210 ema" -> Screener request

Entities to Extract:
- Instrument: NIFTY, BANKNIFTY, stock symbols
- Strike: Numeric value (49500, 23000, etc.)
- Option type: CE, PE, Call, Put
- Date/time: Timestamps, relative dates
- Action: buy, sell, short, long
- Quantity: lots, numbers
"""

from typing import Dict, Optional
from datetime import datetime


class QueryParser:
    """Parses and structures user queries."""

    def __init__(self):
        """Initialize NLP models and patterns."""
        pass

    def parse(self, query_text: str) -> Dict:
        """
        Parse user query into structured format.

        Args:
            query_text: Raw user query from WhatsApp

        Returns:
            dict: {
                "original_query": str,
                "intent": str,  # snapshot, price, screener, simulator, help, unknown
                "entities": {
                    "instrument": str,
                    "strike": int,
                    "option_type": str,  # CE or PE
                    "date": datetime,
                    "action": str,  # buy or sell
                    "quantity": int
                },
                "confidence": float
            }
        """
        pass

    def extract_instrument(self, text: str) -> Optional[str]:
        """Extract instrument symbol from text."""
        pass

    def extract_strike(self, text: str) -> Optional[int]:
        """Extract option strike price from text."""
        pass

    def extract_option_type(self, text: str) -> Optional[str]:
        """Extract option type (CE/PE) from text."""
        pass

    def parse_date_time(self, text: str) -> Optional[datetime]:
        """
        Parse natural language date/time.

        Examples:
        - "yesterday" -> yesterday's date
        - "today morning" -> today 9:15 AM
        - "15 Oct 2024 at 2 PM" -> specific datetime
        """
        pass

    def extract_action(self, text: str) -> Optional[str]:
        """Extract trading action (buy/sell) from text."""
        pass

    def extract_quantity(self, text: str) -> int:
        """Extract quantity/lots from text. Defaults to 1."""
        pass
