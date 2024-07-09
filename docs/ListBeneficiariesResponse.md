# ListBeneficiariesResponse

ListBeneficiariesResponse response object for list beneficiaries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiaries** | [**List[Beneficiary]**](Beneficiary.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_beneficiaries_response import ListBeneficiariesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBeneficiariesResponse from a JSON string
list_beneficiaries_response_instance = ListBeneficiariesResponse.from_json(json)
# print the JSON string representation of the object
print(ListBeneficiariesResponse.to_json())

# convert the object into a dict
list_beneficiaries_response_dict = list_beneficiaries_response_instance.to_dict()
# create an instance of ListBeneficiariesResponse from a dict
list_beneficiaries_response_from_dict = ListBeneficiariesResponse.from_dict(list_beneficiaries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


