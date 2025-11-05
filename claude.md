# GammaVantage Development Guide

## Project Overview

**Product Name:** GammaVantage  
**Vision:** Democratize F&O trading by providing simple, actionable insights via WhatsApp, reducing retail trader losses from 90% to 50%  
**Platform:** WhatsApp Business API Conversational Chatbot  
**Target:** 1,000 paying subscribers within 12 months

## Core Problem Statement

90% of retail traders lose money in F&O markets due to:
- Information overload and complexity
- Lack of accessible professional tools
- Fragmented workflow across multiple apps
- Trading on speculation rather than data-driven analysis

## Target Users

- **Primary:** Aspiring retail traders (novice investors, time-constrained professionals, homemakers, tech-savvy seniors)
- **Demographics:** Need simple, trustworthy data access without complexity of professional terminals
- **Behavior:** Prefer mobile-first, conversational interfaces

## Critical Constraints & Considerations

### Regulatory Environment
- SEBI regulations tightened (Nov 2024): 3x contract sizes, eliminated daily expiries
- Market size: 3.36M active F&O traders (down from 5.26M peak)
- 91% loss rate in FY 2024-25 (₹1.05 lakh crore total losses)
- **MUST implement:** Risk warnings, disclaimers, investor education
- **Consider:** SEBI Registered Investment Advisor (RIA) license requirements

### Economic Constraints
- **WhatsApp Business API Costs:** Marketing (₹0.88/msg), Utility (₹0.125/msg), Auth (₹0.125/msg)
- **Projected messaging cost:** ₹4.5-6 lakhs/month for 1,000 users
- **Data costs:** ₹50k-2L/month for real-time NSE/BSE feeds
- **Infrastructure:** ₹30k-1L/month
- **Break-even:** ~1,450 paying users at ₹999/month

### Technical Requirements
- **Latency:** <1 second for live prices, <2 seconds for queries
- **Uptime:** 99.9% during market hours
- **Data accuracy:** 99.5% guarantee
- **Scale:** Support 1M+ daily requests at maturity

## Product Features (All P1 for Launch)

### Feature 1: Trade Snapshot
**Purpose:** 360-degree view of any F&O symbol in single WhatsApp message

**Components:**
- Live Quote (LTP, volume, change%)
- Futures Data (price, OI, basis)
- ATM Options Data (CE/PE prices, IV, Greeks)
- Key Levels (support, resistance, pivot)
- GV Score (proprietary 0-100 rating)

**User Triggers:**
- Simple instrument name: `NIFTY Futures`, `RELIANCE Opt`, `GOLD`
- Natural language variations accepted

**Technical Requirements:**
- Aggregate data from multiple sources
- Format into readable WhatsApp message
- Cache for 1-minute to reduce API calls
- Include timestamp and disclaimers

### Feature 2: On-Demand Price Lookup
**Purpose:** Query specific contract prices (live or historical)

**Capabilities:**
- **Live:** 1-minute candle data
- **Historical:** 15-minute candle data
- Support futures and options contracts
- Handle natural language queries

**Example Queries:**
- `What is the live price of NIFTY Futures?`
- `BANKNIFTY 49500 PE price on 15 Oct 2024 at 2:00 PM`
- `RELIANCE 2900 CE LTP now`

**Technical Requirements:**
- Parse natural language to extract: instrument, strike, expiry, date/time
- Query appropriate data source (real-time vs historical)
- Handle edge cases (market closed, invalid contract, data unavailable)
- Return formatted price with context

### Feature 3: Market Screeners
**Purpose:** Discover opportunities via pre-configured technical screeners

**Integration:** 
- Chartink.com webhook integration
- Pre-configured screener list (15 screeners)
- Real-time data ingestion

**Screener Categories:**
1. **Trend:** Stocks above/below EMAs (210, 21)
2. **Candlestick:** Open=High/Low patterns, Engulfing
3. **Volume:** Unusual volume alerts
4. **Momentum:** RSI overbought/oversold
5. **Breakouts:** 52-week high/low, Golden Cross
6. **Support/Resistance:** Near pivot points

**User Queries:**
- `Show me stocks above 210 ema on daily basis`
- `Any open low stocks today?`
- `List screeners` (shows all available)

**Technical Requirements:**
- Webhook receiver for Chartink data
- Store latest screener results in database
- Cache results (refresh every 15 minutes during market hours)
- Format results as ranked list with key metrics

### Feature 4: What-If Trade Simulator
**Purpose:** Calculate P&L for hypothetical trades (flagship feature)

**Functionality:**
- Define entry point (past date/time)
- Assume exit point = NOW
- Calculate P&L with actual market data
- Support futures and options
- Handle multiple lots

**Example Queries:**
- `What if I bought NIFTY Futures today morning, what is my P&L?`
- `P&L if I shorted 2 lots of BANKNIFTY Fut yesterday at the open`
- `If I bought RELIANCE 2900 CE yesterday, what's the result?`

**Technical Requirements:**
- Parse: instrument, action (buy/sell), quantity (lots), entry time
- Fetch historical entry price
- Fetch current exit price
- Calculate P&L considering lot sizes
- Display: Entry price, Exit price, Points gained/lost, Absolute P&L, ROI%
- Include disclaimer about brokerage/taxes not included

## Technical Architecture

### Data Layer
**Required Data Sources:**
1. **Real-time Market Data**
   - NSE/BSE authorized data vendors
   - WebSocket for live feeds
   - API for on-demand queries
   - Latency: <500ms

2. **Historical Data**
   - OHLCV data (15-min candles)
   - Options chain snapshots
   - OI data
   - Storage: TimeSeries DB (InfluxDB/TimescaleDB)

3. **Screener Data**
   - Chartink webhook integration
   - Store in PostgreSQL
   - Update frequency: 15 minutes

**Data Provider Options:**
- TrueData API
- Zerodha Kite Connect
- Upstox API
- IIFL Markets API

### Application Layer

**Tech Stack:**
```
Backend: Python 3.11+
Framework: FastAPI
WhatsApp: Twilio/MessageBird/360Dialog API
Database: PostgreSQL (structured), InfluxDB (time-series)
Cache: Redis
Queue: Celery + RabbitMQ
NLU: spaCy/transformers for query parsing
Deployment: Docker + Kubernetes (AWS/GCP)
```

**Core Services:**
1. **WhatsApp Gateway Service**
   - Handle incoming messages
   - Send formatted responses
   - Manage session state
   - Rate limiting

2. **Query Parser Service**
   - NLP for intent classification
   - Entity extraction (instrument, strike, date, etc.)
   - Query validation

3. **Data Retrieval Service**
   - Fetch from appropriate data source
   - Handle caching
   - Fallback mechanisms

4. **Trade Simulator Service**
   - P&L calculations
   - Historical data lookup
   - Lot size handling

5. **Screener Service**
   - Webhook receiver
   - Data processing
   - Result formatting

6. **GV Score Calculator**
   - Proprietary scoring algorithm
   - Combine multiple indicators
   - Real-time computation

### Message Flow Architecture

```
User → WhatsApp → WhatsApp Business API → Webhook
  → Gateway Service → Query Parser → Intent Router
    → Feature Service (Snapshot/Price/Screener/Simulator)
      → Data Layer → Response Formatter → WhatsApp → User
```

### Database Schema (Key Tables)

```sql
-- Users
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    phone_number VARCHAR(15) UNIQUE,
    subscription_tier VARCHAR(20),
    created_at TIMESTAMP,
    last_active TIMESTAMP
);

-- Query Log
CREATE TABLE query_log (
    query_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    query_text TEXT,
    intent VARCHAR(50),
    response_time_ms INTEGER,
    success BOOLEAN,
    created_at TIMESTAMP
);

-- Screener Results
CREATE TABLE screener_results (
    screener_id VARCHAR(50),
    symbol VARCHAR(20),
    timestamp TIMESTAMP,
    metrics JSONB,
    PRIMARY KEY (screener_id, symbol, timestamp)
);

-- Market Data (Time-series DB)
-- Use InfluxDB for OHLCV data
```

## Development Phases

### Phase 1: MVP Foundation (Weeks 1-4)
**Goal:** Basic WhatsApp integration + one feature working

**Tasks:**
1. Setup development environment
2. WhatsApp Business API integration (sandbox)
3. Basic message handling (echo bot)
4. Implement Feature 2 (Price Lookup) - simplest to start
5. Connect to free/demo data source
6. Deploy to staging environment

**Success Criteria:**
- Can query live NIFTY price via WhatsApp
- Response time <3 seconds
- Works 95% of the time

### Phase 2: Core Features (Weeks 5-8)
**Goal:** All 4 features functional

**Tasks:**
1. Implement Feature 1 (Trade Snapshot)
2. Implement Feature 3 (Screeners) with Chartink
3. Implement Feature 4 (What-If Simulator)
4. Build query parser with intent classification
5. Add caching layer
6. Error handling and user feedback

**Success Criteria:**
- All features respond correctly
- 95%+ query success rate
- User can navigate between features

### Phase 3: Production Readiness (Weeks 9-12)
**Goal:** Scalable, compliant, monetizable

**Tasks:**
1. Subscription tier implementation
2. Payment gateway integration
3. User onboarding flow
4. Risk disclaimers and compliance
5. Performance optimization
6. Monitoring and alerting
7. Beta user testing (50 users)

**Success Criteria:**
- Can handle 100 concurrent users
- Payment flow works end-to-end
- All regulatory requirements met
- Beta user satisfaction >80%

### Phase 4: Scale & Iterate (Months 4-6)
**Goal:** 1,000 paying users

**Tasks:**
1. Marketing integration
2. Referral system
3. Advanced analytics
4. Feature enhancements based on feedback
5. Infrastructure scaling
6. Customer support system

## Development Guidelines

### Code Organization
```
gammaVantage/
├── app/
│   ├── api/
│   │   ├── whatsapp_webhook.py
│   │   ├── health.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   ├── services/
│   │   ├── query_parser.py
│   │   ├── data_fetcher.py
│   │   ├── trade_simulator.py
│   │   ├── screener.py
│   │   ├── snapshot.py
│   ├── models/
│   │   ├── user.py
│   │   ├── query.py
│   ├── utils/
│   │   ├── formatters.py
│   │   ├── validators.py
├── tests/
├── deployment/
│   ├── docker-compose.yml
│   ├── k8s/
├── scripts/
├── requirements.txt
├── README.md
```

### Coding Standards
- **Python:** PEP 8 compliant, type hints, docstrings
- **Testing:** 80%+ coverage, pytest framework
- **Logging:** Structured logging (JSON), include trace_id
- **Error Handling:** Never crash, always respond gracefully
- **Security:** Validate all inputs, sanitize outputs, use env vars for secrets

### Response Formatting Standards

**Trade Snapshot Example:**
```
📊 *NIFTY Futures Snapshot*
_Updated: 05-Nov-2025 14:30 IST_

💹 *Live Quote*
Price: ₹19,850.50 | Chg: +125.30 (+0.63%)
Volume: 15.2L | OI: 8.5L

📈 *Futures (Nov)*
LTP: ₹19,865 | Basis: +14.50
OI: 1.2Cr | OI Chg: +2.5%

🎯 *ATM Options (19,850 Strike)*
CE: ₹185 | IV: 18.5% | Δ: 0.52
PE: ₹162 | IV: 17.8% | Δ: -0.48

🎚️ *Key Levels*
Res: 19,950 | 20,100
Sup: 19,750 | 19,600
Pivot: 19,825

⭐ *GV Score: 72/100* (Bullish)

⚠️ _Invest at your own risk. Not financial advice._
```

### Query Parser Logic

**Intent Classification:**
- Snapshot: Contains instrument name only
- Price: Contains "price", "LTP", time references
- Screener: Contains "stocks", "list", "show", screener names
- Simulator: Contains "what if", "P&L", "profit", hypothetical language

**Entity Extraction:**
- Instrument: NIFTY, BANKNIFTY, stock names
- Strike: Numeric value near instrument name
- Option Type: CE, PE, Call, Put
- Date/Time: "yesterday", "today morning", "15 Oct 2024 at 2 PM"
- Action: buy, sell, short, long
- Quantity: "2 lots", "5", numeric prefix

### Error Handling Principles

1. **Always respond:** Never leave user hanging
2. **Be specific:** "RELIANCE data unavailable" not "Error occurred"
3. **Offer alternatives:** "RELIANCE closed. Try NIFTY or BANKNIFTY?"
4. **Log everything:** Every error logged with context for debugging
5. **Graceful degradation:** If live data fails, offer historical

**Example Error Responses:**
```
❌ *Oops!* I couldn't find data for "RELIANC".
Did you mean *RELIANCE*?

💡 *Tip:* Use full names like NIFTY, BANKNIFTY, or TCS
```

### Performance Optimization

1. **Caching Strategy:**
   - Live prices: 1 minute cache
   - Historical data: 1 hour cache
   - Screener results: 15 minute cache
   - Trade snapshots: 30 second cache

2. **Database Queries:**
   - Use connection pooling
   - Index frequently queried fields
   - Batch operations where possible

3. **API Rate Limiting:**
   - User-level: 10 queries/minute
   - Global: 1000 queries/minute
   - Implement queue for excess requests

### Security Checklist

- [ ] All API keys in environment variables
- [ ] WhatsApp signature verification on webhook
- [ ] Input validation and sanitization
- [ ] Rate limiting per user
- [ ] SQL injection prevention (use ORMs)
- [ ] No sensitive data in logs
- [ ] HTTPS only for all endpoints
- [ ] User authentication for paid features
- [ ] Data encryption at rest and in transit

### Compliance Requirements

**Every response MUST include:**
1. Timestamp of data
2. Disclaimer: "Not financial advice. Invest at your own risk."
3. Source attribution for data

**Onboarding MUST include:**
1. Risk disclosure acknowledgment
2. Understanding of market risks
3. No guaranteed returns message
4. User age verification (18+)

### Monitoring & Alerting

**Key Metrics to Track:**
1. Query success rate (target: >95%)
2. Response time (p50, p95, p99)
3. API uptime (target: 99.9%)
4. Error rate by type
5. User engagement (queries per user per day)
6. Conversion rate (free to paid)
7. Churn rate

**Alerts:**
- Success rate drops below 90%
- Response time >3 seconds for 5+ minutes
- API down for >1 minute
- Error rate spike (>10% of requests)
- Data source unavailable

### Testing Strategy

**Unit Tests:**
- Query parser accuracy (>95% on test set)
- Data formatter correctness
- P&L calculation precision
- All utility functions

**Integration Tests:**
- WhatsApp webhook flow end-to-end
- Data source connectivity
- Database operations
- Cache behavior

**Load Tests:**
- 100 concurrent users
- 1000 requests/minute
- Sustained load for 1 hour

**User Acceptance Tests:**
- All 90 example queries work correctly
- Natural language variations handled
- Error scenarios tested

## Critical Success Factors

### Technical Excellence
- Sub-2-second response times
- 99.9% uptime during market hours
- Accurate data (99.5%+ accuracy)
- Handles 1000+ concurrent users

### User Experience
- Zero-learning-curve (WhatsApp familiar)
- Conversational and helpful
- Clear, formatted responses
- Proactive error recovery

### Business Viability
- Unit economics positive at 1,000 users
- Messaging costs <30% of revenue
- Data costs <20% of revenue
- Path to profitability clear

### Regulatory Compliance
- All risk disclosures present
- No guaranteed returns claims
- Proper disclaimers
- User education integrated

## Risk Mitigation

### Technical Risks
| Risk | Mitigation |
|------|------------|
| Data source downtime | Multiple redundant providers |
| WhatsApp API changes | Abstraction layer, monitoring |
| Scaling issues | Cloud auto-scaling, load testing |
| Security breach | Security audit, penetration testing |

### Business Risks
| Risk | Mitigation |
|------|------------|
| High messaging costs | Optimize message count, batching |
| Low conversion rate | Free trial, referral incentives |
| Regulatory shutdown | Legal consultation, compliance-first |
| Competition | Focus on UX, proprietary GV Score |

### Market Risks
| Risk | Mitigation |
|------|------------|
| Shrinking F&O market | Diversify to education, international |
| User losses increase | Better risk management features |
| Broker competition | B2B2C partnerships |

## Success Metrics Dashboard

**Week 1 Targets:**
- WhatsApp echo bot working
- Can parse 10 common queries
- Response time <5 seconds

**Month 1 Targets:**
- All 4 features functional
- 50 beta users
- 90%+ query success rate

**Month 3 Targets:**
- 100 paying users
- ₹1L MRR
- 60% retention rate

**Month 6 Targets:**
- 500 paying users
- ₹5L MRR
- 65% retention rate
- Break-even on operating costs

**Month 12 Targets:**
- 1,000 paying users
- ₹10L MRR
- 70% retention rate
- Profitable

## Resources & References

### Data Sources
- NSE India: https://www.nseindia.com/
- BSE India: https://www.bseindia.com/
- Chartink: https://chartink.com/

### WhatsApp Business API
- Twilio WhatsApp: https://www.twilio.com/whatsapp
- Meta WhatsApp Business: https://developers.facebook.com/docs/whatsapp

### Market Data APIs
- TrueData: https://truedata.in/
- Zerodha Kite: https://kite.trade/
- Upstox: https://upstox.com/developer/

### Regulatory
- SEBI: https://www.sebi.gov.in/
- RIA Registration: https://www.sebi.gov.in/sebi_data/commondocs/riaguideline_p.pdf

## Getting Started Checklist

- [ ] Read this document thoroughly
- [ ] Set up development environment (Python 3.11+, PostgreSQL, Redis)
- [ ] Get WhatsApp Business API sandbox access
- [ ] Register for demo market data API
- [ ] Clone starter template
- [ ] Run hello world WhatsApp bot
- [ ] Implement first query type (live price)
- [ ] Write tests
- [ ] Deploy to staging
- [ ] Test end-to-end
- [ ] Iterate based on feedback

## Questions to Resolve During Development

1. **GV Score Algorithm:** What exact formula/indicators?
2. **Data Provider:** Which vendor for production? (cost vs quality)
3. **Subscription Tiers:** What features in Basic vs Pro vs Elite?
4. **Free Trial:** 7 days or 14 days? Feature limitations?
5. **Payment Gateway:** Razorpay vs Stripe vs others?
6. **Multi-language:** Start with English only or add Hindi?
7. **Customer Support:** Chatbot vs human vs hybrid?
8. **Broker Integration:** Which broker to approach first?

## Appendix: Example User Conversations

### Conversation 1: New User Onboarding
```
User: Hi
Bot: 👋 Welcome to GammaVantage! Your personal F&O trading assistant.

I can help you with:
📊 Trade Snapshots (try: "NIFTY Futures")
💰 Price Lookups (try: "BANKNIFTY 49000 CE price")
🔍 Market Screeners (try: "stocks above 210 ema")
🎯 Trade Simulator (try: "What if I bought RELIANCE yesterday?")

⚠️ *Important:* I provide data and insights, not financial advice. Always trade at your own risk.

What would you like to explore first?
```

### Conversation 2: Trade Snapshot
```
User: NIFTY Futures
Bot: [Formatted Trade Snapshot as shown above]
User: Thanks! What about BANKNIFTY?
Bot: [BANKNIFTY Trade Snapshot]
```

### Conversation 3: What-If Simulator
```
User: What if I bought NIFTY 23000 CE yesterday?
Bot: 🎯 *Hypothetical Trade Analysis*

📍 *Entry:* NIFTY 23000 CE
⏰ Yesterday (04-Nov) at Open: ₹185.50
💼 Action: BUY (1 lot = 50 qty)

📊 *Exit:* Current Price: ₹242.30
📈 Points Gained: +56.80

💰 *P&L Calculation:*
Entry: ₹185.50 Ã— 50 = ₹9,275
Exit: ₹242.30 Ã— 50 = ₹12,115
*Profit: ₹2,840 (+30.62%)*

⚠️ *Note:* Does not include brokerage, taxes, and slippage.

Want to simulate another trade?
```

---

**Document Version:** 1.0  
**Last Updated:** November 5, 2025  
**Status:** Ready for Development

---

## Quick Start Command

```bash
# Start here
git clone <repo-url>
cd gammaVantage
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Configure your API keys
python -m app.main  # Start development server
```

## Support & Questions

For any clarifications during development:
1. Check existing PRD (PRD.txt) for feature details
2. Refer to Gaps analysis (Gaps.txt) for known issues
3. Consult this guide for technical direction
4. Document new decisions in DECISIONS.md
5. Keep CHANGELOG.md updated

**Happy Building! 🚀**
