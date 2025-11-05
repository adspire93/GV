"""
Trade Model

Represents simulated trade data for "what-if" calculations.
"""

from datetime import datetime
from typing import Optional


class SimulatedTrade:
    """Simulated trade with P&L calculation."""

    def __init__(self, instrument: str, contract_type: str, action: str):
        self.instrument = instrument
        self.contract_type = contract_type  # futures or options
        self.action = action  # buy or sell
        self.strike: Optional[int] = None
        self.option_type: Optional[str] = None  # CE or PE

        # Entry details
        self.entry_price: float = 0.0
        self.entry_time: Optional[datetime] = None

        # Exit details
        self.exit_price: float = 0.0
        self.exit_time: Optional[datetime] = None

        # Trade details
        self.lot_size: int = 0
        self.quantity: int = 1  # Number of lots
        self.total_quantity: int = 0  # lot_size × quantity

        # P&L
        self.points_change: float = 0.0
        self.pnl_absolute: float = 0.0
        self.pnl_percentage: float = 0.0

    def calculate_pnl(self):
        """Calculate P&L based on entry/exit prices."""
        self.total_quantity = self.lot_size * self.quantity

        if self.action == "buy":
            self.points_change = self.exit_price - self.entry_price
        else:  # sell/short
            self.points_change = self.entry_price - self.exit_price

        self.pnl_absolute = self.points_change * self.total_quantity

        if self.action == "buy":
            investment = self.entry_price * self.total_quantity
        else:
            investment = self.exit_price * self.total_quantity

        if investment > 0:
            self.pnl_percentage = (self.pnl_absolute / investment) * 100

    def to_dict(self) -> dict:
        """Convert trade object to dictionary."""
        pass
