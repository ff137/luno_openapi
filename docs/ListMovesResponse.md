# ListMovesResponse

ListMovesResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moves** | [**List[FundsMove]**](FundsMove.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_moves_response import ListMovesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMovesResponse from a JSON string
list_moves_response_instance = ListMovesResponse.from_json(json)
# print the JSON string representation of the object
print(ListMovesResponse.to_json())

# convert the object into a dict
list_moves_response_dict = list_moves_response_instance.to_dict()
# create an instance of ListMovesResponse from a dict
list_moves_response_from_dict = ListMovesResponse.from_dict(list_moves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


