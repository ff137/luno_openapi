# luno_openapi.AddressApi

All URIs are relative to *https://api.luno.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate**](AddressApi.md#validate) | **POST** /api/1/address/validate | Validate


# **validate**
> ValidateAddressResponse validate(address, currency, address_name=address_name, has_destination_tag=has_destination_tag, destination_tag=destination_tag, memo=memo, is_self_send=is_self_send, is_private_wallet=is_private_wallet, wallet_name=wallet_name, beneficiary_name=beneficiary_name, is_legal_entity=is_legal_entity, institution_name=institution_name, country=country, physical_address=physical_address, nationality=nationality, date_of_birth=date_of_birth)

Validate

Validate receive addresses, to which a customer wishes to make cryptocurrency sends, are verified under covering regulatory requirements for the customer such as travel rules.  Permissions required: <code>Perm_W_Send</code>

### Example


```python
import luno_openapi
from luno_openapi.models.validate_address_response import ValidateAddressResponse
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
    api_instance = luno_openapi.AddressApi(api_client)
    address = '1AbbJJzevwFFVBKvZRtQHHFgrJyYTKaMw2' # str | Destination address or email address.  <b>Note</b>: <ul> <li>Ethereum addresses must be <a href=\"https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md\" target=\"_blank\" rel=\"nofollow\">checksummed</a>.</li> <li>Ethereum validations of email addresses are not supported.</li> </ul>
    currency = 'XBT' # str | Currency is the currency associated with the address.
    address_name = 'MyNamedAddress' # str | AddressName is the optional name under which to store the address as in the address book. (optional)
    has_destination_tag = true # bool | Optional boolean flag indicating that a XRP destination tag is provided (even if zero). (optional)
    destination_tag = 12345 # int | Optional XRP destination tag. Note that HasDestinationTag must be true if this value is provided. (optional)
    memo = 'Test:TEST-test ?;lsbjaciuq12712837519*T*&$^572' # str | Optional memo string used to provide account information for ATOM, etc. where it holds \"account\" information for a generic address. (optional)
    is_self_send = True # bool | IsSelfSend to indicate that the address belongs to the customer. If this field is true then the remaining omitempty fields should not be populated. (optional)
    is_private_wallet = True # bool | IsPrivateWallet indicates if the address is for private wallet and not held at an exchange. (optional)
    wallet_name = 'John Smith's Wallet or Luno or MX Exchange' # str | PrivateWalletName is the name of the private wallet (optional)
    beneficiary_name = 'John Smith' # str | BeneficiaryName is the name of the beneficial owner if is it is a private address (optional)
    is_legal_entity = True # bool | IsLegalEntity indicates if the address is for a legal entity and not a private beneficiary. If this field is true then the fields BeneficiaryName, Nationality & DateOfBirth should be empty but the fields InstitutionName and Country should be populated. If this field is false and IsSelfSend is false (or empty) then the field InstitutionName should be empty but the fields BeneficiaryName, Nationality & DateOfBirth and Country should be populated. (optional)
    institution_name = 'Some Co Ltd' # str | InstitutionName is the name of the beneficial owner if is it is a legal entities address (optional)
    country = 'MYS' # str | Country is the ISO 3166-1 country code of the beneficial owner of the address (optional)
    physical_address = '1970-01-01' # str | PhysicalAddress is the legal physical address of the beneficial owner of the crypto address (optional)
    nationality = 'MYS' # str | Nationality ISO 3166-1 country code of the nationality of the (non-institutional) beneficial owner of the address (optional)
    date_of_birth = '1970-01-01' # str | DateOfBirth is the date of birth of the (non-institutional) beneficial owner of the address in the form \"YYYY-MM-DD\" (optional)

    try:
        # Validate
        api_response = await api_instance.validate(address, currency, address_name=address_name, has_destination_tag=has_destination_tag, destination_tag=destination_tag, memo=memo, is_self_send=is_self_send, is_private_wallet=is_private_wallet, wallet_name=wallet_name, beneficiary_name=beneficiary_name, is_legal_entity=is_legal_entity, institution_name=institution_name, country=country, physical_address=physical_address, nationality=nationality, date_of_birth=date_of_birth)
        print("The response of AddressApi->validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Destination address or email address.  &lt;b&gt;Note&lt;/b&gt;: &lt;ul&gt; &lt;li&gt;Ethereum addresses must be &lt;a href&#x3D;\&quot;https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;nofollow\&quot;&gt;checksummed&lt;/a&gt;.&lt;/li&gt; &lt;li&gt;Ethereum validations of email addresses are not supported.&lt;/li&gt; &lt;/ul&gt; | 
 **currency** | **str**| Currency is the currency associated with the address. | 
 **address_name** | **str**| AddressName is the optional name under which to store the address as in the address book. | [optional] 
 **has_destination_tag** | **bool**| Optional boolean flag indicating that a XRP destination tag is provided (even if zero). | [optional] 
 **destination_tag** | **int**| Optional XRP destination tag. Note that HasDestinationTag must be true if this value is provided. | [optional] 
 **memo** | **str**| Optional memo string used to provide account information for ATOM, etc. where it holds \&quot;account\&quot; information for a generic address. | [optional] 
 **is_self_send** | **bool**| IsSelfSend to indicate that the address belongs to the customer. If this field is true then the remaining omitempty fields should not be populated. | [optional] 
 **is_private_wallet** | **bool**| IsPrivateWallet indicates if the address is for private wallet and not held at an exchange. | [optional] 
 **wallet_name** | **str**| PrivateWalletName is the name of the private wallet | [optional] 
 **beneficiary_name** | **str**| BeneficiaryName is the name of the beneficial owner if is it is a private address | [optional] 
 **is_legal_entity** | **bool**| IsLegalEntity indicates if the address is for a legal entity and not a private beneficiary. If this field is true then the fields BeneficiaryName, Nationality &amp; DateOfBirth should be empty but the fields InstitutionName and Country should be populated. If this field is false and IsSelfSend is false (or empty) then the field InstitutionName should be empty but the fields BeneficiaryName, Nationality &amp; DateOfBirth and Country should be populated. | [optional] 
 **institution_name** | **str**| InstitutionName is the name of the beneficial owner if is it is a legal entities address | [optional] 
 **country** | **str**| Country is the ISO 3166-1 country code of the beneficial owner of the address | [optional] 
 **physical_address** | **str**| PhysicalAddress is the legal physical address of the beneficial owner of the crypto address | [optional] 
 **nationality** | **str**| Nationality ISO 3166-1 country code of the nationality of the (non-institutional) beneficial owner of the address | [optional] 
 **date_of_birth** | **str**| DateOfBirth is the date of birth of the (non-institutional) beneficial owner of the address in the form \&quot;YYYY-MM-DD\&quot; | [optional] 

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.md)

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

