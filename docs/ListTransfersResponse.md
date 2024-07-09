# ListTransfersResponse

ListTransfersResponse response for /api/1/transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfers** | [**List[Transfer]**](Transfer.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_transfers_response import ListTransfersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransfersResponse from a JSON string
list_transfers_response_instance = ListTransfersResponse.from_json(json)
# print the JSON string representation of the object
print(ListTransfersResponse.to_json())

# convert the object into a dict
list_transfers_response_dict = list_transfers_response_instance.to_dict()
# create an instance of ListTransfersResponse from a dict
list_transfers_response_from_dict = ListTransfersResponse.from_dict(list_transfers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


