"""
Lot Size Calculator

Provides lot sizes for different instruments and contract types.

Lot Sizes (as of Nov 2024):
- NIFTY: 50 (futures and options)
- BANKNIFTY: 15 (futures and options)
- FINNIFTY: 40 (futures and options)
- MIDCPNIFTY: 75
- Stocks: Varies (typically 500-1000)

Note: Lot sizes change periodically. Should be updated or fetched dynamically.
"""

from typing import Dict, Optional


# Standard lot sizes for major indices
LOT_SIZES = {
    "NIFTY": 50,
    "BANKNIFTY": 15,
    "FINNIFTY": 40,
    "MIDCPNIFTY": 75,
    "SENSEX": 10,
    # Popular stocks (examples)
    "RELIANCE": 250,
    "TCS": 150,
    "INFY": 300,
    "HDFCBANK": 550,
    "ICICIBANK": 1375,
    "ITC": 3200,
    "SBIN": 1500,
    "BAJFINANCE": 125,
}


def get_lot_size(instrument: str, contract_type: str = "futures") -> int:
    """
    Get lot size for instrument.

    Args:
        instrument: Symbol (NIFTY, BANKNIFTY, etc.)
        contract_type: "futures" or "options"

    Returns:
        int: Lot size (default 1 if not found)
    """
    instrument_upper = instrument.upper()

    if instrument_upper in LOT_SIZES:
        return LOT_SIZES[instrument_upper]

    # Default lot size if not found
    return 1


def calculate_total_quantity(instrument: str, lots: int, contract_type: str = "futures") -> int:
    """
    Calculate total quantity from number of lots.

    Args:
        instrument: Symbol
        lots: Number of lots
        contract_type: "futures" or "options"

    Returns:
        int: Total quantity (lot_size × lots)
    """
    lot_size = get_lot_size(instrument, contract_type)
    return lot_size * lots


def calculate_lots_from_quantity(instrument: str, quantity: int, contract_type: str = "futures") -> float:
    """
    Calculate number of lots from quantity.

    Args:
        instrument: Symbol
        quantity: Total quantity
        contract_type: "futures" or "options"

    Returns:
        float: Number of lots
    """
    lot_size = get_lot_size(instrument, contract_type)
    return quantity / lot_size


def is_valid_lot_quantity(instrument: str, quantity: int, contract_type: str = "futures") -> bool:
    """
    Check if quantity is a valid multiple of lot size.

    Args:
        instrument: Symbol
        quantity: Quantity to check
        contract_type: "futures" or "options"

    Returns:
        bool: True if valid lot quantity
    """
    lot_size = get_lot_size(instrument, contract_type)
    return quantity % lot_size == 0


def get_lot_sizes_info() -> Dict[str, int]:
    """
    Get all available lot sizes.

    Returns:
        dict: Instrument to lot size mapping
    """
    return LOT_SIZES.copy()
