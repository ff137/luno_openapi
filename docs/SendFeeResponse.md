# SendFeeResponse

SendFeeResponse response object for send fee call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**fee** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.send_fee_response import SendFeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendFeeResponse from a JSON string
send_fee_response_instance = SendFeeResponse.from_json(json)
# print the JSON string representation of the object
print(SendFeeResponse.to_json())

# convert the object into a dict
send_fee_response_dict = send_fee_response_instance.to_dict()
# create an instance of SendFeeResponse from a dict
send_fee_response_from_dict = SendFeeResponse.from_dict(send_fee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


