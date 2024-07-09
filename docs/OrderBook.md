# OrderBook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asks** | [**List[OrderBookEntry]**](OrderBookEntry.md) | List of asks sorted from lowest to highest price | [optional] 
**bids** | [**List[OrderBookEntry]**](OrderBookEntry.md) | List of bids sorted from highest to lowest price | [optional] 
**timestamp** | **int** | Unix timestamp in milliseconds | [optional] 

## Example

```python
from luno_openapi.models.order_book import OrderBook

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBook from a JSON string
order_book_instance = OrderBook.from_json(json)
# print the JSON string representation of the object
print(OrderBook.to_json())

# convert the object into a dict
order_book_dict = order_book_instance.to_dict()
# create an instance of OrderBook from a dict
order_book_from_dict = OrderBook.from_dict(order_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


