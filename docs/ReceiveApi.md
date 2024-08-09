# luno_openapi.ReceiveApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_funding_address**](ReceiveApi.md#create_funding_address) | **POST** /api/1/funding_address | Create receive address
[**get_funding_address**](ReceiveApi.md#get_funding_address) | **GET** /api/1/funding_address | Get receive address


# **create_funding_address**
> CreateFundingAddressResponse create_funding_address(asset, name=name, account_id=account_id)

Create receive address

Allocates a new receive address to your account. There is a rate limit of 1 address per hour, but bursts of up to 10 addresses are allowed. Only 1 Ethereum receive address can be created.  Permissions required: <code>Perm_W_Addresses</code>

### Example


```python
import luno_openapi
from luno_openapi.models.create_funding_address_response import CreateFundingAddressResponse
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
    api_instance = luno_openapi.ReceiveApi(api_client)
    asset = 'XBT' # str | Currency code of the asset.
    name = 'My BTC wallet' # str | An optional name for the new Receive Address (optional)
    account_id = 12345 # int | An optional account_id to assign the new Receive Address too (optional)

    try:
        # Create receive address
        api_response = await api_instance.create_funding_address(asset, name=name, account_id=account_id)
        print("The response of ReceiveApi->create_funding_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiveApi->create_funding_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Currency code of the asset. | 
 **name** | **str**| An optional name for the new Receive Address | [optional] 
 **account_id** | **int**| An optional account_id to assign the new Receive Address too | [optional] 

### Return type

[**CreateFundingAddressResponse**](CreateFundingAddressResponse.md)

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

# **get_funding_address**
> GetFundingAddressResponse get_funding_address(asset, address=address)

Get receive address

Returns the default receive address associated with your account and the amount received via the address. Users can specify an optional address parameter to return information for a non-default receive address. In the response, <code>total_received</code> is the total confirmed amount received excluding unconfirmed transactions. <code>total_unconfirmed</code> is the total sum of unconfirmed receive transactions.  Permissions required: <code>Perm_R_Addresses</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_funding_address_response import GetFundingAddressResponse
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
    api_instance = luno_openapi.ReceiveApi(api_client)
    asset = 'XBT' # str | Currency code of the asset.
    address = '1AbbJJzevwFFVBKvZRtQHHFgrJyYTKaMw2' # str | Specific cryptocurrency address to retrieve. If not provided, the default address will be used. (optional)

    try:
        # Get receive address
        api_response = await api_instance.get_funding_address(asset, address=address)
        print("The response of ReceiveApi->get_funding_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiveApi->get_funding_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Currency code of the asset. | 
 **address** | **str**| Specific cryptocurrency address to retrieve. If not provided, the default address will be used. | [optional] 

### Return type

[**GetFundingAddressResponse**](GetFundingAddressResponse.md)

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

