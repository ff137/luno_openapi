# FeeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_fee** | **str** |  | [optional] 
**taker_fee** | **str** |  | [optional] 
**thirty_day_volume** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.fee_info import FeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeeInfo from a JSON string
fee_info_instance = FeeInfo.from_json(json)
# print the JSON string representation of the object
print(FeeInfo.to_json())

# convert the object into a dict
fee_info_dict = fee_info_instance.to_dict()
# create an instance of FeeInfo from a dict
fee_info_from_dict = FeeInfo.from_dict(fee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


