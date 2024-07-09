# ListUserTradesResponse

ListUserTradesResponse response for /api/1/listtrades

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trades** | [**List[TradeV2]**](TradeV2.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_user_trades_response import ListUserTradesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserTradesResponse from a JSON string
list_user_trades_response_instance = ListUserTradesResponse.from_json(json)
# print the JSON string representation of the object
print(ListUserTradesResponse.to_json())

# convert the object into a dict
list_user_trades_response_dict = list_user_trades_response_instance.to_dict()
# create an instance of ListUserTradesResponse from a dict
list_user_trades_response_from_dict = ListUserTradesResponse.from_dict(list_user_trades_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


