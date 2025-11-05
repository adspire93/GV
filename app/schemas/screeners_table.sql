-- Screener Results Table
-- Stores stock screening results from Chartink

CREATE TABLE IF NOT EXISTS screener_results (
    id SERIAL PRIMARY KEY,
    screener_id VARCHAR(50) NOT NULL,
    screener_name VARCHAR(100) NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2),
    change_percent DECIMAL(5, 2),
    volume BIGINT,
    metrics JSONB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(screener_id, symbol, timestamp)
);

-- Indexes
CREATE INDEX idx_screener_id ON screener_results(screener_id);
CREATE INDEX idx_screener_timestamp ON screener_results(timestamp);
CREATE INDEX idx_screener_symbol ON screener_results(symbol);

-- Partitioning by timestamp (optional, for large datasets)
-- CREATE TABLE screener_results PARTITION BY RANGE (timestamp);

-- Comments
COMMENT ON TABLE screener_results IS 'Stock screening results from Chartink webhooks';
COMMENT ON COLUMN screener_results.metrics IS 'Additional screener-specific metrics (RSI, EMA, etc.)';
