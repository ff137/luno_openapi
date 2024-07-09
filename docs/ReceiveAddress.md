# ReceiveAddress

AddressResp wallet address response body

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
from luno_openapi.models.receive_address import ReceiveAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiveAddress from a JSON string
receive_address_instance = ReceiveAddress.from_json(json)
# print the JSON string representation of the object
print(ReceiveAddress.to_json())

# convert the object into a dict
receive_address_dict = receive_address_instance.to_dict()
# create an instance of ReceiveAddress from a dict
receive_address_from_dict = ReceiveAddress.from_dict(receive_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


