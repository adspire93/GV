"""
Telegram Bot Setup Script

Sets up Telegram bot with commands and webhook.

Usage:
    # Set up commands only
    python scripts/setup_telegram_bot.py --commands

    # Set up webhook
    python scripts/setup_telegram_bot.py --webhook https://yourdomain.com/webhook/telegram

    # Get bot info
    python scripts/setup_telegram_bot.py --info
"""

import os
import sys
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()


def get_bot_info(bot_token):
    """Get bot information."""
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            bot = data['result']
            print("\n✅ Bot Information:")
            print(f"   Name: {bot.get('first_name')}")
            print(f"   Username: @{bot.get('username')}")
            print(f"   Bot ID: {bot.get('id')}")
            print(f"   Can Join Groups: {bot.get('can_join_groups')}")
            return True

    print("❌ Failed to get bot info")
    return False


def setup_commands(bot_token):
    """Set up bot commands menu."""
    url = f"https://api.telegram.org/bot{bot_token}/setMyCommands"

    commands = [
        {"command": "start", "description": "Get started with GammaVantage"},
        {"command": "help", "description": "Show help message"},
        {"command": "snapshot", "description": "Get trade snapshot"},
        {"command": "price", "description": "Look up price"},
        {"command": "screener", "description": "View stock screeners"},
        {"command": "simulator", "description": "Simulate a trade"},
        {"command": "subscribe", "description": "View subscription plans"},
    ]

    response = requests.post(url, json={"commands": commands})

    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            print("\n✅ Commands set up successfully!")
            print("   Users will see these commands in the bot menu")
            return True

    print("❌ Failed to set up commands")
    return False


def setup_webhook(bot_token, webhook_url):
    """Set up webhook URL."""
    url = f"https://api.telegram.org/bot{bot_token}/setWebhook"

    response = requests.post(url, json={"url": webhook_url})

    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            print(f"\n✅ Webhook set up successfully!")
            print(f"   URL: {webhook_url}")
            return True

    print("❌ Failed to set up webhook")
    return False


def get_webhook_info(bot_token):
    """Get current webhook information."""
    url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            info = data['result']
            print("\n📋 Webhook Information:")
            print(f"   URL: {info.get('url', 'Not set')}")
            print(f"   Pending Updates: {info.get('pending_update_count', 0)}")
            if info.get('last_error_date'):
                print(f"   Last Error: {info.get('last_error_message')}")
            return True

    print("❌ Failed to get webhook info")
    return False


def delete_webhook(bot_token):
    """Delete webhook (switch to polling mode)."""
    url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook"
    response = requests.post(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            print("\n✅ Webhook deleted successfully!")
            print("   Bot is now in polling mode")
            return True

    print("❌ Failed to delete webhook")
    return False


def main():
    parser = argparse.ArgumentParser(description="Set up Telegram bot")
    parser.add_argument("--info", action="store_true", help="Get bot information")
    parser.add_argument("--commands", action="store_true", help="Set up bot commands")
    parser.add_argument("--webhook", type=str, help="Set up webhook URL")
    parser.add_argument("--webhook-info", action="store_true", help="Get webhook info")
    parser.add_argument("--delete-webhook", action="store_true", help="Delete webhook")

    args = parser.parse_args()

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token:
        print("❌ Error: TELEGRAM_BOT_TOKEN not found in .env file")
        print("\nTo create a bot:")
        print("1. Message @BotFather on Telegram")
        print("2. Send /newbot")
        print("3. Follow instructions")
        print("4. Copy bot token to .env file")
        sys.exit(1)

    # Default: show info
    if not any([args.info, args.commands, args.webhook, args.webhook_info, args.delete_webhook]):
        args.info = True

    if args.info:
        get_bot_info(bot_token)

    if args.commands:
        setup_commands(bot_token)

    if args.webhook:
        setup_webhook(bot_token, args.webhook)

    if args.webhook_info:
        get_webhook_info(bot_token)

    if args.delete_webhook:
        delete_webhook(bot_token)


if __name__ == "__main__":
    main()
