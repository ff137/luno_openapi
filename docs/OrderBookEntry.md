# OrderBookEntry

OrderBookEntry is the representation of one or more order resting in the order book.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** | Limit price at which orders are trading at | [optional] 
**volume** | **str** | The volume available at the limit price | [optional] 

## Example

```python
from luno_openapi.models.order_book_entry import OrderBookEntry

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBookEntry from a JSON string
order_book_entry_instance = OrderBookEntry.from_json(json)
# print the JSON string representation of the object
print(OrderBookEntry.to_json())

# convert the object into a dict
order_book_entry_dict = order_book_entry_instance.to_dict()
# create an instance of OrderBookEntry from a dict
order_book_entry_from_dict = OrderBookEntry.from_dict(order_book_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


