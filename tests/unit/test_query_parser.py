"""
Unit tests for Query Parser Service

Tests natural language query parsing and entity extraction.
"""

import pytest
from app.services.query_parser import QueryParser


@pytest.fixture
def parser():
    """Create parser instance for tests."""
    return QueryParser()


def test_parse_simple_snapshot_query(parser):
    """Test parsing simple snapshot query."""
    result = parser.parse("NIFTY Futures")
    assert result["intent"] == "snapshot"
    assert result["entities"]["instrument"] == "NIFTY"


def test_parse_price_lookup_query(parser):
    """Test parsing price lookup query."""
    result = parser.parse("What is the price of BANKNIFTY Futures?")
    assert result["intent"] == "price"
    assert result["entities"]["instrument"] == "BANKNIFTY"


def test_parse_options_query(parser):
    """Test parsing options query."""
    result = parser.parse("NIFTY 23000 CE price")
    assert result["entities"]["instrument"] == "NIFTY"
    assert result["entities"]["strike"] == 23000
    assert result["entities"]["option_type"] in ["CE", "CALL"]


def test_parse_simulator_query(parser):
    """Test parsing trade simulator query."""
    result = parser.parse("What if I bought NIFTY Futures yesterday?")
    assert result["intent"] == "simulator"
    assert result["entities"]["action"] == "buy"


# TODO: Add more test cases
# - Test date/time parsing
# - Test quantity extraction
# - Test invalid queries
# - Test edge cases
