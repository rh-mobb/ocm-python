# AMIOverride

AMIOverride specifies what Amazon Machine Image should be used for a particular product and region.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AMIOverride&#39; if this is a complete object or &#39;AMIOverrideLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**ami** | **str** | AMI is the id of the Amazon Machine Image. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**region** | [**CloudRegion**](CloudRegion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


