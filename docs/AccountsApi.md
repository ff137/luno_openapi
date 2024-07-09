# luno_openapi.AccountsApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountsApi.md#create_account) | **POST** /api/1/accounts | Create account
[**get_balances**](AccountsApi.md#get_balances) | **GET** /api/1/balance | List account balances
[**get_move**](AccountsApi.md#get_move) | **GET** /api/exchange/1/move | Move
[**list_moves**](AccountsApi.md#list_moves) | **GET** /api/exchange/1/move/list_moves | List Moves
[**list_pending_transactions**](AccountsApi.md#list_pending_transactions) | **GET** /api/1/accounts/{id}/pending | List pending transactions
[**list_transactions**](AccountsApi.md#list_transactions) | **GET** /api/1/accounts/{id}/transactions | List transactions
[**move**](AccountsApi.md#move) | **POST** /api/exchange/1/move | Move
[**update_account_name**](AccountsApi.md#update_account_name) | **PUT** /api/1/accounts/{id}/name | Update Account Name


# **create_account**
> CreateAccountResponse create_account(currency, name)

Create account

This request creates an Account for the specified currency.  Please note that the balances for the Account will be displayed based on the <code>asset</code> value, which is the currency the Account is based on.  Permissions required: <code>Perm_W_Addresses</code>

### Example


```python
import luno_openapi
from luno_openapi.models.create_account_response import CreateAccountResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    currency = 'XBT' # str | The currency code for the Account you want to create.  Please see the Currency section for a detailed list of currencies supported by the Luno platform.  Users must be verified to trade currency in order to be able to create an Account.  For more information on the verification process, please see <a href=\"/help/en/articles/1000168396\">How do I verify my identity?</a>.  Users have a limit of 10 accounts per currency.
    name = 'Trading ACC' # str | The label to use for this account

    try:
        # Create account
        api_response = await api_instance.create_account(currency, name)
        print("The response of AccountsApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency code for the Account you want to create.  Please see the Currency section for a detailed list of currencies supported by the Luno platform.  Users must be verified to trade currency in order to be able to create an Account.  For more information on the verification process, please see &lt;a href&#x3D;\&quot;/help/en/articles/1000168396\&quot;&gt;How do I verify my identity?&lt;/a&gt;.  Users have a limit of 10 accounts per currency. | 
 **name** | **str**| The label to use for this account | 

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

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

# **get_balances**
> GetBalancesResponse get_balances(assets=assets)

List account balances

The list of all Accounts and their respective balances for the requesting user.  Permissions required: <code>Perm_R_Balance</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_balances_response import GetBalancesResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    assets = ['XBT'] # List[str] | Only return balances for wallets with these currencies (if not provided, all balances will be returned). To request balances for multiple currencies, pass the parameter multiple times, e.g. `assets=XBT&assets=ETH`. (optional)

    try:
        # List account balances
        api_response = await api_instance.get_balances(assets=assets)
        print("The response of AccountsApi->get_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assets** | [**List[str]**](str.md)| Only return balances for wallets with these currencies (if not provided, all balances will be returned). To request balances for multiple currencies, pass the parameter multiple times, e.g. &#x60;assets&#x3D;XBT&amp;assets&#x3D;ETH&#x60;. | [optional] 

### Return type

[**GetBalancesResponse**](GetBalancesResponse.md)

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

# **get_move**
> GetMoveResponse get_move(id=id, client_move_id=client_move_id)

Move

Get a specific move funds instruction by either <code>id</code> or <code>client_move_id</code>. If both are provided an API error will be returned.  Permissions required: <code>MP_None</code>

### Example


```python
import luno_openapi
from luno_openapi.models.get_move_response import GetMoveResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    id = '18563829047' # str | Get by the system ID. This is mutually exclusive with <code>client_move_id</code> and is required if <code>client_move_id</code> is not provided. (optional)
    client_move_id = 'mv-53960812' # str | Get by the user defined ID. This is mutually exclusive with <code>id</code> and is required if <code>id</code> is not provided. (optional)

    try:
        # Move
        api_response = await api_instance.get_move(id=id, client_move_id=client_move_id)
        print("The response of AccountsApi->get_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Get by the system ID. This is mutually exclusive with &lt;code&gt;client_move_id&lt;/code&gt; and is required if &lt;code&gt;client_move_id&lt;/code&gt; is not provided. | [optional] 
 **client_move_id** | **str**| Get by the user defined ID. This is mutually exclusive with &lt;code&gt;id&lt;/code&gt; and is required if &lt;code&gt;id&lt;/code&gt; is not provided. | [optional] 

### Return type

[**GetMoveResponse**](GetMoveResponse.md)

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

# **list_moves**
> ListMovesResponse list_moves(before=before, limit=limit)

List Moves

Returns a list of the most recent moves ordered from newest to oldest. This endpoint will list up to 100 most recent moves by default.  Permissions required: <code>MP_None</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_moves_response import ListMovesResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    before = 1530865703508 # int | Filter to moves requested before this timestamp (Unix milliseconds) (optional)
    limit = 100 # int | Limit to this many moves (optional) (default to 100)

    try:
        # List Moves
        api_response = await api_instance.list_moves(before=before, limit=limit)
        print("The response of AccountsApi->list_moves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_moves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| Filter to moves requested before this timestamp (Unix milliseconds) | [optional] 
 **limit** | **int**| Limit to this many moves | [optional] [default to 100]

### Return type

[**ListMovesResponse**](ListMovesResponse.md)

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

# **list_pending_transactions**
> ListPendingTransactionsResponse list_pending_transactions(id)

List pending transactions

Return a list of all transactions that have not completed for the Account.  Pending transactions are not numbered, and may be reordered, deleted or updated at any time.  Permissions required: <code>Perm_R_Transactions</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_pending_transactions_response import ListPendingTransactionsResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    id = 12345 # int | Account ID

    try:
        # List pending transactions
        api_response = await api_instance.list_pending_transactions(id)
        print("The response of AccountsApi->list_pending_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_pending_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Account ID | 

### Return type

[**ListPendingTransactionsResponse**](ListPendingTransactionsResponse.md)

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

# **list_transactions**
> ListTransactionsResponse list_transactions(id, min_row, max_row)

List transactions

Return a list of transaction entries from an account.  Transaction entry rows are numbered sequentially starting from 1, where 1 is the oldest entry. The range of rows to return are specified with the <code>min_row</code> (inclusive) and <code>max_row</code> (exclusive) parameters. At most 1000 rows can be requested per call.  If <code>min_row</code> or <code>max_row</code> is non-positive, the range wraps around the most recent row. For example, to fetch the 100 most recent rows, use <code>min_row=-100</code> and <code>max_row=0</code>.  Permissions required: <code>Perm_R_Transactions</code>

### Example


```python
import luno_openapi
from luno_openapi.models.list_transactions_response import ListTransactionsResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    id = 12345 # int | Account ID - the unique identifier for the specific Account.
    min_row = 1 # int | Minimum of the row range to return (inclusive)
    max_row = 1000 # int | Maximum of the row range to return (exclusive)

    try:
        # List transactions
        api_response = await api_instance.list_transactions(id, min_row, max_row)
        print("The response of AccountsApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Account ID - the unique identifier for the specific Account. | 
 **min_row** | **int**| Minimum of the row range to return (inclusive) | 
 **max_row** | **int**| Maximum of the row range to return (exclusive) | 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

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

# **move**
> MoveResponse move(amount, debit_account_id, credit_account_id, client_move_id=client_move_id)

Move

Move funds between two of your transactional accounts with the same currency The funds may not be moved by the time the request returns. The GET method can be used to poll for the move's status.  Note: moves will show as transactions, but not as transfers.  Permissions required: <code>MP_None_Write</code>

### Example


```python
import luno_openapi
from luno_openapi.models.move_response import MoveResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    amount = '10000.00' # str | Amount to transfer. Must be positive.
    debit_account_id = 12345 # int | The account to debit the funds from.
    credit_account_id = 12345 # int | The account to credit the funds to.
    client_move_id = 'mv-53960812' # str | Client move ID. May only contain alphanumeric (0-9, a-z, or A-Z) and special characters (_ ; , . -). Maximum length: 255. It will be available in read endpoints, so you can use it to avoid duplicate moves between the same accounts. Values must be unique across all your successful calls of this endpoint; trying to create a move request with the same `client_move_id` as one of your past move requests will result in a HTTP 409 Conflict response. (optional)

    try:
        # Move
        api_response = await api_instance.move(amount, debit_account_id, credit_account_id, client_move_id=client_move_id)
        print("The response of AccountsApi->move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**| Amount to transfer. Must be positive. | 
 **debit_account_id** | **int**| The account to debit the funds from. | 
 **credit_account_id** | **int**| The account to credit the funds to. | 
 **client_move_id** | **str**| Client move ID. May only contain alphanumeric (0-9, a-z, or A-Z) and special characters (_ ; , . -). Maximum length: 255. It will be available in read endpoints, so you can use it to avoid duplicate moves between the same accounts. Values must be unique across all your successful calls of this endpoint; trying to create a move request with the same &#x60;client_move_id&#x60; as one of your past move requests will result in a HTTP 409 Conflict response. | [optional] 

### Return type

[**MoveResponse**](MoveResponse.md)

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

# **update_account_name**
> UpdateAccountNameResponse update_account_name(id, name)

Update Account Name

Update the name of an account with a given ID.  Permissions required: <code>Perm_W_Addresses</code>

### Example


```python
import luno_openapi
from luno_openapi.models.update_account_name_response import UpdateAccountNameResponse
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
    api_instance = luno_openapi.AccountsApi(api_client)
    id = 12345 # int | Account ID - the unique identifier for the specific Account.
    name = 'Trading ACC' # str | The label to use for this account

    try:
        # Update Account Name
        api_response = await api_instance.update_account_name(id, name)
        print("The response of AccountsApi->update_account_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Account ID - the unique identifier for the specific Account. | 
 **name** | **str**| The label to use for this account | 

### Return type

[**UpdateAccountNameResponse**](UpdateAccountNameResponse.md)

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

