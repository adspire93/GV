"""
Telegram Gateway Service

Handles sending and receiving Telegram messages.
Manages bot interactions and message formatting.

Advantages over WhatsApp for Testing:
- Free and instant bot creation via @BotFather
- No business verification required
- Full API access immediately
- Better markdown support
- Inline keyboards for interactive menus
- No message template restrictions

Telegram Bot API Documentation:
https://core.telegram.org/bots/api

Responsibilities:
- Send formatted messages to users
- Receive and parse incoming messages
- Handle inline keyboards and buttons
- Manage chat sessions
- Format responses with Telegram markdown

Telegram Markdown Support:
- *bold text*
- _italic text_
- `code`
- ```code block```
- [inline URL](http://www.example.com/)
- Emojis (📊, 💰, 🎯, etc.)
"""

from typing import Optional, Dict, List
import requests


class TelegramGateway:
    """Manages Telegram Bot API communication."""

    def __init__(self, bot_token: str):
        """
        Initialize Telegram bot client.

        Args:
            bot_token: Telegram bot token from @BotFather

        To create a bot:
        1. Message @BotFather on Telegram
        2. Send /newbot
        3. Follow instructions
        4. Copy the bot token
        """
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, chat_id: int, message: str,
                    parse_mode: str = "Markdown") -> bool:
        """
        Send message to user.

        Args:
            chat_id: Telegram chat ID
            message: Message text (supports Markdown)
            parse_mode: "Markdown" or "HTML"

        Returns:
            bool: True if sent successfully

        Example:
            gateway.send_message(123456789, "*Hello!* Welcome to GammaVantage")
        """
        pass

    def send_message_with_keyboard(self, chat_id: int, message: str,
                                   keyboard: List[List[Dict]]) -> bool:
        """
        Send message with inline keyboard buttons.

        Args:
            chat_id: Telegram chat ID
            message: Message text
            keyboard: Inline keyboard layout

        Example:
            keyboard = [
                [{"text": "📊 Snapshot", "callback_data": "feature_snapshot"}],
                [{"text": "💰 Price Lookup", "callback_data": "feature_price"}],
                [{"text": "🔍 Screeners", "callback_data": "feature_screener"}]
            ]
        """
        pass

    def send_photo(self, chat_id: int, photo_url: str, caption: str = "") -> bool:
        """
        Send photo (useful for charts/graphs later).

        Args:
            chat_id: Telegram chat ID
            photo_url: URL or file_id of photo
            caption: Photo caption

        Returns:
            bool: True if sent successfully
        """
        pass

    def edit_message(self, chat_id: int, message_id: int, new_text: str) -> bool:
        """
        Edit previously sent message.

        Args:
            chat_id: Telegram chat ID
            message_id: Message ID to edit
            new_text: New message text

        Returns:
            bool: True if edited successfully

        Useful for:
        - Updating live prices
        - Showing loading states
        """
        pass

    def send_typing_action(self, chat_id: int):
        """
        Show typing indicator.

        Args:
            chat_id: Telegram chat ID

        Shows "typing..." indicator to user while processing.
        """
        pass

    def get_updates(self, offset: Optional[int] = None) -> List[Dict]:
        """
        Get updates (polling mode - for local testing).

        Args:
            offset: Update ID to start from

        Returns:
            List of update objects

        Note: Use webhook for production, polling for local testing
        """
        pass

    def answer_callback_query(self, callback_query_id: str, text: str = ""):
        """
        Answer callback query from inline keyboard.

        Args:
            callback_query_id: Callback query ID
            text: Optional notification text

        Required after user clicks inline keyboard button.
        """
        pass

    def get_bot_info(self) -> Dict:
        """
        Get bot information.

        Returns:
            dict: Bot username, name, etc.

        Useful for verifying bot token is valid.
        """
        pass

    def format_for_telegram(self, message: str) -> str:
        """
        Convert WhatsApp-style formatting to Telegram markdown.

        Args:
            message: Message with WhatsApp formatting

        Returns:
            str: Message with Telegram markdown

        Note: Both use similar markdown, but this allows for adjustments
        """
        # WhatsApp and Telegram use similar markdown
        # May need minor adjustments for compatibility
        return message
