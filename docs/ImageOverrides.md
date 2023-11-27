# ImageOverrides

ImageOverrides holds the lists of available images per cloud provider.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ImageOverrides&#39; if this is a complete object or &#39;ImageOverridesLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**aws** | [**list[AMIOverride]**](AMIOverride.md) |  | [optional] 
**gcp** | [**list[GCPImageOverride]**](GCPImageOverride.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


