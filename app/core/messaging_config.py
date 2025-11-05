"""
Messaging Platform Configuration

Manages configuration for both Telegram (testing) and WhatsApp (production).
Allows easy switching between platforms.

Development/Testing: Use Telegram
- Free and instant setup
- No business verification
- Better for rapid iteration

Production: Use WhatsApp
- Wider reach in India
- Better for business communication
- Professional appearance
"""

import os
from enum import Enum
from typing import Optional


class MessagingPlatform(Enum):
    """Supported messaging platforms."""
    TELEGRAM = "telegram"
    WHATSAPP = "whatsapp"


class MessagingConfig:
    """Configuration for messaging platforms."""

    def __init__(self):
        # Active platform (set via environment variable)
        self.active_platform = MessagingPlatform(
            os.getenv("MESSAGING_PLATFORM", "telegram")
        )

        # Telegram Configuration
        self.telegram_bot_token: Optional[str] = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_webhook_url: Optional[str] = os.getenv("TELEGRAM_WEBHOOK_URL")

        # WhatsApp Configuration
        self.whatsapp_api_key: Optional[str] = os.getenv("WHATSAPP_API_KEY")
        self.whatsapp_phone_number_id: Optional[str] = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
        self.whatsapp_verify_token: Optional[str] = os.getenv("WHATSAPP_VERIFY_TOKEN")

    def is_telegram_active(self) -> bool:
        """Check if Telegram is the active platform."""
        return self.active_platform == MessagingPlatform.TELEGRAM

    def is_whatsapp_active(self) -> bool:
        """Check if WhatsApp is the active platform."""
        return self.active_platform == MessagingPlatform.WHATSAPP

    def get_active_platform_name(self) -> str:
        """Get name of active platform."""
        return self.active_platform.value

    def validate_config(self) -> bool:
        """
        Validate that required configuration is present for active platform.

        Returns:
            bool: True if valid, False otherwise
        """
        if self.is_telegram_active():
            return bool(self.telegram_bot_token)
        elif self.is_whatsapp_active():
            return bool(self.whatsapp_api_key and self.whatsapp_phone_number_id)
        return False


# Global configuration instance
messaging_config = MessagingConfig()
