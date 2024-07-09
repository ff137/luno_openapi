# GetOrderBookResponse

1/orderbook 1/orderbook_top

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asks** | [**List[OrderBookEntry]**](OrderBookEntry.md) | List of asks sorted from lowest to highest price | [optional] 
**bids** | [**List[OrderBookEntry]**](OrderBookEntry.md) | List of bids sorted from highest to lowest price | [optional] 
**timestamp** | **int** | Unix timestamp in milliseconds | [optional] 

## Example

```python
from luno_openapi.models.get_order_book_response import GetOrderBookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderBookResponse from a JSON string
get_order_book_response_instance = GetOrderBookResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrderBookResponse.to_json())

# convert the object into a dict
get_order_book_response_dict = get_order_book_response_instance.to_dict()
# create an instance of GetOrderBookResponse from a dict
get_order_book_response_from_dict = GetOrderBookResponse.from_dict(get_order_book_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


