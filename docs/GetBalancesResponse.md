# GetBalancesResponse

GetBalancesResponse balance lookup response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**List[AccountBalance]**](AccountBalance.md) |  | [optional] 

## Example

```python
from luno_openapi.models.get_balances_response import GetBalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalancesResponse from a JSON string
get_balances_response_instance = GetBalancesResponse.from_json(json)
# print the JSON string representation of the object
print(GetBalancesResponse.to_json())

# convert the object into a dict
get_balances_response_dict = get_balances_response_instance.to_dict()
# create an instance of GetBalancesResponse from a dict
get_balances_response_from_dict = GetBalancesResponse.from_dict(get_balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


