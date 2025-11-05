"""
Message Router Service

Routes messages to appropriate gateway (Telegram or WhatsApp) based on configuration.
Provides unified interface for sending messages regardless of platform.

This abstraction allows:
- Testing with Telegram
- Production with WhatsApp
- Easy platform switching
- Same business logic for both platforms
"""

from typing import Optional
from app.core.messaging_config import messaging_config, MessagingPlatform


class MessageRouter:
    """Routes messages to appropriate platform."""

    def __init__(self):
        """Initialize with appropriate gateway based on configuration."""
        self.platform = messaging_config.active_platform
        self.gateway = None

        if messaging_config.is_telegram_active():
            from app.services.telegram_gateway import TelegramGateway
            self.gateway = TelegramGateway(messaging_config.telegram_bot_token)
        elif messaging_config.is_whatsapp_active():
            from app.services.whatsapp_gateway import WhatsAppGateway
            self.gateway = WhatsAppGateway()

    def send_message(self, user_identifier: str, message: str) -> bool:
        """
        Send message through active platform.

        Args:
            user_identifier: Phone number (WhatsApp) or chat_id (Telegram)
            message: Formatted message text

        Returns:
            bool: True if sent successfully
        """
        if not self.gateway:
            return False

        if self.platform == MessagingPlatform.TELEGRAM:
            # Convert to integer for Telegram chat_id
            chat_id = int(user_identifier)
            return self.gateway.send_message(chat_id, message)
        elif self.platform == MessagingPlatform.WHATSAPP:
            return self.gateway.send_message(user_identifier, message)

        return False

    def send_typing_indicator(self, user_identifier: str):
        """
        Show typing indicator.

        Args:
            user_identifier: Phone number or chat_id
        """
        if not self.gateway:
            return

        if self.platform == MessagingPlatform.TELEGRAM:
            chat_id = int(user_identifier)
            self.gateway.send_typing_action(chat_id)
        elif self.platform == MessagingPlatform.WHATSAPP:
            self.gateway.send_typing_indicator(user_identifier)

    def format_message(self, message: str) -> str:
        """
        Format message for active platform.

        Args:
            message: Message with standard formatting

        Returns:
            str: Platform-specific formatted message
        """
        if self.platform == MessagingPlatform.TELEGRAM:
            return self.gateway.format_for_telegram(message)
        return message

    def get_platform_name(self) -> str:
        """Get active platform name."""
        return self.platform.value
