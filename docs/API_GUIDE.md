# GammaVantage API Guide

## Webhooks

### WhatsApp Webhook

**Endpoint:** `POST /webhook/whatsapp`

Receives incoming WhatsApp messages.

**Request Format:**
```json
{
  "entry": [{
    "changes": [{
      "value": {
        "messages": [{
          "from": "919876543210",
          "text": {
            "body": "NIFTY Futures"
          }
        }]
      }
    }]
  }]
}
```

### Chartink Webhook

**Endpoint:** `POST /webhook/chartink`

Receives stock screener results.

**Request Format:**
```json
{
  "screener_id": "stocks_above_210_ema",
  "timestamp": "2025-11-05T14:30:00",
  "results": [
    {
      "symbol": "TCS",
      "price": 3842.50,
      "change_percent": 2.3
    }
  ]
}
```

### Payment Webhook

**Endpoint:** `POST /webhook/payment`

Receives payment notifications.

## Health Check

**Endpoint:** `GET /health`

Returns system health status.

**Response:**
```json
{
  "status": "healthy",
  "components": {
    "database": "ok",
    "cache": "ok",
    "market_data_api": "ok"
  }
}
```

## Internal APIs

(Documentation for internal service APIs - TODO)
