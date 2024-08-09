# luno_openapi.OrdersApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fee_info**](OrdersApi.md#get_fee_info) | **GET** /api/1/fee_info | Get fee information
[**get_order**](OrdersApi.md#get_order) | **GET** /api/1/orders/{id} | Get order
[**get_order_v2**](OrdersApi.md#get_order_v2) | **GET** /api/exchange/2/orders/{id} | Get Order v2
[**get_order_v3**](OrdersApi.md#get_order_v3) | **GET** /api/exchange/3/order | Get Order v3
[**list_orders**](OrdersApi.md#list_orders) | **GET** /api/1/listorders | List orders
[**list_orders_v2**](OrdersApi.md#list_orders_v2) | **GET** /api/exchange/2/listorders | List Orders v2
[**list_user_trades**](OrdersApi.md#list_user_trades) | **GET** /api/1/listtrades | List trades
[**post_limit_order**](OrdersApi.md#post_limit_order) | **POST** /api/1/postorder | Post Limit Order
[**post_market_order**](OrdersApi.md#post_market_order) | **POST** /api/1/marketorder | Post Market Order
[**stop_order**](OrdersApi.md#stop_order) | **POST** /api/1/stoporder | Cancel Order


# **get_fee_info**
> GetFeeInfoResponse get_fee_info(pair)

Get fee information

Returns the fees and 30 day trading volume (as of midnight) for a given currency pair.  For complete details, please see <a href=\"en/countries\">Fees & Features</a>.  Permissions required: <code>Perm_R_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_fee_info_response import GetFeeInfoResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    pair = 'XBTZAR' # str | Get fee information about this pair.

    try:
        # Get fee information
        api_response = await api_instance.get_fee_info(pair)
        print("The response of OrdersApi->get_fee_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_fee_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Get fee information about this pair. | 

### Return type

[**GetFeeInfoResponse**](GetFeeInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> GetOrderResponse get_order(id)

Get order

Get an Order's details by its ID.  Permissions required: <code>Perm_R_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_order_response import GetOrderResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    id = 'BXMC2CJ7HNB88U4' # str | Order reference

    try:
        # Get order
        api_response = await api_instance.get_order(id)
        print("The response of OrdersApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order reference | 

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_v2**
> GetOrder2Response get_order_v2(id)

Get Order v2

Get the details for an order.  Permissions required: <code>Perm_R_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_order2_response import GetOrder2Response
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
    api_instance = luno_openapi.OrdersApi(api_client)
    id = 'BXMC2CJ7HNB88U4' # str | Order reference

    try:
        # Get Order v2
        api_response = await api_instance.get_order_v2(id)
        print("The response of OrdersApi->get_order_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order reference | 

### Return type

[**GetOrder2Response**](GetOrder2Response.md)

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

# **get_order_v3**
> GetOrder2Response get_order_v3(id=id, client_order_id=client_order_id)

Get Order v3

Get the details for an order by order reference or client order ID. Exactly one of the two parameters must be provided, otherwise an error is returned. Permissions required: <code>Perm_R_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_order2_response import GetOrder2Response
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
    api_instance = luno_openapi.OrdersApi(api_client)
    id = 'BXMC2CJ7HNB88U4' # str | Order reference (optional)
    client_order_id = 'lmt-53960812' # str | Client Order ID has the value that was passed in when the Order was posted. (optional)

    try:
        # Get Order v3
        api_response = await api_instance.get_order_v3(id=id, client_order_id=client_order_id)
        print("The response of OrdersApi->get_order_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order reference | [optional] 
 **client_order_id** | **str**| Client Order ID has the value that was passed in when the Order was posted. | [optional] 

### Return type

[**GetOrder2Response**](GetOrder2Response.md)

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

# **list_orders**
> ListOrdersResponse list_orders(state=state, pair=pair, created_before=created_before, limit=limit)

List orders

Returns a list of the most recently placed Orders. Users can specify an optional <code>state=PENDING</code> parameter to restrict the results to only open Orders. Users can also specify the market by using the optional currency pair parameter.  Permissions required: <code>Perm_R_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_orders_response import ListOrdersResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    state = 'PENDING' # str | Filter to only orders of this state (optional)
    pair = 'XBTZAR' # str | Filter to only orders of this currency pair (optional)
    created_before = 1530865703508 # int | Filter to orders created before this timestamp (Unix milliseconds) (optional)
    limit = 100 # int | Limit to this many orders (optional) (default to 100)

    try:
        # List orders
        api_response = await api_instance.list_orders(state=state, pair=pair, created_before=created_before, limit=limit)
        print("The response of OrdersApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Filter to only orders of this state | [optional] 
 **pair** | **str**| Filter to only orders of this currency pair | [optional] 
 **created_before** | **int**| Filter to orders created before this timestamp (Unix milliseconds) | [optional] 
 **limit** | **int**| Limit to this many orders | [optional] [default to 100]

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders_v2**
> ListOrders2Response list_orders_v2(pair=pair, closed=closed, created_before=created_before, limit=limit)

List Orders v2

Returns a list of the most recently placed orders ordered from newest to oldest. This endpoint will list up to 100 most recent open orders by default.  <b>Please note:</b> This data is archived 100 days after an exchange order is completed.  Permissions required: <Code>Perm_R_Orders</Code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_orders2_response import ListOrders2Response
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
    api_instance = luno_openapi.OrdersApi(api_client)
    pair = 'XBTZAR' # str | Filter to only orders of this currency pair. (optional)
    closed = False # bool | If true, will return closed orders instead of open orders. (optional) (default to False)
    created_before = 1530865703508 # int | Filter to orders created before this timestamp (Unix milliseconds) (optional)
    limit = 100 # int | Limit to this many orders (optional) (default to 100)

    try:
        # List Orders v2
        api_response = await api_instance.list_orders_v2(pair=pair, closed=closed, created_before=created_before, limit=limit)
        print("The response of OrdersApi->list_orders_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->list_orders_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Filter to only orders of this currency pair. | [optional] 
 **closed** | **bool**| If true, will return closed orders instead of open orders. | [optional] [default to False]
 **created_before** | **int**| Filter to orders created before this timestamp (Unix milliseconds) | [optional] 
 **limit** | **int**| Limit to this many orders | [optional] [default to 100]

### Return type

[**ListOrders2Response**](ListOrders2Response.md)

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

# **list_user_trades**
> ListUserTradesResponse list_user_trades(pair, since=since, before=before, after_seq=after_seq, before_seq=before_seq, sort_desc=sort_desc, limit=limit)

List trades

Returns a list of the recent Trades for a given currency pair for this user, sorted by oldest first. If <code>before</code> is specified, then Trades are returned sorted by most-recent first.  <code>type</code> in the response indicates the type of Order that was placed to participate in the trade. Possible types: <code>BID</code>, <code>ASK</code>.  If <code>is_buy</code> in the response is true, then the Order which completed the trade (market taker) was a Bid Order.  Results of this query may lag behind the latest data.  Permissions required: <code>Perm_R_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_user_trades_response import ListUserTradesResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    pair = 'XBTZAR' # str | Filter to trades of this currency pair.
    since = 56 # int | Filter to trades on or after this timestamp (Unix milliseconds). (optional)
    before = 56 # int | Filter to trades before this timestamp (Unix milliseconds). (optional)
    after_seq = 10 # int | Filter to trades from (including) this sequence number. Default behaviour is not to include this filter. (optional)
    before_seq = 1 # int | Filter to trades before (excluding) this sequence number. Default behaviour is not to include this filter. (optional)
    sort_desc = true # bool | If set to true, sorts trades in descending order, otherwise ascending order will be assumed. (optional)
    limit = 100 # int | Limit to this number of trades (default 100). (optional)

    try:
        # List trades
        api_response = await api_instance.list_user_trades(pair, since=since, before=before, after_seq=after_seq, before_seq=before_seq, sort_desc=sort_desc, limit=limit)
        print("The response of OrdersApi->list_user_trades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->list_user_trades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Filter to trades of this currency pair. | 
 **since** | **int**| Filter to trades on or after this timestamp (Unix milliseconds). | [optional] 
 **before** | **int**| Filter to trades before this timestamp (Unix milliseconds). | [optional] 
 **after_seq** | **int**| Filter to trades from (including) this sequence number. Default behaviour is not to include this filter. | [optional] 
 **before_seq** | **int**| Filter to trades before (excluding) this sequence number. Default behaviour is not to include this filter. | [optional] 
 **sort_desc** | **bool**| If set to true, sorts trades in descending order, otherwise ascending order will be assumed. | [optional] 
 **limit** | **int**| Limit to this number of trades (default 100). | [optional] 

### Return type

[**ListUserTradesResponse**](ListUserTradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_limit_order**
> PostLimitOrderResponse post_limit_order(pair, type, volume, price, time_in_force=time_in_force, post_only=post_only, stop_price=stop_price, stop_direction=stop_direction, base_account_id=base_account_id, counter_account_id=counter_account_id, timestamp=timestamp, ttl=ttl, client_order_id=client_order_id)

Post Limit Order

<b>Warning!</b> Orders cannot be reversed once they have executed. Please ensure your program has been thoroughly tested before submitting Orders.  If no <code>base_account_id</code> or <code>counter_account_id</code> are specified, your default base currency or counter currency account will be used. You can find your Account IDs by calling the <a href=\"#operation/getBalances\">Balances</a> API.  Permissions required: <code>Perm_W_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.post_limit_order_response import PostLimitOrderResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    pair = 'XBTZAR' # str | The currency pair to trade.
    type = 'BID' # str | <code>BID</code> for a bid (buy) limit order<br> <code>ASK</code> for an ask (sell) limit order
    volume = '1.423' # str | Amount of cryptocurrency to buy or sell as a decimal string in units of the currency.
    price = '1200' # str | Limit price as a decimal string in units of ZAR/BTC.
    time_in_force = GTC # str | <code>GTC</code> Good 'Til Cancelled. The order remains open until it is filled or cancelled by the user.</br> <code>IOC</code> Immediate Or Cancel. The part of the order that cannot be filled immediately will be cancelled. Cannot be post-only.</br> <code>FOK</code> Fill Or Kill. If the order cannot be filled immediately and completely it will be cancelled before any trade. Cannot be post-only. (optional) (default to GTC)
    post_only = false # bool | Post-only Orders will be cancelled if they would otherwise have traded immediately. For example, if there's a bid at ZAR 100,000 and you place a post-only ask at ZAR 100,000, your order will be cancelled instead of trading. If the best bid is ZAR 100,000 and you place a post-only ask at ZAR 101,000, your order won't trade but will go into the order book. (optional)
    stop_price = '1150' # str | Trigger trade price to activate this order as a decimal string. If this is set then this is treated as a Stop Limit Order and `stop_direction` is expected to be set too. (optional)
    stop_direction = 'ABOVE' # str | Side of the trigger price to activate the order. This should be set if `stop_price` is also set.  `RELATIVE_LAST_TRADE` will automatically infer the direction based on the last trade price and the stop price. If last trade price is less than stop price then stop direction is ABOVE otherwise is BELOW. (optional)
    base_account_id = 12345 # int | The base currency Account to use in the trade. (optional)
    counter_account_id = 12345 # int | The counter currency Account to use in the trade. (optional)
    timestamp = 56 # int | Unix timestamp in milliseconds of when the request was created and sent. (optional)
    ttl = 10000 # int | Specifies the number of milliseconds after timestamp the request is valid for. If `timestamp` is not specified, `ttl` will not be used. (optional) (default to 10000)
    client_order_id = 'lmt-53960812' # str | Client order ID. May only contain alphanumeric (0-9, a-z, or A-Z) and special characters (_ ; , . -). Maximum length: 255. It will be available in read endpoints, so you can use it to reconcile Luno with your internal system. Values must be unique across all your successful order creation endpoint calls; trying to create an order with the same `client_order_id` as one of your past orders will result in a HTTP 409 Conflict response. (optional)

    try:
        # Post Limit Order
        api_response = await api_instance.post_limit_order(pair, type, volume, price, time_in_force=time_in_force, post_only=post_only, stop_price=stop_price, stop_direction=stop_direction, base_account_id=base_account_id, counter_account_id=counter_account_id, timestamp=timestamp, ttl=ttl, client_order_id=client_order_id)
        print("The response of OrdersApi->post_limit_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->post_limit_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| The currency pair to trade. | 
 **type** | **str**| &lt;code&gt;BID&lt;/code&gt; for a bid (buy) limit order&lt;br&gt; &lt;code&gt;ASK&lt;/code&gt; for an ask (sell) limit order | 
 **volume** | **str**| Amount of cryptocurrency to buy or sell as a decimal string in units of the currency. | 
 **price** | **str**| Limit price as a decimal string in units of ZAR/BTC. | 
 **time_in_force** | **str**| &lt;code&gt;GTC&lt;/code&gt; Good &#39;Til Cancelled. The order remains open until it is filled or cancelled by the user.&lt;/br&gt; &lt;code&gt;IOC&lt;/code&gt; Immediate Or Cancel. The part of the order that cannot be filled immediately will be cancelled. Cannot be post-only.&lt;/br&gt; &lt;code&gt;FOK&lt;/code&gt; Fill Or Kill. If the order cannot be filled immediately and completely it will be cancelled before any trade. Cannot be post-only. | [optional] [default to GTC]
 **post_only** | **bool**| Post-only Orders will be cancelled if they would otherwise have traded immediately. For example, if there&#39;s a bid at ZAR 100,000 and you place a post-only ask at ZAR 100,000, your order will be cancelled instead of trading. If the best bid is ZAR 100,000 and you place a post-only ask at ZAR 101,000, your order won&#39;t trade but will go into the order book. | [optional] 
 **stop_price** | **str**| Trigger trade price to activate this order as a decimal string. If this is set then this is treated as a Stop Limit Order and &#x60;stop_direction&#x60; is expected to be set too. | [optional] 
 **stop_direction** | **str**| Side of the trigger price to activate the order. This should be set if &#x60;stop_price&#x60; is also set.  &#x60;RELATIVE_LAST_TRADE&#x60; will automatically infer the direction based on the last trade price and the stop price. If last trade price is less than stop price then stop direction is ABOVE otherwise is BELOW. | [optional] 
 **base_account_id** | **int**| The base currency Account to use in the trade. | [optional] 
 **counter_account_id** | **int**| The counter currency Account to use in the trade. | [optional] 
 **timestamp** | **int**| Unix timestamp in milliseconds of when the request was created and sent. | [optional] 
 **ttl** | **int**| Specifies the number of milliseconds after timestamp the request is valid for. If &#x60;timestamp&#x60; is not specified, &#x60;ttl&#x60; will not be used. | [optional] [default to 10000]
 **client_order_id** | **str**| Client order ID. May only contain alphanumeric (0-9, a-z, or A-Z) and special characters (_ ; , . -). Maximum length: 255. It will be available in read endpoints, so you can use it to reconcile Luno with your internal system. Values must be unique across all your successful order creation endpoint calls; trying to create an order with the same &#x60;client_order_id&#x60; as one of your past orders will result in a HTTP 409 Conflict response. | [optional] 

### Return type

[**PostLimitOrderResponse**](PostLimitOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_market_order**
> PostMarketOrderResponse post_market_order(pair, type, counter_volume=counter_volume, base_volume=base_volume, base_account_id=base_account_id, counter_account_id=counter_account_id, timestamp=timestamp, ttl=ttl, client_order_id=client_order_id)

Post Market Order

A Market Order executes immediately, and either buys as much of the asset that can be bought for a set amount of fiat currency, or sells a set amount of the asset for as much as possible.  <b>Warning!</b> Orders cannot be reversed once they have executed. Please ensure your program has been thoroughly tested before submitting Orders.  If no <code>base_account_id</code> or <code>counter_account_id</code> are specified, the default base currency or counter currency account will be used. Users can find their account IDs by calling the <a href=\"#operation/getBalances\">Balances</a> request.  Permissions required: <code>Perm_W_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.post_market_order_response import PostMarketOrderResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    pair = 'XBTZAR' # str | The currency pair to trade.
    type = 'BUY' # str | <code>BUY</code> to buy an asset<br> <code>SELL</code> to sell an asset
    counter_volume = '100.50' # str | For a <code>BUY</code> order: amount of the counter currency to use (e.g. how much EUR to use to buy BTC in the BTC/EUR market) (optional)
    base_volume = '1.423' # str | For a <code>SELL</code> order: amount of the base currency to use (e.g. how much BTC to sell for EUR in the BTC/EUR market) (optional)
    base_account_id = 12345 # int | The base currency account to use in the trade. (optional)
    counter_account_id = 12345 # int | The counter currency account to use in the trade. (optional)
    timestamp = 56 # int | Unix timestamp in milliseconds of when the request was created and sent. (optional)
    ttl = 10000 # int | Specifies the number of milliseconds after timestamp the request is valid for. If `timestamp` is not specified, `ttl` will not be used. (optional) (default to 10000)
    client_order_id = 'mkt-53960812' # str | Client order ID. May only contain alphanumeric (0-9, a-z, or A-Z) and special characters (_ ; , . -). Maximum length: 255. It will be available in read endpoints, so you can use it to reconcile Luno with your internal system. Values must be unique across all your successful order creation endpoint calls; trying to create an order with the same `client_order_id` as one of your past orders will result in a HTTP 409 Conflict response. (optional)

    try:
        # Post Market Order
        api_response = await api_instance.post_market_order(pair, type, counter_volume=counter_volume, base_volume=base_volume, base_account_id=base_account_id, counter_account_id=counter_account_id, timestamp=timestamp, ttl=ttl, client_order_id=client_order_id)
        print("The response of OrdersApi->post_market_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->post_market_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| The currency pair to trade. | 
 **type** | **str**| &lt;code&gt;BUY&lt;/code&gt; to buy an asset&lt;br&gt; &lt;code&gt;SELL&lt;/code&gt; to sell an asset | 
 **counter_volume** | **str**| For a &lt;code&gt;BUY&lt;/code&gt; order: amount of the counter currency to use (e.g. how much EUR to use to buy BTC in the BTC/EUR market) | [optional] 
 **base_volume** | **str**| For a &lt;code&gt;SELL&lt;/code&gt; order: amount of the base currency to use (e.g. how much BTC to sell for EUR in the BTC/EUR market) | [optional] 
 **base_account_id** | **int**| The base currency account to use in the trade. | [optional] 
 **counter_account_id** | **int**| The counter currency account to use in the trade. | [optional] 
 **timestamp** | **int**| Unix timestamp in milliseconds of when the request was created and sent. | [optional] 
 **ttl** | **int**| Specifies the number of milliseconds after timestamp the request is valid for. If &#x60;timestamp&#x60; is not specified, &#x60;ttl&#x60; will not be used. | [optional] [default to 10000]
 **client_order_id** | **str**| Client order ID. May only contain alphanumeric (0-9, a-z, or A-Z) and special characters (_ ; , . -). Maximum length: 255. It will be available in read endpoints, so you can use it to reconcile Luno with your internal system. Values must be unique across all your successful order creation endpoint calls; trying to create an order with the same &#x60;client_order_id&#x60; as one of your past orders will result in a HTTP 409 Conflict response. | [optional] 

### Return type

[**PostMarketOrderResponse**](PostMarketOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_order**
> StopOrderResponse stop_order(order_id)

Cancel Order

Request to cancel an Order.  <b>Note!</b>: Once an Order has been completed, it can not be reversed. The return value from this request will indicate if the Stop request was successful or not.  Permissions required: <code>Perm_W_Orders</code>

### Example


```python
import luno_openapi
from luno_openapi.models.stop_order_response import StopOrderResponse
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
    api_instance = luno_openapi.OrdersApi(api_client)
    order_id = 'BXMC2CJ7HNB88U4' # str | The Order identifier as a string.

    try:
        # Cancel Order
        api_response = await api_instance.stop_order(order_id)
        print("The response of OrdersApi->stop_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->stop_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The Order identifier as a string. | 

### Return type

[**StopOrderResponse**](StopOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

