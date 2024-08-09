# GetTickerResponse

GetTickerResponse response for /api/ticker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask** | **str** | The lowest ask price | [optional] 
**bid** | **str** | The highest bid price | [optional] 
**last_trade** | **str** | Last trade price | [optional] 
**pair** | **str** |  | [optional] 
**rolling_24_hour_volume** | **str** | 24h rolling trade volume | [optional] 
**status** | **str** | Market current status  &lt;code&gt;ACTIVE&lt;/code&gt; when the market is trading normally  &lt;code&gt;POSTONLY&lt;/code&gt; when the market has been suspended and only post-only orders will be accepted  &lt;code&gt;DISABLED&lt;/code&gt; when the market is shutdown and no orders can be accepted  &lt;code&gt;UNKNOWN&lt;/code&gt; the market status could not be determined. This is a temporary state. | [optional] 
**timestamp** | **int** | Unix timestamp in milliseconds of the tick | [optional] 

## Example

```python
from luno_openapi.models.get_ticker_response import GetTickerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTickerResponse from a JSON string
get_ticker_response_instance = GetTickerResponse.from_json(json)
# print the JSON string representation of the object
print(GetTickerResponse.to_json())

# convert the object into a dict
get_ticker_response_dict = get_ticker_response_instance.to_dict()
# create an instance of GetTickerResponse from a dict
get_ticker_response_from_dict = GetTickerResponse.from_dict(get_ticker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


