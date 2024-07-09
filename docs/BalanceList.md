# BalanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**List[AccountBalance]**](AccountBalance.md) |  | [optional] 

## Example

```python
from luno_openapi.models.balance_list import BalanceList

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceList from a JSON string
balance_list_instance = BalanceList.from_json(json)
# print the JSON string representation of the object
print(BalanceList.to_json())

# convert the object into a dict
balance_list_dict = balance_list_instance.to_dict()
# create an instance of BalanceList from a dict
balance_list_from_dict = BalanceList.from_dict(balance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


