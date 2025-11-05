"""
Query Model

Represents user queries and their metadata.
Used for analytics and improving query understanding.
"""

from datetime import datetime
from typing import Optional


class Query:
    """
    Query data model.

    Attributes:
        query_id: Unique identifier (UUID)
        user_id: User who made the query
        query_text: Raw user query text
        intent: Classified intent (snapshot, price, screener, simulator)
        entities: Extracted entities (instrument, strike, etc.)
        response_time_ms: Time taken to respond
        success: Whether query was handled successfully
        error_message: Error message if failed
        created_at: Query timestamp
    """

    def __init__(self, query_id: str, user_id: str, query_text: str):
        self.query_id = query_id
        self.user_id = user_id
        self.query_text = query_text
        self.intent: Optional[str] = None
        self.entities: dict = {}
        self.response_time_ms: Optional[int] = None
        self.success = True
        self.error_message: Optional[str] = None
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert query object to dictionary."""
        pass

    @staticmethod
    def from_dict(data: dict) -> 'Query':
        """Create query object from dictionary."""
        pass
