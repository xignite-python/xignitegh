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
    quotes = xgh.get_quotes()
    assert isinstance(quotes, dict), "Result must be of type dictionary"
    assert quotes["Outcome"] == "RegistrationError"


def test_get_quotes_with_invalid_userid():
    xgh = Xignite(_token="invalid", _token_userid=1)
    quotes = xgh.get_quotes()
    assert isinstance(quotes, dict), "Result must be of type dictionary"
    assert quotes["Outcome"] == "RegistrationError"
