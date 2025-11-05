"""
Cache Models

Data structures for cached data in Redis.
"""

from datetime import datetime
from typing import Any, Optional


class CachedData:
    """Wrapper for cached data with metadata."""

    def __init__(self, key: str, value: Any, ttl: int):
        self.key = key
        self.value = value
        self.ttl = ttl  # Time to live in seconds
        self.cached_at = datetime.now()
        self.expires_at: Optional[datetime] = None

    def is_expired(self) -> bool:
        """Check if cached data has expired."""
        if not self.expires_at:
            return False
        return datetime.now() > self.expires_at

    def time_remaining(self) -> int:
        """Get seconds remaining until expiry."""
        if not self.expires_at:
            return 0
        delta = self.expires_at - datetime.now()
        return max(0, int(delta.total_seconds()))
