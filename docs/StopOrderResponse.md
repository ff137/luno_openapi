# StopOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from luno_openapi.models.stop_order_response import StopOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopOrderResponse from a JSON string
stop_order_response_instance = StopOrderResponse.from_json(json)
# print the JSON string representation of the object
print(StopOrderResponse.to_json())

# convert the object into a dict
stop_order_response_dict = stop_order_response_instance.to_dict()
# create an instance of StopOrderResponse from a dict
stop_order_response_from_dict = StopOrderResponse.from_dict(stop_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


