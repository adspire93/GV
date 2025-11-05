"""
Disclaimer Manager

Manages regulatory disclaimers and risk warnings.

SEBI Compliance Requirements:
- Every market data response must include risk disclaimer
- No guaranteed returns language
- Clear "not financial advice" statement
- User education about market risks
"""

from typing import List


# Standard Disclaimers
STANDARD_DISCLAIMER = "⚠️ _Invest at your own risk. Not financial advice._"

DETAILED_DISCLAIMER = """
⚠️ *Risk Disclosure*

Markets are subject to risk. Past performance does not guarantee future results.
This is for educational purposes only, not investment advice.
Consult a SEBI registered advisor before trading.

GammaVantage provides data and tools, not recommendations.
"""

SIMULATOR_DISCLAIMER = """
⚠️ *Note:*
- Hypothetical simulation only
- Does not include brokerage, taxes, and slippage
- Actual results may vary significantly
- Past performance ≠ future results
"""

SUBSCRIPTION_DISCLAIMER = """
⚠️ *Important:*
- No guaranteed profits
- Market risks apply
- Service provides data, not advice
- Refund policy: Check terms
"""


def get_standard_disclaimer() -> str:
    """Get standard short disclaimer for all responses."""
    return STANDARD_DISCLAIMER


def get_detailed_disclaimer() -> str:
    """Get detailed risk disclosure."""
    return DETAILED_DISCLAIMER


def get_simulator_disclaimer() -> str:
    """Get disclaimer for trade simulator."""
    return SIMULATOR_DISCLAIMER


def get_subscription_disclaimer() -> str:
    """Get disclaimer for subscription messaging."""
    return SUBSCRIPTION_DISCLAIMER


def get_onboarding_disclosure() -> str:
    """
    Get comprehensive disclosure for user onboarding.

    Returns:
        str: Full disclosure message
    """
    return """
⚠️ *Risk Disclosure & Terms*

*Market Risks:*
• 90%+ F&O traders lose money
• You may lose entire capital
• Past data ≠ future results

*Service Scope:*
• We provide data & tools only
• NOT investment recommendations
• NOT SEBI registered advisors

*Your Responsibility:*
• Make your own decisions
• Understand risks before trading
• Consult certified advisors

By continuing, you acknowledge:
✓ You understand market risks
✓ You trade at your own risk
✓ GammaVantage is not liable for losses

Type *AGREE* to continue or *CANCEL* to stop.
"""


def add_disclaimer(message: str, disclaimer_type: str = "standard") -> str:
    """
    Add appropriate disclaimer to message.

    Args:
        message: Original message
        disclaimer_type: "standard", "detailed", "simulator", "subscription"

    Returns:
        str: Message with disclaimer appended
    """
    disclaimers = {
        "standard": STANDARD_DISCLAIMER,
        "detailed": DETAILED_DISCLAIMER,
        "simulator": SIMULATOR_DISCLAIMER,
        "subscription": SUBSCRIPTION_DISCLAIMER
    }

    disclaimer = disclaimers.get(disclaimer_type, STANDARD_DISCLAIMER)
    return f"{message}\n\n{disclaimer}"


def get_educational_content() -> List[str]:
    """
    Get educational content about F&O trading risks.

    Returns:
        List[str]: List of educational messages
    """
    return [
        "💡 *Tip:* Always use stop-loss to limit downside risk.",
        "💡 *Tip:* Never risk more than 2% of capital in a single trade.",
        "💡 *Tip:* Options lose value over time (theta decay).",
        "💡 *Tip:* High IV = expensive options. Consider selling instead.",
        "💡 *Tip:* Check OI buildup for institutional interest.",
    ]
