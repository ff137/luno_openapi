# ListOrders2Response

ListOrders2Response response for /api/2/listorders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[OrderV2]**](OrderV2.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_orders2_response import ListOrders2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrders2Response from a JSON string
list_orders2_response_instance = ListOrders2Response.from_json(json)
# print the JSON string representation of the object
print(ListOrders2Response.to_json())

# convert the object into a dict
list_orders2_response_dict = list_orders2_response_instance.to_dict()
# create an instance of ListOrders2Response from a dict
list_orders2_response_from_dict = ListOrders2Response.from_dict(list_orders2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


