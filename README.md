# luno-openapi

The Luno API provides developers with a wealth of financial information provided through the Luno platform. Through this secure system developers can:

<ul>
   <li>Create accounts for trading in cryptocurrencies</li>
   <li>Access current and historic cryptocurrency market data</li>
   <li>Submit trade orders and view order status</li>
   <li>Buy and sell Bitcoin and Ethereum</li>
   <li>Send and receive Bitcoin and Ethereum</li>
   <li>Generate Bitcoin and Ethereum wallet addresses</li>
 </ul>

The Luno API brings the world of Bitcoin and Ethereum to your doorstep.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.2.3
- Package version: 1.2.3
- Generator version: 7.8.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements

Python 3.7+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ff137/luno_openapi.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ff137/luno_openapi.git`)

Then import the package:

```python
import luno_openapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import luno_openapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = luno_openapi.AccountsApi(api_client)
    currency = 'XBT' # str | The currency code for the Account you want to create.  Please see the Currency section for a detailed list of currencies supported by the Luno platform.  Users must be verified to trade currency in order to be able to create an Account.  For more information on the verification process, please see <a href=\"/help/en/articles/1000168396\">How do I verify my identity?</a>.  Users have a limit of 10 accounts per currency.
    name = 'Trading ACC' # str | The label to use for this account

    try:
        # Create account
        api_response = await api_instance.create_account(currency, name)
        print("The response of AccountsApi->create_account:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *<https://api.luno.com>*

| Class              | Method                                                                         | HTTP request                              | Description                         |
| ------------------ | ------------------------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| *AccountsApi*      | [**create_account**](docs/AccountsApi.md#create_account)                       | **POST** /api/1/accounts                  | Create account                      |
| *AccountsApi*      | [**get_balances**](docs/AccountsApi.md#get_balances)                           | **GET** /api/1/balance                    | List account balances               |
| *AccountsApi*      | [**get_move**](docs/AccountsApi.md#get_move)                                   | **GET** /api/exchange/1/move              | Move                                |
| *AccountsApi*      | [**list_moves**](docs/AccountsApi.md#list_moves)                               | **GET** /api/exchange/1/move/list_moves   | List Moves                          |
| *AccountsApi*      | [**list_pending_transactions**](docs/AccountsApi.md#list_pending_transactions) | **GET** /api/1/accounts/{id}/pending      | List pending transactions           |
| *AccountsApi*      | [**list_transactions**](docs/AccountsApi.md#list_transactions)                 | **GET** /api/1/accounts/{id}/transactions | List transactions                   |
| *AccountsApi*      | [**move**](docs/AccountsApi.md#move)                                           | **POST** /api/exchange/1/move             | Move                                |
| *AccountsApi*      | [**update_account_name**](docs/AccountsApi.md#update_account_name)             | **PUT** /api/1/accounts/{id}/name         | Update Account Name                 |
| *AddressApi*       | [**validate**](docs/AddressApi.md#validate)                                    | **POST** /api/1/address/validate          | Validate                            |
| *BeneficiariesApi* | [**create_beneficiary**](docs/BeneficiariesApi.md#create_beneficiary)          | **POST** /api/1/beneficiaries             | Create beneficiary                  |
| *BeneficiariesApi* | [**delete_beneficiary**](docs/BeneficiariesApi.md#delete_beneficiary)          | **DELETE** /api/1/beneficiaries/{id}      | Delete beneficiary                  |
| *BeneficiariesApi* | [**list_beneficiaries**](docs/BeneficiariesApi.md#list_beneficiaries)          | **GET** /api/1/beneficiaries              | List beneficiaries                  |
| *MarketApi*        | [**get_candles**](docs/MarketApi.md#get_candles)                               | **GET** /api/exchange/1/candles           | Get candles                         |
| *MarketApi*        | [**get_order_book**](docs/MarketApi.md#get_order_book)                         | **GET** /api/1/orderbook_top              | Get top order book                  |
| *MarketApi*        | [**get_order_book_full**](docs/MarketApi.md#get_order_book_full)               | **GET** /api/1/orderbook                  | Get full order book                 |
| *MarketApi*        | [**get_ticker**](docs/MarketApi.md#get_ticker)                                 | **GET** /api/1/ticker                     | Get ticker for currency pair        |
| *MarketApi*        | [**get_tickers**](docs/MarketApi.md#get_tickers)                               | **GET** /api/1/tickers                    | List tickers for all currency pairs |
| *MarketApi*        | [**list_trades**](docs/MarketApi.md#list_trades)                               | **GET** /api/1/trades                     | List recent trades                  |
| *MarketApi*        | [**markets**](docs/MarketApi.md#markets)                                       | **GET** /api/exchange/1/markets           | Get markets info                    |
| *OrdersApi*        | [**get_fee_info**](docs/OrdersApi.md#get_fee_info)                             | **GET** /api/1/fee_info                   | Get fee information                 |
| *OrdersApi*        | [**get_order**](docs/OrdersApi.md#get_order)                                   | **GET** /api/1/orders/{id}                | Get order                           |
| *OrdersApi*        | [**get_order_v2**](docs/OrdersApi.md#get_order_v2)                             | **GET** /api/exchange/2/orders/{id}       | Get Order v2                        |
| *OrdersApi*        | [**get_order_v3**](docs/OrdersApi.md#get_order_v3)                             | **GET** /api/exchange/3/order             | Get Order v3                        |
| *OrdersApi*        | [**list_orders**](docs/OrdersApi.md#list_orders)                               | **GET** /api/1/listorders                 | List orders                         |
| *OrdersApi*        | [**list_orders_v2**](docs/OrdersApi.md#list_orders_v2)                         | **GET** /api/exchange/2/listorders        | List Orders v2                      |
| *OrdersApi*        | [**list_user_trades**](docs/OrdersApi.md#list_user_trades)                     | **GET** /api/1/listtrades                 | List trades                         |
| *OrdersApi*        | [**post_limit_order**](docs/OrdersApi.md#post_limit_order)                     | **POST** /api/1/postorder                 | Post Limit Order                    |
| *OrdersApi*        | [**post_market_order**](docs/OrdersApi.md#post_market_order)                   | **POST** /api/1/marketorder               | Post Market Order                   |
| *OrdersApi*        | [**stop_order**](docs/OrdersApi.md#stop_order)                                 | **POST** /api/1/stoporder                 | Cancel Order                        |
| *ReceiveApi*       | [**create_funding_address**](docs/ReceiveApi.md#create_funding_address)        | **POST** /api/1/funding_address           | Create receive address              |
| *ReceiveApi*       | [**get_funding_address**](docs/ReceiveApi.md#get_funding_address)              | **GET** /api/1/funding_address            | Get receive address                 |
| *SendApi*          | [**send**](docs/SendApi.md#send)                                               | **POST** /api/1/send                      | Send                                |
| *SendApi*          | [**send_fee**](docs/SendApi.md#send_fee)                                       | **GET** /api/1/send_fee                   | Estimate send fees                  |
| *TransfersApi*     | [**cancel_withdrawal**](docs/TransfersApi.md#cancel_withdrawal)                | **DELETE** /api/1/withdrawals/{id}        | Cancel withdrawal request           |
| *TransfersApi*     | [**create_withdrawal**](docs/TransfersApi.md#create_withdrawal)                | **POST** /api/1/withdrawals               | Request a withdrawal                |
| *TransfersApi*     | [**get_withdrawal**](docs/TransfersApi.md#get_withdrawal)                      | **GET** /api/1/withdrawals/{id}           | Get withdrawal request              |
| *TransfersApi*     | [**list_transfers**](docs/TransfersApi.md#list_transfers)                      | **GET** /api/exchange/1/transfers         | List transfers                      |
| *TransfersApi*     | [**list_withdrawals**](docs/TransfersApi.md#list_withdrawals)                  | **GET** /api/1/withdrawals                | List withdrawal requests            |

## Documentation For Models

- [AccountBalance](docs/AccountBalance.md)
- [AccountInfo](docs/AccountInfo.md)
- [AddressMeta](docs/AddressMeta.md)
- [BalanceList](docs/BalanceList.md)
- [Beneficiary](docs/Beneficiary.md)
- [CancelWithdrawalResponse](docs/CancelWithdrawalResponse.md)
- [Candle](docs/Candle.md)
- [CreateAccountResponse](docs/CreateAccountResponse.md)
- [CreateBeneficiaryDefaultResponse](docs/CreateBeneficiaryDefaultResponse.md)
- [CreateBeneficiaryResponse](docs/CreateBeneficiaryResponse.md)
- [CreateFundingAddressResponse](docs/CreateFundingAddressResponse.md)
- [CreateWithdrawalResponse](docs/CreateWithdrawalResponse.md)
- [CryptoDetails](docs/CryptoDetails.md)
- [DetailFields](docs/DetailFields.md)
- [FeeInfo](docs/FeeInfo.md)
- [FundsMove](docs/FundsMove.md)
- [GetBalancesResponse](docs/GetBalancesResponse.md)
- [GetCandlesResponse](docs/GetCandlesResponse.md)
- [GetFeeInfoResponse](docs/GetFeeInfoResponse.md)
- [GetFundingAddressResponse](docs/GetFundingAddressResponse.md)
- [GetMoveResponse](docs/GetMoveResponse.md)
- [GetOrder2Response](docs/GetOrder2Response.md)
- [GetOrderBookResponse](docs/GetOrderBookResponse.md)
- [GetOrderResponse](docs/GetOrderResponse.md)
- [GetTickerResponse](docs/GetTickerResponse.md)
- [GetWithdrawalResponse](docs/GetWithdrawalResponse.md)
- [ListBeneficiariesResponse](docs/ListBeneficiariesResponse.md)
- [ListMovesResponse](docs/ListMovesResponse.md)
- [ListOrders2Response](docs/ListOrders2Response.md)
- [ListOrdersResponse](docs/ListOrdersResponse.md)
- [ListPendingTransactionsResponse](docs/ListPendingTransactionsResponse.md)
- [ListTickersResponse](docs/ListTickersResponse.md)
- [ListTradesResponse](docs/ListTradesResponse.md)
- [ListTransactionsResponse](docs/ListTransactionsResponse.md)
- [ListTransfersResponse](docs/ListTransfersResponse.md)
- [ListUserTradesResponse](docs/ListUserTradesResponse.md)
- [ListWithdrawalsResponse](docs/ListWithdrawalsResponse.md)
- [MarketInfo](docs/MarketInfo.md)
- [MarketsInfoResponse](docs/MarketsInfoResponse.md)
- [MoveResponse](docs/MoveResponse.md)
- [Order](docs/Order.md)
- [OrderBook](docs/OrderBook.md)
- [OrderBookEntry](docs/OrderBookEntry.md)
- [OrderV2](docs/OrderV2.md)
- [PostLimitOrderResponse](docs/PostLimitOrderResponse.md)
- [PostMarketOrderResponse](docs/PostMarketOrderResponse.md)
- [PublicTrade](docs/PublicTrade.md)
- [ReceiveAddress](docs/ReceiveAddress.md)
- [SendFeeResponse](docs/SendFeeResponse.md)
- [SendResponse](docs/SendResponse.md)
- [StopOrderResponse](docs/StopOrderResponse.md)
- [Ticker](docs/Ticker.md)
- [TradeDetails](docs/TradeDetails.md)
- [TradeV2](docs/TradeV2.md)
- [Transaction](docs/Transaction.md)
- [Transfer](docs/Transfer.md)
- [UpdateAccountNameResponse](docs/UpdateAccountNameResponse.md)
- [ValidateAddressResponse](docs/ValidateAddressResponse.md)
- [Withdrawal](docs/Withdrawal.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Endpoints do not require authorization.

## Author
