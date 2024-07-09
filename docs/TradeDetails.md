# TradeDetails

TradeDetails contains a transaction volume, price and pair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pair** | **str** | Pair of the market | [optional] 
**price** | **str** | Price at which the volume traded for | [optional] 
**sequence** | **int** | Sequence identifies the trade within a market | [optional] 
**volume** | **str** | Volume is the amount of base traded | [optional] 

## Example

```python
from luno_openapi.models.trade_details import TradeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TradeDetails from a JSON string
trade_details_instance = TradeDetails.from_json(json)
# print the JSON string representation of the object
print(TradeDetails.to_json())

# convert the object into a dict
trade_details_dict = trade_details_instance.to_dict()
# create an instance of TradeDetails from a dict
trade_details_from_dict = TradeDetails.from_dict(trade_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


