"""Price data."""
import pandas as pd

from .parser import fmp_json_parser

def get_last_price_data(symbol: str) -> str:
    data = fmp_json_parser(path=f"/historical-price-full/{symbol}?serietype=line", api_version="v3").get("historical")
    data = pd.DataFrame(data).sort_values(by="date").set_index("date")
    data["pct_change_1d"] = data["close"].pct_change(periods=1)
    data["pct_change_1m"] = data["close"].pct_change(periods=22)
    data["pct_change_1y"] = data["close"].pct_change(periods=252)
    data = data.iloc[-1]
    data_str = f"Price Data:\nLast Price={data.close}\nReturns 1D={data.pct_change_1d}\nReturns 1M={data.pct_change_1m}\nReturns 1Y={data.pct_change_1y}"
    return data_str