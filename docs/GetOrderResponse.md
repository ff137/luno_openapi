# GetOrderResponse

GetOrderResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Amount of base filled, this value is always positive. | [optional] 
**completed_timestamp** | **str** | Time of order completion (Unix milliseconds)  This value is set at the time of this order leaving the order book, either immediately upon posting or later on due to a trade or cancellation. Whilst the order is still pending/live it will be 0. | [optional] 
**counter** | **str** | Amount of counter filled, this value is always positive. | [optional] 
**creation_timestamp** | **str** | Time of order creation (Unix milliseconds) | [optional] 
**expiration_timestamp** | **str** | Time of order expiration (Unix milliseconds)  This value is set at the time of processing a request from you to cancel the order, otherwise it will be 0. | [optional] 
**fee_base** | **str** | Base amount of fees to be charged | [optional] 
**fee_counter** | **str** | Counter amount of fees to be charged | [optional] 
**limit_price** | **str** | Limit price to transact | [optional] 
**limit_volume** | **str** | Limit volume to transact | [optional] 
**order_id** | **str** |  | [optional] 
**pair** | **str** | Specifies the market. | [optional] 
**state** | **str** | &lt;code&gt;PENDING&lt;/code&gt; The order has been placed. Some trades may have taken place but the order is not filled yet.&lt;br&gt; &lt;code&gt;COMPLETE&lt;/code&gt; The order is no longer active. It has been settled or has been cancelled. | [optional] 
**time_in_force** | **str** | The Time in force option used when the LimitOrder was posted.  Only returned on limit orders.&lt;br&gt; &lt;code&gt;GTC&lt;/code&gt; Good &#39;Til Cancelled. The order remains open until it is filled or cancelled by the user. (default)&lt;/br&gt; &lt;code&gt;IOC&lt;/code&gt; Immediate Or Cancel. The part of the order that cannot be filled immediately will be cancelled. Cannot be post-only.&lt;/br&gt; &lt;code&gt;FOK&lt;/code&gt; Fill Or Kill. If the order cannot be filled immediately and completely it will be cancelled before any trade. Cannot be post-only. | [optional] 
**type** | **str** | &lt;code&gt;BUY&lt;/code&gt; buy market order.&lt;br&gt; &lt;code&gt;SELL&lt;/code&gt; sell market order.&lt;br&gt; &lt;code&gt;BID&lt;/code&gt; bid (buy) limit order.&lt;br&gt; &lt;code&gt;ASK&lt;/code&gt; ask (sell) limit order. | [optional] 

## Example

```python
from luno_openapi.models.get_order_response import GetOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderResponse from a JSON string
get_order_response_instance = GetOrderResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrderResponse.to_json())

# convert the object into a dict
get_order_response_dict = get_order_response_instance.to_dict()
# create an instance of GetOrderResponse from a dict
get_order_response_from_dict = GetOrderResponse.from_dict(get_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


