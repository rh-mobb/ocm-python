# DNSDomain

Contains the properties of a DNS domain.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;DNSDomain&#39; if this is a complete object or &#39;DNSDomainLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster** | [**ClusterLink**](ClusterLink.md) |  | [optional] 
**organization** | [**OrganizationLink**](OrganizationLink.md) |  | [optional] 
**reserved_at_timestamp** | **datetime** | Date and time when the DNS domain was reserved. | [optional] 
**user_defined** | **bool** | Indicates if this dns domain is user defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


