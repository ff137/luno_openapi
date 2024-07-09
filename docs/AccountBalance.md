# AccountBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account. | [optional] 
**asset** | **str** | Currency code for the asset held in this account. | [optional] 
**balance** | **str** | The amount available to send or trade. | [optional] 
**name** | **str** | The name set by the user upon creating the account. | [optional] 
**reserved** | **str** | Amount locked by Luno and cannot be sent or traded. This could be due to open orders. | [optional] 
**unconfirmed** | **str** | Amount that is awaiting some sort of verification to be credited to this account. This could be an on-chain transaction that Luno is waiting for further block verifications to happen. | [optional] 

## Example

```python
from luno_openapi.models.account_balance import AccountBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBalance from a JSON string
account_balance_instance = AccountBalance.from_json(json)
# print the JSON string representation of the object
print(AccountBalance.to_json())

# convert the object into a dict
account_balance_dict = account_balance_instance.to_dict()
# create an instance of AccountBalance from a dict
account_balance_from_dict = AccountBalance.from_dict(account_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


