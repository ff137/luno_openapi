# ListTradesResponse

ListTradesResponse response for /api/1/trades

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trades** | [**List[PublicTrade]**](PublicTrade.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_trades_response import ListTradesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTradesResponse from a JSON string
list_trades_response_instance = ListTradesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTradesResponse.to_json())

# convert the object into a dict
list_trades_response_dict = list_trades_response_instance.to_dict()
# create an instance of ListTradesResponse from a dict
list_trades_response_from_dict = ListTradesResponse.from_dict(list_trades_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


