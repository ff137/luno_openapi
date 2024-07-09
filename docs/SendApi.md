# luno_openapi.SendApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send**](SendApi.md#send) | **POST** /api/1/send | Send
[**send_fee**](SendApi.md#send_fee) | **GET** /api/1/send_fee | Estimate send fees


# **send**
> SendResponse send(amount, currency, address, description=description, message=message, external_id=external_id, has_destination_tag=has_destination_tag, destination_tag=destination_tag, memo=memo, is_forex_send=is_forex_send, is_drb=is_drb, forex_notice_self_declaration=forex_notice_self_declaration, account_id=account_id)

Send

Send assets from an Account. Please note that the asset type sent must match the receive address of the same cryptocurrency of the same type - Bitcoin to Bitcoin, Ethereum to Ethereum, etc.  Sends can be made to cryptocurrency receive addresses.  <b>Note:</b> This is currently unavailable to users who are verified in countries with money travel rules.  Permissions required: <code>Perm_W_Send</code>

### Example


```python
import luno_openapi
from luno_openapi.models.send_response import SendResponse
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
    api_instance = luno_openapi.SendApi(api_client)
    amount = '1.5' # str | Amount to send as a decimal string.
    currency = 'XBT' # str | Currency to send.
    address = '1AbbJJzevwFFVBKvZRtQHHFgrJyYTKaMw2' # str | Destination address or email address.  <b>Note</b>: <ul> <li>Ethereum addresses must be <a href=\"https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md\" target=\"_blank\" rel=\"nofollow\">checksummed</a>.</li> <li>Ethereum sends to email addresses are not supported.</li> </ul>
    description = 'My description' # str | User description for the transaction to record on the account statement. (optional)
    message = 'My message' # str | Message to send to the recipient. This is only relevant when sending to an email address. (optional)
    external_id = '123e4567-e89b-12d3-a456-426655440000' # str | Optional unique ID to associate with this withdrawal. Useful to prevent duplicate sends in case of failure. This supports all alphanumeric characters, as well as \"-\" and \"_\". (optional)
    has_destination_tag = true # bool | Optional boolean flag indicating that a XRP destination tag is provided (even if zero). (optional)
    destination_tag = 12345 # int | Optional XRP destination tag. Note that HasDestinationTag must be true if this value is provided. (optional)
    memo = 'Test:TEST-test ?;lsbjaciuq12712837519*T*&$^572' # str | Optional memo string used to provide account information for ATOM, etc. where it holds \"account\" information for a generic address. (optional)
    is_forex_send = true # bool | Only required for Foreign Exchange Notification under the Malaysia FEN rules. IsForexSend must be true if sending to an address hosted outside of Malaysia. (optional)
    is_drb = true # bool | Only required for Foreign Exchange Notification under the Malaysia FEN rules. IsDRB must be true if the user has Domestic Ringgit Borrowing (DRB). (optional)
    forex_notice_self_declaration = true # bool | Only required for Foreign Exchange Notification under the Malaysia FEN rules. ForexNoticeSelfDeclaration must be true if the user has exceeded his/her annual investment limit in foreign currency assets. (optional)
    account_id = 5998716001549232000 # int | Optional source account. In case of multiple accounts for a single currency, the source account that will provide the funds for the transaction may be specified. If omitted, the default account will be used. (optional)

    try:
        # Send
        api_response = await api_instance.send(amount, currency, address, description=description, message=message, external_id=external_id, has_destination_tag=has_destination_tag, destination_tag=destination_tag, memo=memo, is_forex_send=is_forex_send, is_drb=is_drb, forex_notice_self_declaration=forex_notice_self_declaration, account_id=account_id)
        print("The response of SendApi->send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**| Amount to send as a decimal string. | 
 **currency** | **str**| Currency to send. | 
 **address** | **str**| Destination address or email address.  &lt;b&gt;Note&lt;/b&gt;: &lt;ul&gt; &lt;li&gt;Ethereum addresses must be &lt;a href&#x3D;\&quot;https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;nofollow\&quot;&gt;checksummed&lt;/a&gt;.&lt;/li&gt; &lt;li&gt;Ethereum sends to email addresses are not supported.&lt;/li&gt; &lt;/ul&gt; | 
 **description** | **str**| User description for the transaction to record on the account statement. | [optional] 
 **message** | **str**| Message to send to the recipient. This is only relevant when sending to an email address. | [optional] 
 **external_id** | **str**| Optional unique ID to associate with this withdrawal. Useful to prevent duplicate sends in case of failure. This supports all alphanumeric characters, as well as \&quot;-\&quot; and \&quot;_\&quot;. | [optional] 
 **has_destination_tag** | **bool**| Optional boolean flag indicating that a XRP destination tag is provided (even if zero). | [optional] 
 **destination_tag** | **int**| Optional XRP destination tag. Note that HasDestinationTag must be true if this value is provided. | [optional] 
 **memo** | **str**| Optional memo string used to provide account information for ATOM, etc. where it holds \&quot;account\&quot; information for a generic address. | [optional] 
 **is_forex_send** | **bool**| Only required for Foreign Exchange Notification under the Malaysia FEN rules. IsForexSend must be true if sending to an address hosted outside of Malaysia. | [optional] 
 **is_drb** | **bool**| Only required for Foreign Exchange Notification under the Malaysia FEN rules. IsDRB must be true if the user has Domestic Ringgit Borrowing (DRB). | [optional] 
 **forex_notice_self_declaration** | **bool**| Only required for Foreign Exchange Notification under the Malaysia FEN rules. ForexNoticeSelfDeclaration must be true if the user has exceeded his/her annual investment limit in foreign currency assets. | [optional] 
 **account_id** | **int**| Optional source account. In case of multiple accounts for a single currency, the source account that will provide the funds for the transaction may be specified. If omitted, the default account will be used. | [optional] 

### Return type

[**SendResponse**](SendResponse.md)

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

# **send_fee**
> SendFeeResponse send_fee(amount, currency, address)

Estimate send fees

Calculate fees involved with a crypto send request.  Send address can be to a cryptocurrency receive address, or the email address of another Luno platform user.  Permissions required: <code>MP_None</code>

### Example


```python
import luno_openapi
from luno_openapi.models.send_fee_response import SendFeeResponse
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
    api_instance = luno_openapi.SendApi(api_client)
    amount = '1.5' # str | Amount to send as a decimal string.
    currency = 'XBT' # str | Currency to send.
    address = '1AbbJJzevwFFVBKvZRtQHHFgrJyYTKaMw2' # str | Destination address or email address.  <b>Note</b>: <ul> <li>Ethereum addresses must be <a href=\"https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md\" target=\"_blank\" rel=\"nofollow\">checksummed</a>.</li> <li>Ethereum sends to email addresses are not supported.</li> </ul>

    try:
        # Estimate send fees
        api_response = await api_instance.send_fee(amount, currency, address)
        print("The response of SendApi->send_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**| Amount to send as a decimal string. | 
 **currency** | **str**| Currency to send. | 
 **address** | **str**| Destination address or email address.  &lt;b&gt;Note&lt;/b&gt;: &lt;ul&gt; &lt;li&gt;Ethereum addresses must be &lt;a href&#x3D;\&quot;https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;nofollow\&quot;&gt;checksummed&lt;/a&gt;.&lt;/li&gt; &lt;li&gt;Ethereum sends to email addresses are not supported.&lt;/li&gt; &lt;/ul&gt; | 

### Return type

[**SendFeeResponse**](SendFeeResponse.md)

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

