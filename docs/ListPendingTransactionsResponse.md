# ListPendingTransactionsResponse

ListPendingTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**pending** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**transactions** | [**List[Transaction]**](Transaction.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_pending_transactions_response import ListPendingTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPendingTransactionsResponse from a JSON string
list_pending_transactions_response_instance = ListPendingTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPendingTransactionsResponse.to_json())

# convert the object into a dict
list_pending_transactions_response_dict = list_pending_transactions_response_instance.to_dict()
# create an instance of ListPendingTransactionsResponse from a dict
list_pending_transactions_response_from_dict = ListPendingTransactionsResponse.from_dict(list_pending_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


