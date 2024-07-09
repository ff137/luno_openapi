# GetMoveResponse

GetMoveResponse response for GET /1/move

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The assets quantity to move from the debit account to credit account. This is always a positive value. | [optional] 
**client_move_id** | **str** | User defined unique ID | [optional] 
**created_at** | **str** | Unix time the move was initiated, in milliseconds | [optional] 
**credit_account_id** | **str** | The account to credit the funds to. | [optional] 
**debit_account_id** | **str** | The account to debit the funds from. | [optional] 
**id** | **str** | Unique ID, defined by Luno | [optional] 
**status** | **str** | Current status of the move.  Status meaning:&lt;br&gt; &lt;code&gt;CREATED&lt;/code&gt; The move is awaiting execution.&lt;br&gt; &lt;code&gt;MOVING&lt;/code&gt; The funds have been reserved and the move is being executed.&lt;br&gt; &lt;code&gt;SUCCESSFUL&lt;/code&gt; The move has completed successfully and should be reflected in both accounts available balance.&lt;br&gt; &lt;code&gt;FAILED&lt;/code&gt; The move has failed. There could be many reasons for this but the most likely is that the debit account doesn&#39;t have enough available funds to move.&lt;br&gt; | [optional] 
**updated_at** | **str** | Unix time the move was last updated, in milliseconds | [optional] 

## Example

```python
from luno_openapi.models.get_move_response import GetMoveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMoveResponse from a JSON string
get_move_response_instance = GetMoveResponse.from_json(json)
# print the JSON string representation of the object
print(GetMoveResponse.to_json())

# convert the object into a dict
get_move_response_dict = get_move_response_instance.to_dict()
# create an instance of GetMoveResponse from a dict
get_move_response_from_dict = GetMoveResponse.from_dict(get_move_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


