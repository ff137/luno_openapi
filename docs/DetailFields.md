# DetailFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_details** | [**CryptoDetails**](CryptoDetails.md) |  | [optional] 
**trade_details** | [**TradeDetails**](TradeDetails.md) |  | [optional] 

## Example

```python
from luno_openapi.models.detail_fields import DetailFields

# TODO update the JSON string below
json = "{}"
# create an instance of DetailFields from a JSON string
detail_fields_instance = DetailFields.from_json(json)
# print the JSON string representation of the object
print(DetailFields.to_json())

# convert the object into a dict
detail_fields_dict = detail_fields_instance.to_dict()
# create an instance of DetailFields from a dict
detail_fields_from_dict = DetailFields.from_dict(detail_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


