"""
Date and Time Parser

Parses natural language date/time expressions into datetime objects.

Supported Formats:
- Relative: "yesterday", "today", "today morning"
- Specific: "15 Oct 2024", "15 Oct 2024 at 2 PM"
- Time only: "2 PM", "14:30", "market open", "market close"

Market Timing Context:
- "morning" = 9:15 AM (market open)
- "afternoon" = 1:00 PM
- "close" = 3:30 PM (market close)
- "open" = 9:15 AM
"""

from datetime import datetime, timedelta
from typing import Optional
import re


def parse_natural_date(date_str: str) -> Optional[datetime]:
    """
    Parse natural language date expression.

    Args:
        date_str: Natural language date/time

    Returns:
        datetime: Parsed datetime or None if invalid

    Examples:
        "yesterday" -> yesterday's date at market open
        "today morning" -> today 9:15 AM
        "15 Oct 2024 at 2 PM" -> October 15, 2024 2:00 PM
        "yesterday close" -> yesterday 3:30 PM
    """
    pass


def parse_relative_date(date_str: str) -> Optional[datetime]:
    """
    Parse relative dates (yesterday, today, tomorrow).

    Args:
        date_str: Relative date string

    Returns:
        datetime: Parsed datetime or None
    """
    date_str_lower = date_str.lower()
    now = datetime.now()

    if "yesterday" in date_str_lower:
        base_date = now - timedelta(days=1)
    elif "today" in date_str_lower:
        base_date = now
    elif "tomorrow" in date_str_lower:
        base_date = now + timedelta(days=1)
    else:
        return None

    # Check for time qualifier
    if "morning" in date_str_lower or "open" in date_str_lower:
        return base_date.replace(hour=9, minute=15, second=0, microsecond=0)
    elif "close" in date_str_lower:
        return base_date.replace(hour=15, minute=30, second=0, microsecond=0)
    elif "afternoon" in date_str_lower:
        return base_date.replace(hour=13, minute=0, second=0, microsecond=0)
    else:
        # Default to market open
        return base_date.replace(hour=9, minute=15, second=0, microsecond=0)


def parse_specific_date(date_str: str) -> Optional[datetime]:
    """
    Parse specific date formats.

    Args:
        date_str: Specific date string

    Returns:
        datetime: Parsed datetime or None

    Formats:
        - "15 Oct 2024"
        - "15 Oct 2024 at 2 PM"
        - "15-10-2024"
        - "15/10/2024 14:30"
    """
    pass


def parse_time(time_str: str) -> Optional[int]:
    """
    Parse time string to hour.

    Args:
        time_str: Time string

    Returns:
        int: Hour (0-23) or None

    Examples:
        "2 PM" -> 14
        "14:30" -> 14
        "9:15" -> 9
    """
    pass


def get_market_open_time(date: datetime) -> datetime:
    """Get market opening time for given date (9:15 AM)."""
    return date.replace(hour=9, minute=15, second=0, microsecond=0)


def get_market_close_time(date: datetime) -> datetime:
    """Get market closing time for given date (3:30 PM)."""
    return date.replace(hour=15, minute=30, second=0, microsecond=0)


def is_valid_market_time(dt: datetime) -> bool:
    """
    Check if datetime is within market hours.

    Args:
        dt: Datetime to check

    Returns:
        bool: True if within market hours (9:15 AM - 3:30 PM)
    """
    market_open = get_market_open_time(dt)
    market_close = get_market_close_time(dt)
    return market_open <= dt <= market_close
