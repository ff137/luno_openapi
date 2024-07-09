# luno_openapi.MarketApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_candles**](MarketApi.md#get_candles) | **GET** /api/exchange/1/candles | Get candles
[**get_order_book**](MarketApi.md#get_order_book) | **GET** /api/1/orderbook_top | Get top order book
[**get_order_book_full**](MarketApi.md#get_order_book_full) | **GET** /api/1/orderbook | Get full order book
[**get_ticker**](MarketApi.md#get_ticker) | **GET** /api/1/ticker | Get ticker for currency pair
[**get_tickers**](MarketApi.md#get_tickers) | **GET** /api/1/tickers | List tickers for all currency pairs
[**list_trades**](MarketApi.md#list_trades) | **GET** /api/1/trades | List recent trades
[**markets**](MarketApi.md#markets) | **GET** /api/exchange/1/markets | Get markets info


# **get_candles**
> GetCandlesResponse get_candles(pair, since, duration)

Get candles

Get candlestick market data from the specified time until now, from the oldest to the most recent.  Permissions required: <code>MP_None</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_candles_response import GetCandlesResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = 'XBTZAR' # str | Currency pair
    since = '1470810728478' # str | Filter to candles starting on or after this timestamp (Unix milliseconds). Only up to 1000 of the earliest candles are returned.
    duration = 300 # int | Candle duration in seconds. For example, 300 corresponds to 5m candles. Currently supported durations are: 60 (1m), 300 (5m), 900 (15m), 1800 (30m), 3600 (1h), 10800 (3h), 14400 (4h), 28800 (8h), 86400 (24h), 259200 (3d), 604800 (7d).

    try:
        # Get candles
        api_response = await api_instance.get_candles(pair, since, duration)
        print("The response of MarketApi->get_candles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_candles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Currency pair | 
 **since** | **str**| Filter to candles starting on or after this timestamp (Unix milliseconds). Only up to 1000 of the earliest candles are returned. | 
 **duration** | **int**| Candle duration in seconds. For example, 300 corresponds to 5m candles. Currently supported durations are: 60 (1m), 300 (5m), 900 (15m), 1800 (30m), 3600 (1h), 10800 (3h), 14400 (4h), 28800 (8h), 86400 (24h), 259200 (3d), 604800 (7d). | 

### Return type

[**GetCandlesResponse**](GetCandlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_book**
> GetOrderBookResponse get_order_book(pair)

Get top order book

This request returns the best 100 `bids` and `asks`, for the currency pair specified, in the Order Book.  `asks` are sorted by price ascending and `bids` are sorted by price descending.  Multiple orders at the same price are aggregated.

### Example


```python
import luno_openapi
from luno_openapi.models.get_order_book_response import GetOrderBookResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = 'XBTZAR' # str | Currency pair of the Orders to retrieve

    try:
        # Get top order book
        api_response = await api_instance.get_order_book(pair)
        print("The response of MarketApi->get_order_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_order_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Currency pair of the Orders to retrieve | 

### Return type

[**GetOrderBookResponse**](GetOrderBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_book_full**
> GetOrderBookResponse get_order_book_full(pair)

Get full order book

This request returns all `bids` and `asks`, for the currency pair specified, in the Order Book.  `asks` are sorted by price ascending and `bids` are sorted by price descending.  Multiple orders at the same price are not aggregated.  <b>WARNING:</b> This may return a large amount of data. Users are recommended to use the <a href=\"#operation/getOrderBookTop\">top 100 bids and asks</a> or the <a href=\"#tag/Streaming-API\">Streaming API</a>.

### Example


```python
import luno_openapi
from luno_openapi.models.get_order_book_response import GetOrderBookResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = 'XBTZAR' # str | Currency pair of the Orders to retrieve

    try:
        # Get full order book
        api_response = await api_instance.get_order_book_full(pair)
        print("The response of MarketApi->get_order_book_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_order_book_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Currency pair of the Orders to retrieve | 

### Return type

[**GetOrderBookResponse**](GetOrderBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticker**
> GetTickerResponse get_ticker(pair)

Get ticker for currency pair

Returns the latest ticker indicators for the specified currency pair.  Please see the <a href=\"#tag/currency \">Currency list</a> for the complete list of supported currency pairs.

### Example


```python
import luno_openapi
from luno_openapi.models.get_ticker_response import GetTickerResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = 'XBTZAR' # str | Currency pair

    try:
        # Get ticker for currency pair
        api_response = await api_instance.get_ticker(pair)
        print("The response of MarketApi->get_ticker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_ticker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Currency pair | 

### Return type

[**GetTickerResponse**](GetTickerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickers**
> ListTickersResponse get_tickers(pair=pair)

List tickers for all currency pairs

Returns the latest ticker indicators from all active Luno exchanges.  Please see the <a href=\"#tag/currency \">Currency list</a> for the complete list of supported currency pairs.

### Example


```python
import luno_openapi
from luno_openapi.models.list_tickers_response import ListTickersResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = ['XBTZAR'] # List[str] | Return tickers for multiple markets (if not provided, all tickers will be returned). To request tickers for multiple markets, pass the parameter multiple times, e.g. `pair=XBTZAR&pair=ETHZAR`. (optional)

    try:
        # List tickers for all currency pairs
        api_response = await api_instance.get_tickers(pair=pair)
        print("The response of MarketApi->get_tickers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_tickers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | [**List[str]**](str.md)| Return tickers for multiple markets (if not provided, all tickers will be returned). To request tickers for multiple markets, pass the parameter multiple times, e.g. &#x60;pair&#x3D;XBTZAR&amp;pair&#x3D;ETHZAR&#x60;. | [optional] 

### Return type

[**ListTickersResponse**](ListTickersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trades**
> ListTradesResponse list_trades(pair, since=since)

List recent trades

Returns a list of recent trades for the specified currency pair. At most 100 trades are returned per call and never trades older than 24h. The trades are sorted from newest to oldest.  Please see the <a href=\"#tag/currency \">Currency list</a> for the complete list of supported currency pairs.

### Example


```python
import luno_openapi
from luno_openapi.models.list_trades_response import ListTradesResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = 'XBTZAR' # str | Currency pair of the market to list the trades from
    since = '1520438111000' # str | Fetch trades executed after this time, specified as a Unix timestamp in milliseconds. An error will be returned if this is before 24h ago. Use this parameter to either restrict to a shorter window or to iterate over the trades in case you need more than the 100 most recent trades. (optional)

    try:
        # List recent trades
        api_response = await api_instance.list_trades(pair, since=since)
        print("The response of MarketApi->list_trades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->list_trades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Currency pair of the market to list the trades from | 
 **since** | **str**| Fetch trades executed after this time, specified as a Unix timestamp in milliseconds. An error will be returned if this is before 24h ago. Use this parameter to either restrict to a shorter window or to iterate over the trades in case you need more than the 100 most recent trades. | [optional] 

### Return type

[**ListTradesResponse**](ListTradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets**
> MarketsInfoResponse markets(pair=pair)

Get markets info

List all supported markets parameter information like price scale, min and max order volumes and market ID.

### Example


```python
import luno_openapi
from luno_openapi.models.markets_info_response import MarketsInfoResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.MarketApi(api_client)
    pair = ['XBTZAR'] # List[str] | List of market pairs to return. Requesting only the required pairs will improve response times. (optional)

    try:
        # Get markets info
        api_response = await api_instance.markets(pair=pair)
        print("The response of MarketApi->markets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->markets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | [**List[str]**](str.md)| List of market pairs to return. Requesting only the required pairs will improve response times. | [optional] 

### Return type

[**MarketsInfoResponse**](MarketsInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

