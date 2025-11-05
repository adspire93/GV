"""
Telegram Polling Script

Run this for local testing without webhook setup.
Continuously polls Telegram for new messages and processes them.

Usage:
    python scripts/telegram_polling.py

Requirements:
    - TELEGRAM_BOT_TOKEN in .env file
    - Bot created via @BotFather

This is ideal for:
    - Local development
    - Testing without public URL
    - Debugging query parsing
    - Quick iterations
"""

import os
import time
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Run Telegram bot in polling mode."""

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN not found in .env file")
        logger.error("Please create a bot via @BotFather and add token to .env")
        return

    logger.info("Starting GammaVantage Telegram Bot in polling mode...")
    logger.info("Press Ctrl+C to stop")

    # TODO: Implement actual polling logic
    # from app.services.telegram_gateway import TelegramGateway
    # from app.services.query_parser import QueryParser
    # from app.services.intent_classifier import IntentClassifier

    # gateway = TelegramGateway(bot_token)
    # parser = QueryParser()
    # classifier = IntentClassifier()

    offset = None

    try:
        while True:
            # TODO: Get updates from Telegram
            # updates = gateway.get_updates(offset)

            # for update in updates:
            #     # Extract message
            #     message = extract_message_data(update)
            #
            #     # Parse query
            #     parsed = parser.parse(message['text'])
            #
            #     # Classify intent
            #     intent, confidence = classifier.classify(parsed)
            #
            #     # Route to appropriate service
            #     # Send response
            #
            #     # Update offset
            #     offset = update['update_id'] + 1

            logger.info("Polling for messages... (TODO: Implement)")
            time.sleep(2)

    except KeyboardInterrupt:
        logger.info("\nStopping bot...")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
