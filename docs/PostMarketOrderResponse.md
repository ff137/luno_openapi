# PostMarketOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Unique order identifier | [optional] 

## Example

```python
from luno_openapi.models.post_market_order_response import PostMarketOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostMarketOrderResponse from a JSON string
post_market_order_response_instance = PostMarketOrderResponse.from_json(json)
# print the JSON string representation of the object
print(PostMarketOrderResponse.to_json())

# convert the object into a dict
post_market_order_response_dict = post_market_order_response_instance.to_dict()
# create an instance of PostMarketOrderResponse from a dict
post_market_order_response_from_dict = PostMarketOrderResponse.from_dict(post_market_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


