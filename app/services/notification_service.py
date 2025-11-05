"""
Notification Service

Sends proactive notifications and alerts to users.

Notification Types:
1. Market Open/Close reminders
2. Unusual market events (VIX spike, major moves)
3. Subscription expiry reminders
4. Custom price alerts (Pro/Elite users)
5. System maintenance notifications

Delivery:
- WhatsApp template messages
- Scheduled via background jobs
- User preference based (opt-in/opt-out)

Rate Limiting:
- Max 5 notifications per user per day
- No notifications during non-market hours (unless urgent)
"""

from typing import List, Dict
from datetime import datetime


class NotificationService:
    """Manages user notifications and alerts."""

    def __init__(self):
        """Initialize with WhatsApp gateway."""
        pass

    def send_market_open_reminder(self, user_ids: List[str]):
        """Send market opening reminder to users."""
        pass

    def send_subscription_expiry_reminder(self, user_id: str, days_remaining: int):
        """
        Send subscription expiry reminder.

        Args:
            user_id: User identifier
            days_remaining: Days until expiry
        """
        pass

    def send_custom_alert(self, user_id: str, alert_config: Dict, current_price: float):
        """
        Send custom price alert.

        Args:
            user_id: User identifier
            alert_config: Alert configuration
            current_price: Current price that triggered alert
        """
        pass

    def send_unusual_market_event(self, event_type: str, details: Dict):
        """
        Send notification for unusual market events.

        Event Types:
        - vix_spike: VIX increased >20%
        - major_index_move: NIFTY/BANKNIFTY moved >2%
        - circuit_breaker: Market circuit hit
        """
        pass

    def check_notification_preferences(self, user_id: str, notification_type: str) -> bool:
        """Check if user wants this notification type."""
        pass

    def check_notification_limit(self, user_id: str) -> bool:
        """Check if user hasn't exceeded daily notification limit."""
        pass
