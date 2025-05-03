import pytest
from arbitrage_bot.fetcher import fetch_latest_odds
from arbitrage_bot.parser  import parse_odds

def test_fetch_returns_list():
    odds = fetch_latest_odds()
    assert isinstance(odds, list)

def test_parse_on_empty_list():
    parsed = parse_odds([])
    assert isinstance(parsed, list)
    assert parsed == []  # no stub, deve devolver lista vazia
