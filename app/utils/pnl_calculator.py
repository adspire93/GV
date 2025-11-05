"""
Profit & Loss Calculator

Calculates P&L for trades (used by trade simulator).

Calculation Formulas:
- LONG (Buy): P&L = (Exit Price - Entry Price) × Quantity
- SHORT (Sell): P&L = (Entry Price - Exit Price) × Quantity
- ROI% = (P&L / Investment) × 100

Investment Calculation:
- For LONG: Entry Price × Quantity
- For SHORT: Exit Price × Quantity (margin-based approximation)
"""

from typing import Dict


def calculate_pnl(entry_price: float, exit_price: float,
                 action: str, quantity: int) -> Dict:
    """
    Calculate P&L for a trade.

    Args:
        entry_price: Entry price per unit
        exit_price: Exit price per unit
        action: "buy" or "sell"
        quantity: Total quantity

    Returns:
        dict: {
            "points_change": float,
            "pnl_absolute": float,
            "pnl_percentage": float,
            "investment": float,
            "final_value": float
        }
    """
    result = {}

    # Calculate points change
    if action.lower() in ["buy", "long"]:
        result["points_change"] = exit_price - entry_price
        result["investment"] = entry_price * quantity
        result["final_value"] = exit_price * quantity
    else:  # sell/short
        result["points_change"] = entry_price - exit_price
        result["investment"] = exit_price * quantity  # Approximation
        result["final_value"] = entry_price * quantity

    # Calculate absolute P&L
    result["pnl_absolute"] = result["points_change"] * quantity

    # Calculate percentage P&L
    if result["investment"] > 0:
        result["pnl_percentage"] = (result["pnl_absolute"] / result["investment"]) * 100
    else:
        result["pnl_percentage"] = 0.0

    return result


def calculate_options_pnl(entry_premium: float, exit_premium: float,
                         action: str, lot_size: int, lots: int) -> Dict:
    """
    Calculate P&L for options trade.

    Args:
        entry_premium: Entry option premium
        exit_premium: Exit option premium
        action: "buy" or "sell"
        lot_size: Contract lot size
        lots: Number of lots

    Returns:
        dict: P&L calculations
    """
    quantity = lot_size * lots
    return calculate_pnl(entry_premium, exit_premium, action, quantity)


def calculate_futures_pnl(entry_price: float, exit_price: float,
                         action: str, lot_size: int, lots: int) -> Dict:
    """
    Calculate P&L for futures trade.

    Args:
        entry_price: Entry futures price
        exit_price: Exit futures price
        action: "buy" or "sell"
        lot_size: Contract lot size
        lots: Number of lots

    Returns:
        dict: P&L calculations
    """
    quantity = lot_size * lots
    return calculate_pnl(entry_price, exit_price, action, quantity)


def format_pnl(pnl: float) -> str:
    """
    Format P&L with appropriate sign and color indicator.

    Args:
        pnl: P&L amount

    Returns:
        str: Formatted P&L string
    """
    if pnl > 0:
        return f"+₹{pnl:,.2f}"
    elif pnl < 0:
        return f"-₹{abs(pnl):,.2f}"
    else:
        return "₹0.00"


def estimate_brokerage(pnl: float, trade_type: str = "intraday") -> float:
    """
    Estimate brokerage and taxes (rough approximation).

    Args:
        pnl: P&L amount
        trade_type: "intraday" or "delivery"

    Returns:
        float: Estimated brokerage + taxes
    """
    # Very rough approximation: 0.5% of P&L for intraday
    # Actual brokerage depends on broker, STT, GST, etc.
    if trade_type == "intraday":
        return abs(pnl) * 0.005
    else:
        return abs(pnl) * 0.01
