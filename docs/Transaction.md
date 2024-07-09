# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**available** | **str** | Amount available | [optional] 
**available_delta** | **str** | Change in amount available | [optional] 
**balance** | **str** | Account balance | [optional] 
**balance_delta** | **str** | Change in balance | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** | Human-readable description of the transaction. | [optional] 
**detail_fields** | [**DetailFields**](DetailFields.md) |  | [optional] 
**details** | **Dict[str, str]** | Human-readable label-value attributes. | [optional] 
**kind** | **str** | The kind of the transaction indicates the transaction flow  Kinds explained:&lt;br&gt; &lt;code&gt;FEE&lt;/code&gt; when transaction is towards Luno fees&lt;br&gt; &lt;code&gt;TRANSFER&lt;/code&gt; when the transaction is a one way flow of funds, e.g. a deposit or crypto send&lt;br&gt; &lt;code&gt;EXCHANGE&lt;/code&gt; when the transaction is part of a two way exchange, e.g. a trade or instant buy | [optional] 
**reference** | **str** | A unique reference for the transaction this statement entry relates to. There may be multiple statement entries related to the same transaction. E.g. a withdrawal and the withdrawal fee are two separate statement entries with the same reference. | [optional] 
**row_index** | **int** |  | [optional] 
**timestamp** | **str** | Unix timestamp, in milliseconds | [optional] 

## Example

```python
from luno_openapi.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


