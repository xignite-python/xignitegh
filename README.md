# XigniteGH

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/xignite-python/xignitegh/release)
![PyPI](https://img.shields.io/pypi/v/xignitegh)
![GitHub last commit](https://img.shields.io/github/last-commit/xignite-python/xignitegh)
![GitHub issues](https://img.shields.io/github/issues/xignite-python/xignitegh)
![GitHub](https://img.shields.io/github/license/xignite-python/xignitegh)

*Python module to get historical stock data from the XigniteGlobalHistorical API*

XigniteGH is a wrapper to the XigniteGlobalHistorical API. This module implements a python interface to the API provided by [Xignite](https://www.xignite.com/product/historical-stock-prices#/productoverview). A token is required.

## Install
To install the package use:
```shell
pip install xignitegh
```

## Usage
```python
from xignitegh import Xignite

xgh = Xignite(_token="YOUR_TOKEN", _token_userid="YOUR_USERID")
params = {
    "IdentifierType": "Symbol",
    "Identifier": "AAPL",
    "IdentifierAsOfDate": "",
    "AdjustmentMethod": "All",
    "StartDate": "7/20/2020",
    "EndDate": "7/20/2021",
}
quotes = xgh.get_quotes(params=params)
if quotes["Outcome"] == "Success":
    pass
```