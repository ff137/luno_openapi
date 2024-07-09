# CreateBeneficiaryResponse

CreateBeneficiaryResponse response object for creating beneficiaries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from luno_openapi.models.create_beneficiary_response import CreateBeneficiaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBeneficiaryResponse from a JSON string
create_beneficiary_response_instance = CreateBeneficiaryResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBeneficiaryResponse.to_json())

# convert the object into a dict
create_beneficiary_response_dict = create_beneficiary_response_instance.to_dict()
# create an instance of CreateBeneficiaryResponse from a dict
create_beneficiary_response_from_dict = CreateBeneficiaryResponse.from_dict(create_beneficiary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


