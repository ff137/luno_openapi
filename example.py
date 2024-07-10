import asyncio
import os
from typing import List

from luno_openapi import ListTickersResponse, LunoClient
from luno_openapi.models.ticker import Ticker

api_key_id = os.environ.get("API_KEY_ID")
api_key_secret = os.environ.get("API_KEY_SECRET")

client = LunoClient(api_key_id=api_key_id, api_key_secret=api_key_secret)


async def run():
    result: ListTickersResponse = await client.market_api.get_tickers()

    tickers: List[Ticker] = result.tickers or []

    for ticker in tickers:
        print(f"{ticker=}")


asyncio.get_event_loop().run_until_complete(run())
