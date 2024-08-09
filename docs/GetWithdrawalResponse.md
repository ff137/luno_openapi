# GetWithdrawalResponse

GetWithdrawalResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount to withdraw | [optional] 
**created_at** | **int** | Unix time the withdrawal was initiated, in milliseconds | [optional] 
**currency** | **str** | Withdrawal currency. | [optional] 
**external_id** | **str** | External ID has the value that was passed in when the Withdrawal request was posted. | [optional] 
**fee** | **str** | Withdrawal fee | [optional] 
**id** | **str** |  | [optional] 
**status** | **str** | Status | [optional] 
**transfer_id** | **str** | Transfer ID is the identifier of the Withdrawal&#39;s transfer once it completes. | [optional] 
**type** | **str** | Type distinguishes between different withdrawal methods where more than one is supported for the given currency. | [optional] 

## Example

```python
from luno_openapi.models.get_withdrawal_response import GetWithdrawalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWithdrawalResponse from a JSON string
get_withdrawal_response_instance = GetWithdrawalResponse.from_json(json)
# print the JSON string representation of the object
print(GetWithdrawalResponse.to_json())

# convert the object into a dict
get_withdrawal_response_dict = get_withdrawal_response_instance.to_dict()
# create an instance of GetWithdrawalResponse from a dict
get_withdrawal_response_from_dict = GetWithdrawalResponse.from_dict(get_withdrawal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


