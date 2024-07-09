# CreateFundingAddressResponse

CreateFundingAddressResponse create wallet response body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address_meta** | [**List[AddressMeta]**](AddressMeta.md) |  | [optional] 
**asset** | **str** |  | [optional] 
**assigned_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**qr_code_uri** | **str** |  | [optional] 
**receive_fee** | **str** |  | [optional] 
**total_received** | **str** |  | [optional] 
**total_unconfirmed** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.create_funding_address_response import CreateFundingAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFundingAddressResponse from a JSON string
create_funding_address_response_instance = CreateFundingAddressResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFundingAddressResponse.to_json())

# convert the object into a dict
create_funding_address_response_dict = create_funding_address_response_instance.to_dict()
# create an instance of CreateFundingAddressResponse from a dict
create_funding_address_response_from_dict = CreateFundingAddressResponse.from_dict(create_funding_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


