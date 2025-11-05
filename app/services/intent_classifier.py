"""
Intent Classification Service

Determines what feature the user wants to use based on their query.

Intent Types:
1. snapshot: User wants 360-degree trade snapshot
2. price: User wants current or historical price
3. screener: User wants stock screening results
4. simulator: User wants what-if P&L calculation
5. help: User needs assistance
6. subscribe: User wants subscription info
7. unknown: Unable to determine intent

Classification Logic:
- Snapshot: Instrument name only, no specific request
- Price: Contains "price", "LTP", "rate", time references
- Screener: Contains "stocks", "list", "show", screener names, "ema", "rsi"
- Simulator: Contains "what if", "P&L", "profit", "loss", hypothetical language
- Help: Contains "help", "commands", "how to"
- Subscribe: Contains "subscribe", "plan", "pricing", "payment"

Confidence Threshold: 0.7 (below this, ask for clarification)
"""

from typing import Tuple


class IntentClassifier:
    """Classifies user intent from parsed query."""

    def __init__(self):
        """Initialize classifier with patterns and rules."""
        pass

    def classify(self, parsed_query: dict) -> Tuple[str, float]:
        """
        Classify user intent.

        Args:
            parsed_query: Parsed query from QueryParser

        Returns:
            tuple: (intent_name, confidence_score)
        """
        pass

    def is_snapshot_request(self, query: dict) -> bool:
        """Check if query is for trade snapshot."""
        pass

    def is_price_request(self, query: dict) -> bool:
        """Check if query is for price lookup."""
        pass

    def is_screener_request(self, query: dict) -> bool:
        """Check if query is for market screener."""
        pass

    def is_simulator_request(self, query: dict) -> bool:
        """Check if query is for trade simulator."""
        pass

    def is_help_request(self, query: dict) -> bool:
        """Check if query is asking for help."""
        pass

    def needs_clarification(self, confidence: float) -> bool:
        """
        Determine if clarification is needed.

        Args:
            confidence: Confidence score (0-1)

        Returns:
            bool: True if confidence below threshold
        """
        pass
