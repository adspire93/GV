"""
WhatsApp Gateway Service

Handles sending and receiving WhatsApp messages.
Manages session state and conversation flow.

Responsibilities:
- Send formatted messages to users
- Receive and parse incoming messages
- Manage user session state
- Handle message delivery status
- Format responses with proper WhatsApp markdown

WhatsApp Message Format Support:
- *Bold text*
- _Italic text_
- Emojis (📊, 💰, 🎯, etc.)
- Line breaks
- Bullet points

Performance:
- Message delivery: < 500ms
- Handle concurrent sends
- Queue messages if rate limited
"""

from typing import Optional, Dict


class WhatsAppGateway:
    """Manages WhatsApp Business API communication."""

    def __init__(self):
        """Initialize WhatsApp API client."""
        pass

    def send_message(self, phone_number: str, message: str) -> bool:
        """
        Send WhatsApp message to user.

        Args:
            phone_number: User's WhatsApp number
            message: Formatted message text

        Returns:
            bool: True if sent successfully, False otherwise
        """
        pass

    def send_template_message(self, phone_number: str, template_name: str, params: dict) -> bool:
        """
        Send WhatsApp template message (for notifications).

        Args:
            phone_number: User's WhatsApp number
            template_name: Pre-approved template name
            params: Template parameters

        Returns:
            bool: True if sent successfully, False otherwise
        """
        pass

    def parse_incoming_message(self, webhook_data: dict) -> Optional[Dict]:
        """
        Parse incoming WhatsApp message from webhook.

        Args:
            webhook_data: Raw webhook payload

        Returns:
            dict: Parsed message with user_id, text, timestamp
                  None if invalid message
        """
        pass

    def mark_as_read(self, message_id: str):
        """
        Mark message as read.

        Args:
            message_id: WhatsApp message ID
        """
        pass

    def send_typing_indicator(self, phone_number: str):
        """
        Show typing indicator to user.

        Args:
            phone_number: User's WhatsApp number
        """
        pass
