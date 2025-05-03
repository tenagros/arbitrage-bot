def test_store_parsed_returns_true():
    from arbitrage_bot.store import store_parsed
    assert store_parsed([]) is True
