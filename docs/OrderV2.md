# OrderV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Amount of base filled, this value is always positive.  Use this field and &#x60;side&#x60; to determine credit or debit of funds. | [optional] 
**base_account_id** | **int** | The base currency account | [optional] 
**client_order_id** | **str** | Client Order ID has the value that was passed in when the Order was posted. | [optional] 
**completed_timestamp** | **str** | Time of order completion (Unix milliseconds)  This value is set at the time of this order leaving the order book, either immediately upon posting or later on due to a trade or cancellation. Whilst the order is still pending/live it will be 0. | [optional] 
**counter** | **str** | Amount of counter filled, this value is always positive.  Use this field and &#x60;side&#x60; to determine credit or debit of funds. | [optional] 
**counter_account_id** | **int** | The counter currency account | [optional] 
**creation_timestamp** | **str** | Time of order creation (Unix milliseconds) | [optional] 
**expiration_timestamp** | **str** | Time of order expiration (Unix milliseconds)  This value is set at the time of processing a request from you to cancel the order, otherwise it will be 0. | [optional] 
**fee_base** | **str** | Base amount of fees to be charged | [optional] 
**fee_counter** | **str** | Counter amount of fees to be charged | [optional] 
**limit_price** | **str** | Limit price to transact | [optional] 
**limit_volume** | **str** | Limit volume to transact | [optional] 
**order_id** | **str** | The order reference | [optional] 
**pair** | **str** | Specifies the market | [optional] 
**side** | **str** | The intention of the order, whether to buy or sell funds in the market.  You can use this to determine the flow of funds in the order. | [optional] 
**status** | **str** | The current state of the order  Status meaning:&lt;br&gt; &lt;code&gt;AWAITING&lt;/code&gt; The order is awaiting to enter the order book.&lt;br&gt; &lt;code&gt;PENDING&lt;/code&gt; The order is in the order book. Some trades may have taken place but the order is not filled yet.&lt;br&gt; &lt;code&gt;COMPLETE&lt;/code&gt; The order is no longer in the order book. It has been settled/filled or has been cancelled. | [optional] 
**stop_direction** | **str** | Direction to trigger the order | [optional] 
**stop_price** | **str** | Price to trigger the order | [optional] 
**time_in_force** | **str** | The Time in force option used when the LimitOrder was posted.  Only returned on limit orders.&lt;br&gt; &lt;code&gt;GTC&lt;/code&gt; Good &#39;Til Cancelled. The order remains open until it is filled or cancelled by the user. (default)&lt;/br&gt; &lt;code&gt;IOC&lt;/code&gt; Immediate Or Cancel. The part of the order that cannot be filled immediately will be cancelled. Cannot be post-only.&lt;/br&gt; &lt;code&gt;FOK&lt;/code&gt; Fill Or Kill. If the order cannot be filled immediately and completely it will be cancelled before any trade. Cannot be post-only. | [optional] 
**type** | **str** | The order type | [optional] 

## Example

```python
from luno_openapi.models.order_v2 import OrderV2

# TODO update the JSON string below
json = "{}"
# create an instance of OrderV2 from a JSON string
order_v2_instance = OrderV2.from_json(json)
# print the JSON string representation of the object
print(OrderV2.to_json())

# convert the object into a dict
order_v2_dict = order_v2_instance.to_dict()
# create an instance of OrderV2 from a dict
order_v2_from_dict = OrderV2.from_dict(order_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


