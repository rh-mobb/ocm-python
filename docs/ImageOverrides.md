# ImageOverrides

ImageOverrides holds the lists of available images per cloud provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ImageOverrides&#39; if this is a complete object or &#39;ImageOverridesLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**aws** | [**List[AMIOverride]**](AMIOverride.md) |  | [optional] 
**gcp** | [**List[GCPImageOverride]**](GCPImageOverride.md) |  | [optional] 

## Example

```python
from ocm_client.models.image_overrides import ImageOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOverrides from a JSON string
image_overrides_instance = ImageOverrides.from_json(json)
# print the JSON string representation of the object
print(ImageOverrides.to_json())

# convert the object into a dict
image_overrides_dict = image_overrides_instance.to_dict()
# create an instance of ImageOverrides from a dict
image_overrides_from_dict = ImageOverrides.from_dict(image_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


