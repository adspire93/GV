"""
Subscription Model

Represents user subscription and payment data.
"""

from datetime import datetime
from typing import Optional


class Subscription:
    """User subscription details."""

    def __init__(self, subscription_id: str, user_id: str, plan: str):
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.plan = plan  # free_trial, basic, pro, elite
        self.status = "active"  # active, expired, cancelled
        self.start_date = datetime.now()
        self.end_date: Optional[datetime] = None
        self.auto_renew = False
        self.payment_method: Optional[str] = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def is_active(self) -> bool:
        """Check if subscription is currently active."""
        if self.status != "active":
            return False
        if self.end_date and datetime.now() > self.end_date:
            return False
        return True

    def days_remaining(self) -> int:
        """Calculate days remaining in subscription."""
        if not self.end_date:
            return 0
        delta = self.end_date - datetime.now()
        return max(0, delta.days)


class Payment:
    """Payment transaction record."""

    def __init__(self, payment_id: str, user_id: str, amount: float):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount
        self.currency = "INR"
        self.status = "pending"  # pending, success, failed
        self.transaction_id: Optional[str] = None
        self.payment_method: Optional[str] = None
        self.plan: Optional[str] = None
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
