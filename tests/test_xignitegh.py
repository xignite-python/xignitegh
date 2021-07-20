import pytest
from xignitegh import Xignite


def test_init_without_token():
    with pytest.raises(ValueError):
        xgh = Xignite()


def test_init_with_invalid_token_type():
    with pytest.raises(ValueError):
        xgh = Xignite(_token=1)


def test_init_with_invalid_userid_type():
    with pytest.raises(ValueError):
        xgh = Xignite(_token="invalid", _token_userid="1")


def test_get_quotes_with_invalid_token():
    xgh = Xignite(_token="invalid")
    quotes = xgh.get_quotes(ticker="AAPL", years=1)
    assert isinstance(quotes, dict), "Result must be of type dictionary"
    assert quotes["Outcome"] == "RegistrationError"


def test_get_quotes_with_invalid_userid():
    xgh = Xignite(_token="invalid", _token_userid=1)
    quotes = xgh.get_quotes(ticker="AAPL", years=1)
    assert isinstance(quotes, dict), "Result must be of type dictionary"
    assert quotes["Outcome"] == "RegistrationError"


def test_get_dividends_with_invalid_token():
    xgh = Xignite(_token="invalid")
    dividends = xgh.get_dividends(ticker="AAPL", years=1)
    assert isinstance(dividends, dict), "Result must be of type dictionary"
    assert dividends["Outcome"] == "RegistrationError"


def test_get_dividends_with_invalid_userid():
    xgh = Xignite(_token="invalid", _token_userid=1)
    dividends = xgh.get_dividends(ticker="AAPL", years=1)
    assert isinstance(dividends, dict), "Result must be of type dictionary"
    assert dividends["Outcome"] == "RegistrationError"
