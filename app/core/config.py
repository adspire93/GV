"""
Configuration Management

Centralized configuration for the GammaVantage application.
Loads settings from environment variables.

Environment Variables Required:
- WHATSAPP_API_KEY: WhatsApp Business API key
- WHATSAPP_PHONE_NUMBER_ID: WhatsApp phone number ID
- DATABASE_URL: PostgreSQL connection string
- REDIS_URL: Redis connection string
- MARKET_DATA_API_KEY: Market data provider API key
- MARKET_DATA_API_URL: Market data provider endpoint
- CHARTINK_WEBHOOK_SECRET: Chartink webhook validation secret
- PAYMENT_GATEWAY_KEY: Payment gateway API key
- PAYMENT_GATEWAY_SECRET: Payment gateway secret

Performance Settings:
- CACHE_TTL_LIVE_PRICE: 60 seconds
- CACHE_TTL_HISTORICAL: 3600 seconds
- CACHE_TTL_SCREENER: 900 seconds (15 minutes)
- CACHE_TTL_SNAPSHOT: 30 seconds
- RATE_LIMIT_PER_USER: 10 queries/minute
- RATE_LIMIT_GLOBAL: 1000 queries/minute
"""

import os
from typing import Optional


class Settings:
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = "GammaVantage"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # WhatsApp
    WHATSAPP_API_KEY: Optional[str] = os.getenv("WHATSAPP_API_KEY")
    WHATSAPP_PHONE_NUMBER_ID: Optional[str] = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    WHATSAPP_VERIFY_TOKEN: Optional[str] = os.getenv("WHATSAPP_VERIFY_TOKEN")

    # Database
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    TIMESERIES_DB_URL: Optional[str] = os.getenv("TIMESERIES_DB_URL")

    # Cache
    REDIS_URL: Optional[str] = os.getenv("REDIS_URL", "redis://localhost:6379")

    # Market Data
    MARKET_DATA_API_KEY: Optional[str] = os.getenv("MARKET_DATA_API_KEY")
    MARKET_DATA_API_URL: Optional[str] = os.getenv("MARKET_DATA_API_URL")

    # Chartink
    CHARTINK_WEBHOOK_SECRET: Optional[str] = os.getenv("CHARTINK_WEBHOOK_SECRET")

    # Payment
    PAYMENT_GATEWAY_KEY: Optional[str] = os.getenv("PAYMENT_GATEWAY_KEY")
    PAYMENT_GATEWAY_SECRET: Optional[str] = os.getenv("PAYMENT_GATEWAY_SECRET")

    # Cache TTL (seconds)
    CACHE_TTL_LIVE_PRICE: int = 60
    CACHE_TTL_HISTORICAL: int = 3600
    CACHE_TTL_SCREENER: int = 900
    CACHE_TTL_SNAPSHOT: int = 30

    # Rate Limiting
    RATE_LIMIT_PER_USER: int = 10  # queries per minute
    RATE_LIMIT_GLOBAL: int = 1000  # queries per minute

    # Performance
    MAX_RESPONSE_TIME_MS: int = 2000
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10


settings = Settings()
