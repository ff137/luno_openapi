# Transfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount that has been credited or debited on the account. This is always a positive value regardless of the transfer direction. | [optional] 
**created_at** | **str** | Unix timestamp the transfer was initiated, in milliseconds | [optional] 
**fee** | **str** | Fee that has been charged by Luno with regards to this transfer. This is not included in the &#x60;amount&#x60;. For example, if you receive a transaction with the raw amount of 1 BTC and we charge a &#x60;fee&#x60; of 0.003 BTC on this transaction you will be credited the &#x60;amount&#x60; of 0.997 BTC. | [optional] 
**id** | **str** | Transfer unique identifier | [optional] 
**inbound** | **bool** | True for credit transfers, false for debits. | [optional] 
**transaction_id** | **str** | When the transfer reflects an on-chain transaction this field will have the transaction ID. | [optional] 

## Example

```python
from luno_openapi.models.transfer import Transfer

# TODO update the JSON string below
json = "{}"
# create an instance of Transfer from a JSON string
transfer_instance = Transfer.from_json(json)
# print the JSON string representation of the object
print(Transfer.to_json())

# convert the object into a dict
transfer_dict = transfer_instance.to_dict()
# create an instance of Transfer from a dict
transfer_from_dict = Transfer.from_dict(transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


