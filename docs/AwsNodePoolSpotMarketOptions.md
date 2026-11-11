# AwsNodePoolSpotMarketOptions

Spot market options for AWS node pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AwsNodePoolSpotMarketOptions&#39; if this is a complete object or &#39;AwsNodePoolSpotMarketOptionsLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**max_price** | **str** | The max price for spot instance. Optional. If not set, use the on-demand price. | [optional] 

## Example

```python
from ocm_client.models.aws_node_pool_spot_market_options import AwsNodePoolSpotMarketOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AwsNodePoolSpotMarketOptions from a JSON string
aws_node_pool_spot_market_options_instance = AwsNodePoolSpotMarketOptions.from_json(json)
# print the JSON string representation of the object
print(AwsNodePoolSpotMarketOptions.to_json())

# convert the object into a dict
aws_node_pool_spot_market_options_dict = aws_node_pool_spot_market_options_instance.to_dict()
# create an instance of AwsNodePoolSpotMarketOptions from a dict
aws_node_pool_spot_market_options_from_dict = AwsNodePoolSpotMarketOptions.from_dict(aws_node_pool_spot_market_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


