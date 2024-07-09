# ListTransactionsResponse

ListTransactionsResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**transactions** | [**List[Transaction]**](Transaction.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_transactions_response import ListTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsResponse from a JSON string
list_transactions_response_instance = ListTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListTransactionsResponse.to_json())

# convert the object into a dict
list_transactions_response_dict = list_transactions_response_instance.to_dict()
# create an instance of ListTransactionsResponse from a dict
list_transactions_response_from_dict = ListTransactionsResponse.from_dict(list_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


