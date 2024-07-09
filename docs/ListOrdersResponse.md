# ListOrdersResponse

ListOrdersResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[Order]**](Order.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_orders_response import ListOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrdersResponse from a JSON string
list_orders_response_instance = ListOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(ListOrdersResponse.to_json())

# convert the object into a dict
list_orders_response_dict = list_orders_response_instance.to_dict()
# create an instance of ListOrdersResponse from a dict
list_orders_response_from_dict = ListOrdersResponse.from_dict(list_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


