"""
Input Validators

Validates and sanitizes user inputs and data.

Validation Rules:
- Symbols: Alphanumeric, 1-20 characters
- Strikes: Positive integers, reasonable range
- Dates: Valid date formats, not in future (for historical)
- Phone numbers: Valid Indian mobile format
- Quantities: Positive integers, reasonable range (1-100)
"""

import re
from datetime import datetime
from typing import Optional, Tuple


def validate_symbol(symbol: str) -> Tuple[bool, str]:
    """
    Validate instrument symbol.

    Args:
        symbol: Instrument symbol

    Returns:
        tuple: (is_valid, error_message)
    """
    if not symbol:
        return False, "Symbol cannot be empty"

    if len(symbol) > 20:
        return False, "Symbol too long (max 20 characters)"

    if not re.match(r'^[A-Z0-9]+$', symbol.upper()):
        return False, "Symbol must be alphanumeric"

    return True, ""


def validate_strike(strike: int) -> Tuple[bool, str]:
    """
    Validate option strike price.

    Args:
        strike: Strike price

    Returns:
        tuple: (is_valid, error_message)
    """
    if strike <= 0:
        return False, "Strike must be positive"

    if strike > 1000000:
        return False, "Strike value too high"

    return True, ""


def validate_option_type(option_type: str) -> Tuple[bool, str]:
    """
    Validate option type (CE/PE).

    Args:
        option_type: Option type

    Returns:
        tuple: (is_valid, error_message)
    """
    if option_type.upper() not in ["CE", "PE", "CALL", "PUT"]:
        return False, "Option type must be CE or PE"

    return True, ""


def validate_date(date_str: str) -> Tuple[bool, Optional[datetime]]:
    """
    Validate and parse date string.

    Args:
        date_str: Date string in various formats

    Returns:
        tuple: (is_valid, parsed_datetime)
    """
    pass


def validate_phone_number(phone: str) -> Tuple[bool, str]:
    """
    Validate Indian phone number.

    Args:
        phone: Phone number

    Returns:
        tuple: (is_valid, error_message)
    """
    # Remove spaces and special characters
    cleaned = re.sub(r'[^\d+]', '', phone)

    # Check for valid Indian mobile format
    if not re.match(r'^\+91[6-9]\d{9}$', cleaned):
        if not re.match(r'^[6-9]\d{9}$', cleaned):
            return False, "Invalid Indian mobile number"

    return True, ""


def validate_quantity(quantity: int) -> Tuple[bool, str]:
    """
    Validate lot quantity.

    Args:
        quantity: Number of lots

    Returns:
        tuple: (is_valid, error_message)
    """
    if quantity <= 0:
        return False, "Quantity must be positive"

    if quantity > 100:
        return False, "Quantity too large (max 100 lots)"

    return True, ""


def sanitize_input(user_input: str) -> str:
    """
    Sanitize user input to prevent injection attacks.

    Args:
        user_input: Raw user input

    Returns:
        str: Sanitized input
    """
    # Remove potentially harmful characters
    sanitized = re.sub(r'[<>&;\'"\\]', '', user_input)
    return sanitized.strip()


def is_market_hours() -> bool:
    """
    Check if current time is during market hours.

    Market Hours: 9:15 AM - 3:30 PM IST (Mon-Fri)

    Returns:
        bool: True if market hours, False otherwise
    """
    pass


def is_trading_day() -> bool:
    """
    Check if today is a trading day (Mon-Fri, excluding holidays).

    Returns:
        bool: True if trading day, False otherwise
    """
    pass
