# luno_openapi.BeneficiariesApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_beneficiary**](BeneficiariesApi.md#create_beneficiary) | **POST** /api/1/beneficiaries | Create beneficiary
[**delete_beneficiary**](BeneficiariesApi.md#delete_beneficiary) | **DELETE** /api/1/beneficiaries/{id} | Delete beneficiary
[**list_beneficiaries**](BeneficiariesApi.md#list_beneficiaries) | **GET** /api/1/beneficiaries | List beneficiaries


# **create_beneficiary**
> CreateBeneficiaryResponse create_beneficiary(bank_name, bank_account_number, account_type, bank_recipient)

Create beneficiary

Create a new beneficiary.  Permissions required: <code>Perm_W_Beneficiaries</code>

### Example


```python
import luno_openapi
from luno_openapi.models.create_beneficiary_response import CreateBeneficiaryResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.BeneficiariesApi(api_client)
    bank_name = 'FIRNZAJJ' # str | Bank SWIFT code
    bank_account_number = '9234101100063672' # str | Beneficiary bank account number
    account_type = 'account_type_example' # str | Bank account type
    bank_recipient = 'bank_recipient_example' # str | The owner of the recipient account

    try:
        # Create beneficiary
        api_response = await api_instance.create_beneficiary(bank_name, bank_account_number, account_type, bank_recipient)
        print("The response of BeneficiariesApi->create_beneficiary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BeneficiariesApi->create_beneficiary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_name** | **str**| Bank SWIFT code | 
 **bank_account_number** | **str**| Beneficiary bank account number | 
 **account_type** | **str**| Bank account type | 
 **bank_recipient** | **str**| The owner of the recipient account | 

### Return type

[**CreateBeneficiaryResponse**](CreateBeneficiaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_beneficiary**
> delete_beneficiary(id)

Delete beneficiary

Delete a beneficiary  Permissions required: <code>Perm_W_Beneficiaries</code>

### Example


```python
import luno_openapi
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.BeneficiariesApi(api_client)
    id = 12345 # int | ID of the Beneficiary to delete.

    try:
        # Delete beneficiary
        await api_instance.delete_beneficiary(id)
    except Exception as e:
        print("Exception when calling BeneficiariesApi->delete_beneficiary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the Beneficiary to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Beneficiary was deleted successfully |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_beneficiaries**
> ListBeneficiariesResponse list_beneficiaries(bank_recipient=bank_recipient)

List beneficiaries

Returns a list of bank beneficiaries.  Permissions required: <code>Perm_R_Beneficiaries</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_beneficiaries_response import ListBeneficiariesResponse
from luno_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.luno.com
# See configuration.py for a list of all supported configuration parameters.
configuration = luno_openapi.Configuration(
    host = "https://api.luno.com"
)


# Enter a context with an instance of the API client
async with luno_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = luno_openapi.BeneficiariesApi(api_client)
    bank_recipient = 'John* or *Smith or *John*' # str |  (optional)

    try:
        # List beneficiaries
        api_response = await api_instance.list_beneficiaries(bank_recipient=bank_recipient)
        print("The response of BeneficiariesApi->list_beneficiaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BeneficiariesApi->list_beneficiaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_recipient** | **str**|  | [optional] 

### Return type

[**ListBeneficiariesResponse**](ListBeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

