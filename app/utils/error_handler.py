"""
Error Handler

Centralized error handling and user-friendly error messages.

Principles:
1. Never leave user hanging - always respond
2. Be specific about the error
3. Offer alternatives or solutions
4. Log all errors for debugging
5. No technical jargon in user messages
"""

from typing import Optional, Dict
import logging


logger = logging.getLogger(__name__)


class GammaVantageError(Exception):
    """Base exception for GammaVantage errors."""
    pass


class DataNotAvailableError(GammaVantageError):
    """Raised when market data is not available."""
    pass


class InvalidQueryError(GammaVantageError):
    """Raised when user query is invalid or cannot be parsed."""
    pass


class SubscriptionError(GammaVantageError):
    """Raised when user doesn't have access to feature."""
    pass


class RateLimitError(GammaVantageError):
    """Raised when user exceeds rate limit."""
    pass


def handle_error(error: Exception, context: Optional[Dict] = None) -> str:
    """
    Handle error and return user-friendly message.

    Args:
        error: Exception that occurred
        context: Additional context (query, user_id, etc.)

    Returns:
        str: User-friendly error message
    """
    # Log error with context
    logger.error(f"Error occurred: {str(error)}", extra=context)

    # Generate user-friendly message based on error type
    if isinstance(error, DataNotAvailableError):
        return format_data_unavailable_error(str(error))
    elif isinstance(error, InvalidQueryError):
        return format_invalid_query_error(str(error))
    elif isinstance(error, SubscriptionError):
        return format_subscription_error(str(error))
    elif isinstance(error, RateLimitError):
        return format_rate_limit_error()
    else:
        return format_generic_error()


def format_data_unavailable_error(details: str) -> str:
    """Format error when data is not available."""
    return f"""
❌ *Data Unavailable*

{details}

*Possible reasons:*
• Market is closed
• Contract doesn't exist
• Data provider issue

💡 *Try:*
• Check symbol spelling
• Try a different instrument
• Query during market hours (9:15 AM - 3:30 PM)

Need help? Type *help*
"""


def format_invalid_query_error(details: str) -> str:
    """Format error for invalid query."""
    return f"""
❓ *Couldn't Understand*

{details}

💡 *Examples:*
• NIFTY Futures
• BANKNIFTY 49500 PE price
• What if I bought NIFTY yesterday?
• Show stocks above 210 ema

Type *help* to see all features.
"""


def format_subscription_error(details: str) -> str:
    """Format error when user doesn't have access."""
    return f"""
🔒 *Premium Feature*

{details}

This feature is available for *Basic* plan and above.

💎 *Upgrade Benefits:*
• Unlimited queries
• All features unlocked
• Priority support

Type *subscribe* to view plans.
"""


def format_rate_limit_error() -> str:
    """Format error when rate limit exceeded."""
    return """
⏰ *Rate Limit Reached*

You've reached the maximum queries for this minute.

Please wait a moment and try again.

💡 *Upgrade to Pro* for higher limits!
Type *subscribe* to view plans.
"""


def format_generic_error() -> str:
    """Format generic error message."""
    return """
😓 *Oops! Something went wrong*

We're experiencing a temporary issue.
Our team has been notified.

Please try again in a moment.

If the problem persists, contact support.
"""


def suggest_alternatives(instrument: str) -> str:
    """Suggest alternative instruments if one not found."""
    return f"""
❌ *Not Found:* {instrument}

💡 *Did you mean?*
• NIFTY
• BANKNIFTY
• FINNIFTY
• RELIANCE
• TCS
• INFY

Or check spelling and try again.
"""
