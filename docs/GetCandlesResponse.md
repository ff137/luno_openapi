# GetCandlesResponse

GetCandlesResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candles** | [**List[Candle]**](Candle.md) |  | [optional] 
**duration** | **int** | Duration in seconds | [optional] 
**pair** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.get_candles_response import GetCandlesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCandlesResponse from a JSON string
get_candles_response_instance = GetCandlesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCandlesResponse.to_json())

# convert the object into a dict
get_candles_response_dict = get_candles_response_instance.to_dict()
# create an instance of GetCandlesResponse from a dict
get_candles_response_from_dict = GetCandlesResponse.from_dict(get_candles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


