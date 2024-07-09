# MoveResponse

MoveResponse response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Move unique identifier | [optional] 
**status** | **str** | The current state of the move.  Status meaning:&lt;br&gt; &lt;code&gt;CREATED&lt;/code&gt; The move is awaiting execution.&lt;br&gt; &lt;code&gt;MOVING&lt;/code&gt; The funds have been reserved and the move is being executed.&lt;br&gt; &lt;code&gt;SUCCESSFUL&lt;/code&gt; The move has completed successfully and should be reflected in both accounts available balance.&lt;br&gt; &lt;code&gt;FAILED&lt;/code&gt; The move has failed. There could be many reasons for this but the most likely is that the debit account doesn&#39;t have enough available funds to move.&lt;br&gt; | [optional] 

## Example

```python
from luno_openapi.models.move_response import MoveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MoveResponse from a JSON string
move_response_instance = MoveResponse.from_json(json)
# print the JSON string representation of the object
print(MoveResponse.to_json())

# convert the object into a dict
move_response_dict = move_response_instance.to_dict()
# create an instance of MoveResponse from a dict
move_response_from_dict = MoveResponse.from_dict(move_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


