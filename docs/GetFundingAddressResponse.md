# GetFundingAddressResponse

GetFundingAddressResponse get funding address response body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address_meta** | [**List[AddressMeta]**](AddressMeta.md) |  | [optional] 
**asset** | **str** |  | [optional] 
**assigned_at** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**qr_code_uri** | **str** |  | [optional] 
**receive_fee** | **str** |  | [optional] 
**total_received** | **str** |  | [optional] 
**total_unconfirmed** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.get_funding_address_response import GetFundingAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFundingAddressResponse from a JSON string
get_funding_address_response_instance = GetFundingAddressResponse.from_json(json)
# print the JSON string representation of the object
print(GetFundingAddressResponse.to_json())

# convert the object into a dict
get_funding_address_response_dict = get_funding_address_response_instance.to_dict()
# create an instance of GetFundingAddressResponse from a dict
get_funding_address_response_from_dict = GetFundingAddressResponse.from_dict(get_funding_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


