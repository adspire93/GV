"""
User Model

Represents GammaVantage users and their data.
"""

from datetime import datetime
from typing import Optional


class User:
    """
    User data model.

    Attributes:
        user_id: Unique identifier (UUID)
        phone_number: WhatsApp phone number
        subscription_tier: free_trial, basic, pro, elite
        subscription_status: active, expired, cancelled
        subscription_start: Subscription start date
        subscription_end: Subscription end date
        created_at: Account creation timestamp
        last_active: Last activity timestamp
        queries_today: Number of queries used today
        preferences: User notification preferences
    """

    def __init__(self, user_id: str, phone_number: str):
        self.user_id = user_id
        self.phone_number = phone_number
        self.subscription_tier = "free_trial"
        self.subscription_status = "active"
        self.subscription_start: Optional[datetime] = None
        self.subscription_end: Optional[datetime] = None
        self.created_at = datetime.now()
        self.last_active = datetime.now()
        self.queries_today = 0
        self.preferences = {}

    def to_dict(self) -> dict:
        """Convert user object to dictionary."""
        pass

    @staticmethod
    def from_dict(data: dict) -> 'User':
        """Create user object from dictionary."""
        pass
