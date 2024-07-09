# CryptoDetails

CryptoDetails contains a transaction's cryptocurrency address and transaction id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**txid** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.crypto_details import CryptoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoDetails from a JSON string
crypto_details_instance = CryptoDetails.from_json(json)
# print the JSON string representation of the object
print(CryptoDetails.to_json())

# convert the object into a dict
crypto_details_dict = crypto_details_instance.to_dict()
# create an instance of CryptoDetails from a dict
crypto_details_from_dict = CryptoDetails.from_dict(crypto_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


