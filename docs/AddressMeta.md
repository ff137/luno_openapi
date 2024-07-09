# AddressMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.address_meta import AddressMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AddressMeta from a JSON string
address_meta_instance = AddressMeta.from_json(json)
# print the JSON string representation of the object
print(AddressMeta.to_json())

# convert the object into a dict
address_meta_dict = address_meta_instance.to_dict()
# create an instance of AddressMeta from a dict
address_meta_from_dict = AddressMeta.from_dict(address_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


