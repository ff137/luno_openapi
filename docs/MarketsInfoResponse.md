# MarketsInfoResponse

MarketsInfoResponse response for /api/2/markets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markets** | [**List[MarketInfo]**](MarketInfo.md) |  | [optional] 

## Example

```python
from luno_openapi.models.markets_info_response import MarketsInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketsInfoResponse from a JSON string
markets_info_response_instance = MarketsInfoResponse.from_json(json)
# print the JSON string representation of the object
print(MarketsInfoResponse.to_json())

# convert the object into a dict
markets_info_response_dict = markets_info_response_instance.to_dict()
# create an instance of MarketsInfoResponse from a dict
markets_info_response_from_dict = MarketsInfoResponse.from_dict(markets_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


