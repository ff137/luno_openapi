# Beneficiary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_branch** | **str** | Bank branch code | [optional] 
**bank_account_number** | **str** | Beneficiary bank account number | [optional] 
**bank_account_type** | **str** | Bank account type | [optional] 
**bank_country** | **str** | Bank country of origin | [optional] 
**bank_name** | **str** | Bank SWIFT code | [optional] 
**bank_recipient** | **str** | The owner of the recipient account | [optional] 
**created_at** | **int** | Time of beneficiary creation | [optional] 
**id** | **str** | Unique id referencing beneficiary | [optional] 
**supports_fast_withdrawals** | **bool** | If the bank account supports fast withdrawals | [optional] 

## Example

```python
from luno_openapi.models.beneficiary import Beneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of Beneficiary from a JSON string
beneficiary_instance = Beneficiary.from_json(json)
# print the JSON string representation of the object
print(Beneficiary.to_json())

# convert the object into a dict
beneficiary_dict = beneficiary_instance.to_dict()
# create an instance of Beneficiary from a dict
beneficiary_from_dict = Beneficiary.from_dict(beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


