"""Sentiment Data."""
import datetime
import pandas as pd

from .parser import fmp_json_parser
from .format import try_to_float


def get_social_sentiment(symbol: str) -> str:
    sentiment = []
    page = 0
    while True:
        tmp = fmp_json_parser(path=f"/historical/social-sentiment?symbol={symbol}&page={page}", api_version="v4")
        if len(tmp) == 0 or page > 10:
            break
        sentiment += tmp
        page += 1

    if len(sentiment) > 0:
        data = pd.DataFrame(sentiment)
        data["date"] = pd.to_datetime(data["date"].apply(lambda x: x[0:10]))

        current_dt = pd.to_datetime(datetime.date.today())
        data = data[(data["date"] >= current_dt - datetime.timedelta(days=15)) & (data["date"] < current_dt)].sort_index()
        data = data.groupby("date")[["stocktwitsSentiment"]].mean().join(data.groupby("date")[["stocktwitsPosts"]].sum())
        data.columns = ["sentiment","posts"]
        data["sentiment"] = data["sentiment"].apply(lambda x: try_to_float(x, 2))
        return "Sentiment scores for last 15 days:\n" + data.to_csv()
    return ""
