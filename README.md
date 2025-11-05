# GammaVantage

**Democratize F&O trading through messaging platforms.**

GammaVantage is a conversational AI assistant that provides simple, actionable F&O trading insights to retail traders.

**Development:** Testing with Telegram
**Production:** Launching on WhatsApp

## 🎯 Vision

Reduce retail trader losses from 90% to 50% by providing accessible, professional-grade trading tools via WhatsApp.

## ✨ Features

### 1. 📊 Trade Snapshot
360-degree view of any F&O instrument in a single message
- Live quote (LTP, volume, change%)
- Futures data (price, OI, basis)
- ATM options data (CE/PE, IV, Greeks)
- Key levels (support, resistance, pivot)
- Proprietary GV Score (0-100)

### 2. 💰 On-Demand Price Lookup
Query specific contract prices (live or historical)
- Real-time prices (1-minute candles)
- Historical prices (15-minute candles)
- Natural language queries

### 3. 🔍 Market Screeners
Pre-configured technical screeners via Chartink integration
- Trend: EMA crossovers
- Candlestick: Patterns
- Volume: Unusual activity
- Momentum: RSI levels
- Breakouts: 52-week highs/lows

### 4. 🎯 What-If Trade Simulator (Flagship)
Calculate P&L for hypothetical trades using actual market data
- Define entry point (any past time)
- Calculate P&L to current price
- Support futures and options
- Handle multiple lots

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/GammaVantage.git
cd GammaVantage

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run application
python main.py
```

## 🤖 Testing with Telegram

We're using **Telegram** for initial development and testing before launching on WhatsApp.

### Why Telegram First?

✅ **Free & instant setup** - No business verification
✅ **Easy testing** - Better API, no message template restrictions
✅ **Faster iteration** - Same features, simpler development

### Set Up Your Telegram Bot

1. **Create a bot** via @BotFather on Telegram
2. **Get your bot token**
3. **Add to `.env` file:**
   ```bash
   MESSAGING_PLATFORM=telegram
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

4. **Run in polling mode** (for local testing):
   ```bash
   python scripts/telegram_polling.py
   ```

5. **Message your bot** and test all features!

**📖 Full Guide:** [Telegram Testing Guide](docs/TELEGRAM_TESTING_GUIDE.md)

**💬 Once testing is complete, switch to WhatsApp by changing `MESSAGING_PLATFORM=whatsapp` in .env**

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- InfluxDB 2.0+ (for time-series data)
- **For Testing:** Telegram bot token (free from @BotFather)
- **For Production:** WhatsApp Business API access
- Market data provider API key

## 🏗️ Architecture

```
User → Telegram/WhatsApp → Message Router → GammaVantage
  → Query Parser → Intent Classifier → Feature Service
    → Data Layer → Response Formatter → User
```

**Platform Flexibility:** Supports both Telegram (testing) and WhatsApp (production) through unified message router.

### Tech Stack

- **Backend**: Python 3.11, FastAPI
- **Database**: PostgreSQL (structured), InfluxDB (time-series)
- **Cache**: Redis
- **Queue**: Celery + RabbitMQ
- **NLU**: spaCy
- **Deployment**: Docker, Kubernetes (AWS/GCP)

## 📁 Project Structure

See [Project Structure Documentation](docs/PROJECT_STRUCTURE.md)

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test category
pytest tests/unit/
pytest tests/integration/
```

## 📊 Monitoring

- Health check: `http://localhost:8000/health`
- Metrics: `http://localhost:9090` (Prometheus)
- Dashboard: `http://localhost:3000` (Grafana)

## 🔒 Security

- All API keys in environment variables
- WhatsApp webhook signature verification
- Input validation and sanitization
- Rate limiting per user
- HTTPS only

## 📜 Compliance

- SEBI risk disclaimers on all responses
- No guaranteed returns claims
- User education integrated
- Consider RIA registration requirements

## 💰 Subscription Tiers

1. **Free Trial** (7 days): 5 queries/day, basic features
2. **Basic** (₹499/month): 50 queries/day, all features
3. **Pro** (₹999/month): Unlimited queries, priority support
4. **Elite** (₹2,499/month): Everything + consultation + API access

## 🛣️ Roadmap

### Phase 1: MVP (Weeks 1-4)
- WhatsApp integration
- Basic price lookup feature
- Deploy to staging

### Phase 2: Core Features (Weeks 5-8)
- All 4 features functional
- Query parser with NLP
- Caching layer

### Phase 3: Production (Weeks 9-12)
- Subscription system
- Payment integration
- Beta testing (50 users)

### Phase 4: Scale (Months 4-6)
- 1,000 paying users
- Marketing & referrals
- Advanced analytics

## 🎯 Success Metrics

- **Week 1**: Echo bot working
- **Month 1**: 50 beta users, 90% success rate
- **Month 3**: 100 paying users, ₹1L MRR
- **Month 12**: 1,000 paying users, ₹10L MRR, profitable

## 📚 Documentation

- [Development Guide](claude.md)
- [API Documentation](docs/API_GUIDE.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md)

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## 📝 License

[MIT License](LICENSE)

## 📧 Support

- Email: support@gammavantage.com
- WhatsApp: +91-XXXXXXXXXX
- GitHub Issues: [Report Issue](https://github.com/yourusername/GammaVantage/issues)

## ⚠️ Disclaimer

GammaVantage provides data and tools for educational purposes only. This is NOT financial advice. Trading in F&O involves substantial risk of loss. Past performance does not guarantee future results. Always consult a SEBI registered investment advisor before making trading decisions.

---

**Built with ❤️ for Indian retail traders**
