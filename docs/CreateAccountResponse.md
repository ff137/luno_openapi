# CreateAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.create_account_response import CreateAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountResponse from a JSON string
create_account_response_instance = CreateAccountResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAccountResponse.to_json())

# convert the object into a dict
create_account_response_dict = create_account_response_instance.to_dict()
# create an instance of CreateAccountResponse from a dict
create_account_response_from_dict = CreateAccountResponse.from_dict(create_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


