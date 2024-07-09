# Ticker

Ticker summarised instant market data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask** | **str** | The lowest ask price | [optional] 
**bid** | **str** | The highest bid price | [optional] 
**last_trade** | **str** | Last trade price | [optional] 
**pair** | **str** |  | [optional] 
**rolling_24_hour_volume** | **str** | 24h rolling trade volume | [optional] 
**status** | **str** | Market current status  &lt;code&gt;ACTIVE&lt;/code&gt; when the market is trading normally  &lt;code&gt;POSTONLY&lt;/code&gt; when the market has been suspended and only post-only orders will be accepted  &lt;code&gt;DISABLED&lt;/code&gt; when the market is shutdown and no orders can be accepted  &lt;code&gt;UNKNOWN&lt;/code&gt; the market status could not be determined. This is a temporary state. | [optional] 
**timestamp** | **str** | Unix timestamp in milliseconds of the tick | [optional] 

## Example

```python
from luno_openapi.models.ticker import Ticker

# TODO update the JSON string below
json = "{}"
# create an instance of Ticker from a JSON string
ticker_instance = Ticker.from_json(json)
# print the JSON string representation of the object
print(Ticker.to_json())

# convert the object into a dict
ticker_dict = ticker_instance.to_dict()
# create an instance of Ticker from a dict
ticker_from_dict = Ticker.from_dict(ticker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


