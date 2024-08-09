# TradeV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Amount of base filled | [optional] 
**client_order_id** | **str** | Client Order ID has the value that was passed in when the Order was posted. | [optional] 
**counter** | **str** | Amount of counter filled | [optional] 
**fee_base** | **str** | Base amount of fees charged | [optional] 
**fee_counter** | **str** | Counter amount of fees charged | [optional] 
**is_buy** | **bool** |  | [optional] 
**order_id** | **str** | Unique order identifier | [optional] 
**pair** | **str** | Currency pair | [optional] 
**price** | **str** | Order price | [optional] 
**sequence** | **int** |  | [optional] 
**timestamp** | **int** | Unix timestamp in milliseconds | [optional] 
**type** | **str** | Order type | [optional] 
**volume** | **str** | Order volume | [optional] 

## Example

```python
from luno_openapi.models.trade_v2 import TradeV2

# TODO update the JSON string below
json = "{}"
# create an instance of TradeV2 from a JSON string
trade_v2_instance = TradeV2.from_json(json)
# print the JSON string representation of the object
print(TradeV2.to_json())

# convert the object into a dict
trade_v2_dict = trade_v2_instance.to_dict()
# create an instance of TradeV2 from a dict
trade_v2_from_dict = TradeV2.from_dict(trade_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


