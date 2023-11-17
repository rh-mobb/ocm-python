# CloudProvider

Cloud provider.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;CloudProvider&#39; if this is a complete object or &#39;CloudProviderLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**display_name** | **str** | Name of the cloud provider for display purposes. It can contain any characters, including spaces. | [optional] 
**name** | **str** | Human friendly identifier of the cloud provider, for example &#x60;aws&#x60;. | [optional] 
**regions** | [**list[CloudRegion]**](CloudRegion.md) | (optional) Provider&#39;s regions - only included when listing providers with &#x60;fetchRegions&#x3D;true&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


