# ListTickersResponse

ListTickersResponse response for /api/tickers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickers** | [**List[Ticker]**](Ticker.md) |  | [optional] 

## Example

```python
from luno_openapi.models.list_tickers_response import ListTickersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTickersResponse from a JSON string
list_tickers_response_instance = ListTickersResponse.from_json(json)
# print the JSON string representation of the object
print(ListTickersResponse.to_json())

# convert the object into a dict
list_tickers_response_dict = list_tickers_response_instance.to_dict()
# create an instance of ListTickersResponse from a dict
list_tickers_response_from_dict = ListTickersResponse.from_dict(list_tickers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


