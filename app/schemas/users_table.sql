-- Users Table
-- Stores GammaVantage user information

CREATE TABLE IF NOT EXISTS users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    subscription_tier VARCHAR(20) DEFAULT 'free_trial',
    subscription_status VARCHAR(20) DEFAULT 'active',
    subscription_start TIMESTAMP,
    subscription_end TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    queries_today INTEGER DEFAULT 0,
    preferences JSONB DEFAULT '{}',

    CONSTRAINT valid_tier CHECK (
        subscription_tier IN ('free_trial', 'basic', 'pro', 'elite')
    ),
    CONSTRAINT valid_status CHECK (
        subscription_status IN ('active', 'expired', 'cancelled')
    )
);

-- Indexes
CREATE INDEX idx_users_phone ON users(phone_number);
CREATE INDEX idx_users_subscription ON users(subscription_tier, subscription_status);
CREATE INDEX idx_users_last_active ON users(last_active);

-- Comments
COMMENT ON TABLE users IS 'GammaVantage user accounts';
COMMENT ON COLUMN users.queries_today IS 'Number of queries made today (resets daily)';
COMMENT ON COLUMN users.preferences IS 'User notification and feature preferences';
