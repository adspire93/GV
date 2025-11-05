-- Query Log Table
-- Stores all user queries for analytics and debugging

CREATE TABLE IF NOT EXISTS query_log (
    query_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    query_text TEXT NOT NULL,
    intent VARCHAR(50),
    entities JSONB,
    response_time_ms INTEGER,
    success BOOLEAN DEFAULT true,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT valid_intent CHECK (
        intent IN ('snapshot', 'price', 'screener', 'simulator', 'help', 'subscribe', 'unknown')
    )
);

-- Indexes
CREATE INDEX idx_queries_user ON query_log(user_id);
CREATE INDEX idx_queries_created ON query_log(created_at);
CREATE INDEX idx_queries_intent ON query_log(intent);
CREATE INDEX idx_queries_success ON query_log(success);

-- Comments
COMMENT ON TABLE query_log IS 'Log of all user queries';
COMMENT ON COLUMN query_log.entities IS 'Extracted entities (instrument, strike, date, etc.)';
COMMENT ON COLUMN query_log.response_time_ms IS 'Time taken to process query in milliseconds';
