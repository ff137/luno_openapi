# Candle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close** | **str** | Closing price | [optional] 
**high** | **str** | High price | [optional] 
**low** | **str** | Low price | [optional] 
**open** | **str** | Opening price | [optional] 
**timestamp** | **str** | Unix timestamp in milliseconds | [optional] 
**volume** | **str** | Volume traded | [optional] 

## Example

```python
from luno_openapi.models.candle import Candle

# TODO update the JSON string below
json = "{}"
# create an instance of Candle from a JSON string
candle_instance = Candle.from_json(json)
# print the JSON string representation of the object
print(Candle.to_json())

# convert the object into a dict
candle_dict = candle_instance.to_dict()
# create an instance of Candle from a dict
candle_from_dict = Candle.from_dict(candle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


