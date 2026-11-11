# ImageMirror

ImageMirror represents a container image mirror configuration for a cluster. This enables Day 2 image mirroring configuration for ROSA HCP clusters using HyperShift's native imageContentSources mechanism.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ImageMirror&#39; if this is a complete object or &#39;ImageMirrorLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**creation_timestamp** | **datetime** | CreationTimestamp indicates when the image mirror was created. | [optional] 
**last_update_timestamp** | **datetime** | LastUpdateTimestamp indicates when the image mirror was last updated. | [optional] 
**mirrors** | **List[str]** | Mirrors is the list of mirror registries that will serve content for the source. Mirrors array cannot be empty (must contain at least one mirror registry). Each mirror registry URL must conform to OpenShift&#39;s ImageDigestMirrorSet format specifications. | [optional] 
**source** | **str** | Source is the source registry that will be mirrored. Source registry must be unique per cluster and is immutable after creation. Source is used to identify mirror entries in HostedCluster imageContentSources. | [optional] 
**type** | **str** | Type specifies the mirror type, currently only \&quot;digest\&quot; is supported. | [optional] 

## Example

```python
from ocm_client.models.image_mirror import ImageMirror

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMirror from a JSON string
image_mirror_instance = ImageMirror.from_json(json)
# print the JSON string representation of the object
print(ImageMirror.to_json())

# convert the object into a dict
image_mirror_dict = image_mirror_instance.to_dict()
# create an instance of ImageMirror from a dict
image_mirror_from_dict = ImageMirror.from_dict(image_mirror_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


