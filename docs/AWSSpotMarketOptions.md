# AWSSpotMarketOptions

Spot market options for AWS machine pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AWSSpotMarketOptions&#39; if this is a complete object or &#39;AWSSpotMarketOptionsLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**max_price** | **float** | The max price for spot instance. Optional. If not set, use the on-demand price. | [optional] 

## Example

```python
from ocm_client.models.aws_spot_market_options import AWSSpotMarketOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AWSSpotMarketOptions from a JSON string
aws_spot_market_options_instance = AWSSpotMarketOptions.from_json(json)
# print the JSON string representation of the object
print(AWSSpotMarketOptions.to_json())

# convert the object into a dict
aws_spot_market_options_dict = aws_spot_market_options_instance.to_dict()
# create an instance of AWSSpotMarketOptions from a dict
aws_spot_market_options_from_dict = AWSSpotMarketOptions.from_dict(aws_spot_market_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


