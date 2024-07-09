# CreateBeneficiaryDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique error reference | [optional] 
**message** | **str** | Verbose error message | [optional] 

## Example

```python
from luno_openapi.models.create_beneficiary_default_response import CreateBeneficiaryDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBeneficiaryDefaultResponse from a JSON string
create_beneficiary_default_response_instance = CreateBeneficiaryDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBeneficiaryDefaultResponse.to_json())

# convert the object into a dict
create_beneficiary_default_response_dict = create_beneficiary_default_response_instance.to_dict()
# create an instance of CreateBeneficiaryDefaultResponse from a dict
create_beneficiary_default_response_from_dict = CreateBeneficiaryDefaultResponse.from_dict(create_beneficiary_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


