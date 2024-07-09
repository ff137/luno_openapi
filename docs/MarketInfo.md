# MarketInfo

MarketInfo current market information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | Base currency code | [optional] 
**counter_currency** | **str** | Counter currency code | [optional] 
**fee_scale** | **int** | Fee decimal places | [optional] 
**market_id** | **str** | Unique identifier for the market | [optional] 
**max_price** | **str** | Maximum order price | [optional] 
**max_volume** | **str** | Maximum order volume | [optional] 
**min_price** | **str** | Minimum order price | [optional] 
**min_volume** | **str** | Minimum order volume | [optional] 
**price_scale** | **int** | Price decimal places | [optional] 
**trading_status** | **str** | Current market trading status:&lt;br&gt; &lt;code&gt;POST_ONLY&lt;/code&gt; Trading is indefinitely suspended. This state is commonly used when new markets are being launched to give traders enough time to setup their orders before trading begins. When in this status, orders can only be posted as post-only.&lt;br&gt; &lt;code&gt;ACTIVE&lt;/code&gt; Trading is fully enabled.&lt;br&gt; &lt;code&gt;SUSPENDED&lt;/code&gt; Trading has been temporarily suspended due to very high volatility. When in this status, orders can only be posted as post-only.&lt;br&gt; &lt;code&gt;Unknown&lt;/code&gt; Trading status is unknown. This could indicate a temporary error on the market and should resolve shortly. | [optional] 
**volume_scale** | **int** | Volume decimal places | [optional] 

## Example

```python
from luno_openapi.models.market_info import MarketInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketInfo from a JSON string
market_info_instance = MarketInfo.from_json(json)
# print the JSON string representation of the object
print(MarketInfo.to_json())

# convert the object into a dict
market_info_dict = market_info_instance.to_dict()
# create an instance of MarketInfo from a dict
market_info_from_dict = MarketInfo.from_dict(market_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


