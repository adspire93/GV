# Telegram Testing Guide

## Why Telegram First?

We're using Telegram for initial testing before moving to WhatsApp Business API because:

✅ **Free & Instant Setup**
- No business verification required
- No costs for testing
- Instant bot creation via @BotFather

✅ **Easier Development**
- Simple HTTP API
- Better documentation
- No message template restrictions
- Full API access immediately

✅ **Better Testing Experience**
- Markdown support for formatted messages
- Inline keyboards for interactive menus
- Can edit messages (useful for live updates)
- Better error messages

✅ **Same User Experience**
- Test all 4 core features
- Validate query parsing
- Test response formatting
- Verify user flows

## Setting Up Telegram Bot

### Step 1: Create Your Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Follow the prompts:
   - Choose a name for your bot (e.g., "GammaVantage Test")
   - Choose a username (must end in 'bot', e.g., "gammavantage_test_bot")
4. Copy the **bot token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
5. Save this token - you'll need it!

### Step 2: Configure Your Bot

Send these commands to @BotFather:

```
/setdescription
Select your bot
Enter: "Your personal F&O trading assistant. Get live prices, trade snapshots, screeners, and P&L simulations."

/setabouttext
Select your bot
Enter: "GammaVantage - Democratizing F&O trading through conversational AI"

/setuserpic
Select your bot
Upload a profile picture (optional)
```

### Step 3: Configure Environment

Update your `.env` file:

```bash
# Messaging Platform
MESSAGING_PLATFORM=telegram  # Use 'telegram' for testing, 'whatsapp' for production

# Telegram Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_WEBHOOK_URL=https://yourdomain.com/webhook/telegram  # For production
```

### Step 4: Local Testing (Polling Mode)

For local testing without a public URL:

```python
# Run in polling mode (checks for messages periodically)
python scripts/telegram_polling.py
```

This will:
- Connect to Telegram
- Listen for messages
- Process queries
- Send responses
- No webhook setup needed

### Step 5: Production Setup (Webhook Mode)

For deployment with a public URL:

1. Deploy your application to a server with HTTPS
2. Set webhook:
   ```bash
   curl -X POST https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook \
        -d "url=https://yourdomain.com/webhook/telegram"
   ```
3. Verify webhook:
   ```bash
   curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo
   ```

## Testing Features

### 1. Trade Snapshot
```
Message to bot: NIFTY Futures
Expected: Complete snapshot with live data, futures info, options, key levels
```

### 2. Price Lookup
```
Message: What is the price of BANKNIFTY Futures?
Expected: Current price with timestamp
```

### 3. Market Screeners
```
Message: Show stocks above 210 ema
Expected: List of stocks matching criteria
```

### 4. Trade Simulator
```
Message: What if I bought NIFTY Futures yesterday?
Expected: P&L calculation with entry/exit prices
```

### 5. Help Command
```
Message: /start or help
Expected: Welcome message with feature overview
```

## Telegram-Specific Features

### Inline Keyboards (Future Enhancement)

```
User: /start
Bot: Welcome! Choose a feature:
     [📊 Snapshot] [💰 Price] [🔍 Screener] [🎯 Simulator]
```

### Quick Commands

Set up bot commands via @BotFather:
```
/setcommands
Select your bot
Enter:
start - Get started with GammaVantage
help - Show help message
snapshot - Get trade snapshot
price - Look up price
screener - View stock screeners
simulator - Simulate a trade
subscribe - View subscription plans
```

## Monitoring Telegram Bot

### Check Bot Status
```bash
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe
```

### Get Updates (Manual Testing)
```bash
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

### Clear Pending Updates
```bash
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates?offset=-1
```

## Differences: Telegram vs WhatsApp

| Feature | Telegram | WhatsApp Business |
|---------|----------|-------------------|
| **Setup** | Instant, free | Requires Meta Business verification |
| **Cost** | Free | Pay per message (₹0.125-0.88/msg) |
| **Formatting** | Full Markdown/HTML | Limited formatting |
| **Buttons** | Inline keyboards | Template buttons only |
| **Message Templates** | Not required | Required for proactive messages |
| **Testing** | Easy, instant | Requires sandbox/production setup |
| **API Complexity** | Simple HTTP API | More complex, stricter rules |

## Migration to WhatsApp

Once testing is complete on Telegram:

1. Set up WhatsApp Business Account
2. Get Meta Business verification
3. Update `.env`:
   ```bash
   MESSAGING_PLATFORM=whatsapp
   ```
4. Deploy - same code works for both platforms!

## Troubleshooting

### Bot Not Responding
- Check bot token is correct
- Verify bot is not blocked
- Check server logs for errors

### Webhook Not Working
- Ensure HTTPS (Telegram requires SSL)
- Check webhook URL is accessible
- Verify webhook is set: `getWebhookInfo`

### Message Formatting Issues
- Escape special characters: `_`, `*`, `[`, `]`, `(`, `)`, `~`, `` ` ``
- Use proper Markdown syntax
- Test formatting with simple messages first

## Sample Test Conversation

```
User: /start
Bot: 👋 Welcome to GammaVantage!
     Your personal F&O trading assistant.

     I can help you with:
     📊 Trade Snapshots (try: "NIFTY Futures")
     💰 Price Lookups (try: "BANKNIFTY 49000 CE price")
     🔍 Market Screeners (try: "stocks above 210 ema")
     🎯 Trade Simulator (try: "What if I bought RELIANCE yesterday?")

User: NIFTY Futures
Bot: [Sends formatted snapshot with live data]

User: What if I bought NIFTY yesterday?
Bot: [Sends P&L calculation]
```

## Resources

- [Telegram Bot API Docs](https://core.telegram.org/bots/api)
- [BotFather Commands](https://core.telegram.org/bots#6-botfather)
- [Telegram Bot Examples](https://core.telegram.org/bots/samples)

---

**Once Telegram testing is complete and stable, we'll migrate to WhatsApp Business API for production launch.**
