# luno_openapi.TransfersApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_withdrawal**](TransfersApi.md#cancel_withdrawal) | **DELETE** /api/1/withdrawals/{id} | Cancel withdrawal request
[**create_withdrawal**](TransfersApi.md#create_withdrawal) | **POST** /api/1/withdrawals | Request a withdrawal
[**get_withdrawal**](TransfersApi.md#get_withdrawal) | **GET** /api/1/withdrawals/{id} | Get withdrawal request
[**list_transfers**](TransfersApi.md#list_transfers) | **GET** /api/exchange/1/transfers | List transfers
[**list_withdrawals**](TransfersApi.md#list_withdrawals) | **GET** /api/1/withdrawals | List withdrawal requests


# **cancel_withdrawal**
> CancelWithdrawalResponse cancel_withdrawal(id)

Cancel withdrawal request

Cancels a withdrawal request. This can only be done if the request is still in state <code>PENDING</code>.  Permissions required: <code>Perm_W_Withdrawals</code>

### Example


```python
import luno_openapi
from luno_openapi.models.cancel_withdrawal_response import CancelWithdrawalResponse
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
    api_instance = luno_openapi.TransfersApi(api_client)
    id = 12345 # int | ID of the withdrawal to cancel.

    try:
        # Cancel withdrawal request
        api_response = await api_instance.cancel_withdrawal(id)
        print("The response of TransfersApi->cancel_withdrawal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->cancel_withdrawal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the withdrawal to cancel. | 

### Return type

[**CancelWithdrawalResponse**](CancelWithdrawalResponse.md)

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

# **create_withdrawal**
> CreateWithdrawalResponse create_withdrawal(type, amount, beneficiary_id=beneficiary_id, fast=fast, reference=reference, external_id=external_id)

Request a withdrawal

Creates a new withdrawal request to the specified beneficiary.  Permissions required: <code>Perm_W_Withdrawals</code>

### Example


```python
import luno_openapi
from luno_openapi.models.create_withdrawal_response import CreateWithdrawalResponse
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
    api_instance = luno_openapi.TransfersApi(api_client)
    type = 'ZAR_EFT' # str | Withdrawal method.
    amount = '10000.00' # str | Amount to withdraw. The currency withdrawn depends on the type setting.
    beneficiary_id = 12345 # int | The beneficiary ID of the bank account the withdrawal will be paid out to. This parameter is required if the user has set up multiple beneficiaries. The beneficiary ID can be found by selecting on the beneficiary name on the user’s <a href=\"/wallet/beneficiaries\">Beneficiaries</a> page. (optional)
    fast = False # bool | If true, it will be a fast withdrawal if possible. Fast withdrawals come with a fee. Currently fast withdrawals are only available for `type=ZAR_EFT`; for other types, an error is returned. Fast withdrawals are not possible for Bank of Baroda, Deutsche Bank, Merrill Lynch South Africa, UBS, Postbank and Tyme Bank. The fee to be charged is the same as when withdrawing from the UI. (optional) (default to False)
    reference = 'reference_example' # str | For internal use. Deprecated: We don't allow custom references and will remove this soon. (optional)
    external_id = '123e4567-e89b-12d3-a456-426655440000' # str | Optional unique ID to associate with this withdrawal. Useful to prevent duplicate sends. This field supports all alphanumeric characters including \"-\" and \"_\". (optional)

    try:
        # Request a withdrawal
        api_response = await api_instance.create_withdrawal(type, amount, beneficiary_id=beneficiary_id, fast=fast, reference=reference, external_id=external_id)
        print("The response of TransfersApi->create_withdrawal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->create_withdrawal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Withdrawal method. | 
 **amount** | **str**| Amount to withdraw. The currency withdrawn depends on the type setting. | 
 **beneficiary_id** | **int**| The beneficiary ID of the bank account the withdrawal will be paid out to. This parameter is required if the user has set up multiple beneficiaries. The beneficiary ID can be found by selecting on the beneficiary name on the user’s &lt;a href&#x3D;\&quot;/wallet/beneficiaries\&quot;&gt;Beneficiaries&lt;/a&gt; page. | [optional] 
 **fast** | **bool**| If true, it will be a fast withdrawal if possible. Fast withdrawals come with a fee. Currently fast withdrawals are only available for &#x60;type&#x3D;ZAR_EFT&#x60;; for other types, an error is returned. Fast withdrawals are not possible for Bank of Baroda, Deutsche Bank, Merrill Lynch South Africa, UBS, Postbank and Tyme Bank. The fee to be charged is the same as when withdrawing from the UI. | [optional] [default to False]
 **reference** | **str**| For internal use. Deprecated: We don&#39;t allow custom references and will remove this soon. | [optional] 
 **external_id** | **str**| Optional unique ID to associate with this withdrawal. Useful to prevent duplicate sends. This field supports all alphanumeric characters including \&quot;-\&quot; and \&quot;_\&quot;. | [optional] 

### Return type

[**CreateWithdrawalResponse**](CreateWithdrawalResponse.md)

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

# **get_withdrawal**
> GetWithdrawalResponse get_withdrawal(id)

Get withdrawal request

Returns the status of a particular withdrawal request.  Permissions required: <code>Perm_R_Withdrawals</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_withdrawal_response import GetWithdrawalResponse
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
    api_instance = luno_openapi.TransfersApi(api_client)
    id = 12345 # int | Withdrawal ID to retrieve.

    try:
        # Get withdrawal request
        api_response = await api_instance.get_withdrawal(id)
        print("The response of TransfersApi->get_withdrawal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->get_withdrawal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Withdrawal ID to retrieve. | 

### Return type

[**GetWithdrawalResponse**](GetWithdrawalResponse.md)

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

# **list_transfers**
> ListTransfersResponse list_transfers(account_id, limit=limit, before=before)

List transfers

Returns a list of the most recent confirmed transfers ordered from newest to oldest. This includes bank transfers, card payments, or on-chain transactions that have been reflected on your account available balance.  Note that the Transfer `amount` is always a positive value and you should use the `inbound` flag to determine the direction of the transfer.  If you need to paginate the results you can set the `before` parameter to the last returned transfer `created_at` field value and repeat the request until you have all the transfers you need. This endpoint will list up to 100 transfers at a time by default.  Permissions required: <Code>Perm_R_Transfers</Code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_transfers_response import ListTransfersResponse
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
    api_instance = luno_openapi.TransfersApi(api_client)
    account_id = 56 # int | Unique identifier of the account to list the transfers from.
    limit = 100 # int | Limit to this many transfers. (optional) (default to 100)
    before = 0 # int | Filter to transfers created before this timestamp (Unix milliseconds). The default value (0) will return the latest transfers on the account. (optional) (default to 0)

    try:
        # List transfers
        api_response = await api_instance.list_transfers(account_id, limit=limit, before=before)
        print("The response of TransfersApi->list_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->list_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Unique identifier of the account to list the transfers from. | 
 **limit** | **int**| Limit to this many transfers. | [optional] [default to 100]
 **before** | **int**| Filter to transfers created before this timestamp (Unix milliseconds). The default value (0) will return the latest transfers on the account. | [optional] [default to 0]

### Return type

[**ListTransfersResponse**](ListTransfersResponse.md)

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

# **list_withdrawals**
> ListWithdrawalsResponse list_withdrawals(before_id=before_id, limit=limit)

List withdrawal requests

Returns a list of withdrawal requests.  Permissions required: <code>Perm_R_Withdrawals</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_withdrawals_response import ListWithdrawalsResponse
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
    api_instance = luno_openapi.TransfersApi(api_client)
    before_id = 12345 # int | Filter to withdrawals requested on or before the withdrawal with this ID. Can be used for pagination. (optional)
    limit = 100 # int | Limit to this many withdrawals (optional) (default to 100)

    try:
        # List withdrawal requests
        api_response = await api_instance.list_withdrawals(before_id=before_id, limit=limit)
        print("The response of TransfersApi->list_withdrawals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->list_withdrawals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before_id** | **int**| Filter to withdrawals requested on or before the withdrawal with this ID. Can be used for pagination. | [optional] 
 **limit** | **int**| Limit to this many withdrawals | [optional] [default to 100]

### Return type

[**ListWithdrawalsResponse**](ListWithdrawalsResponse.md)

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

