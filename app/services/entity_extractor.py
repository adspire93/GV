"""
Entity Extraction Service

Extracts specific entities from user queries using NLP.

Entities:
1. Instrument: Stock/index symbols (NIFTY, BANKNIFTY, RELIANCE, TCS)
2. Strike Price: Numeric values for options (49500, 23000)
3. Option Type: CE (Call) or PE (Put)
4. Expiry: Monthly, weekly expiries
5. Date/Time: Trading dates and times
6. Action: Buy, Sell, Short, Long
7. Quantity: Number of lots
8. Price: Specific price levels

Handles Variations:
- "NIFTY" = "Nifty" = "nifty" = "nf"
- "BANKNIFTY" = "Bank Nifty" = "BNF"
- "CE" = "Call" = "call option"
- "PE" = "Put" = "put option"
"""

from typing import Dict, Optional, List
from datetime import datetime


class EntityExtractor:
    """Extracts entities from natural language queries."""

    def __init__(self):
        """Initialize entity patterns and mappings."""
        self.instrument_aliases = {
            "nifty": "NIFTY",
            "nf": "NIFTY",
            "banknifty": "BANKNIFTY",
            "bnf": "BANKNIFTY",
            "finnifty": "FINNIFTY",
            # Add more aliases
        }
        pass

    def extract_all(self, text: str) -> Dict:
        """
        Extract all entities from text.

        Args:
            text: User query text

        Returns:
            dict: All extracted entities
        """
        pass

    def normalize_instrument(self, instrument: str) -> str:
        """
        Normalize instrument name to standard format.

        Args:
            instrument: Raw instrument name from query

        Returns:
            str: Standardized instrument symbol
        """
        pass

    def extract_numbers(self, text: str) -> List[int]:
        """Extract all numeric values from text."""
        pass

    def is_futures_query(self, text: str) -> bool:
        """Check if query is about futures."""
        pass

    def is_options_query(self, text: str) -> bool:
        """Check if query is about options."""
        pass
