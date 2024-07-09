# ListWithdrawalsResponse

ListWithdrawalsResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdrawals** | [**List[Withdrawal]**](Withdrawal.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_withdrawals_response import ListWithdrawalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWithdrawalsResponse from a JSON string
list_withdrawals_response_instance = ListWithdrawalsResponse.from_json(json)
# print the JSON string representation of the object
print(ListWithdrawalsResponse.to_json())

# convert the object into a dict
list_withdrawals_response_dict = list_withdrawals_response_instance.to_dict()
# create an instance of ListWithdrawalsResponse from a dict
list_withdrawals_response_from_dict = ListWithdrawalsResponse.from_dict(list_withdrawals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


