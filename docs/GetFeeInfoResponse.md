# GetFeeInfoResponse

GetFeeInfoResponse response object for get fee info calls

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_fee** | **str** |  | [optional] 
**taker_fee** | **str** |  | [optional] 
**thirty_day_volume** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.get_fee_info_response import GetFeeInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeeInfoResponse from a JSON string
get_fee_info_response_instance = GetFeeInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeeInfoResponse.to_json())

# convert the object into a dict
get_fee_info_response_dict = get_fee_info_response_instance.to_dict()
# create an instance of GetFeeInfoResponse from a dict
get_fee_info_response_from_dict = GetFeeInfoResponse.from_dict(get_fee_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


