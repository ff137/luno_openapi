# PublicTrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_buy** | **bool** | Whether the taker was buying or not. | [optional] 
**price** | **str** | Price at which the asset traded at | [optional] 
**sequence** | **int** | The ever incrementing trade identifier within a market | [optional] 
**timestamp** | **str** | Unix timestamp in milliseconds | [optional] 
**volume** | **str** | Amount of assets traded | [optional] 

## Example

```python
from luno_openapi.models.public_trade import PublicTrade

# TODO update the JSON string below
json = "{}"
# create an instance of PublicTrade from a JSON string
public_trade_instance = PublicTrade.from_json(json)
# print the JSON string representation of the object
print(PublicTrade.to_json())

# convert the object into a dict
public_trade_dict = public_trade_instance.to_dict()
# create an instance of PublicTrade from a dict
public_trade_from_dict = PublicTrade.from_dict(public_trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


