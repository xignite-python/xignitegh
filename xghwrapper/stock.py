import os
from datetime import date, timedelta

import requests


class Stock(object):

    _XIGNITE_GH = "https://globalhistorical.xignite.com/v3/"
    _XIGNITE_GH_INFO = "xGlobalHistorical.json/GetGlobalHistoricalQuotesTrailing"

    def __init__(self, ticker: str, _token=None, _token_userid=None):

        self.ticker = ticker.upper()

        if _token is None:
            _token = os.environ.get("XIGNITE_TOKEN")
        if not _token or not isinstance(_token, str):
            raise ValueError("The Xignite token must be provided")
        self.token = _token

        if not (_token_userid is None or isinstance(_token_userid, int)):
            raise ValueError("The Xignite userid must be a number")
        self.userid = _token_userid

    def info(self):

        params = {
            "IdentifierType": "Symbol",
            "Identifier": self.ticker,
            "IdentifierAsOfDate": "",
            "AdjustmentMethod": "All",
            "EndDate": (date.today() - timedelta(days=1)).strftime("%m/%d/%Y"),
            "PeriodType": "Day",
            "Periods": "1",
            "_token": self.token,
        }
        if self.userid:
            params["_token_userid"] = self.userid

        url = Stock._XIGNITE_GH + Stock._XIGNITE_GH_INFO
        response = requests.get(url=url, params=params)

        return response.json()["Security"]

    def _get_date(years_ago):

        datum = date.today() - timedelta(days=years_ago * 365)
        return datum.strftime("%m/%d/%Y")
