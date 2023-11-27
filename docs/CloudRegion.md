# CloudRegion

Description of a region of a cloud provider.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;CloudRegion&#39; if this is a complete object or &#39;CloudRegionLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**ccs_only** | **bool** | &#39;true&#39; if the region is supported only for CCS clusters, &#39;false&#39; otherwise. | [optional] 
**kms_location_id** | **str** | (GCP only) Comma-separated list of KMS location IDs that can be used with this region. E.g. \&quot;global,nam4,us\&quot;. Order is not guaranteed. | [optional] 
**kms_location_name** | **str** | (GCP only) Comma-separated list of display names corresponding to KMSLocationID. E.g. \&quot;Global,nam4 (Iowa, South Carolina, and Oklahoma),US\&quot;. Order is not guaranteed but will match KMSLocationID. Unfortunately, this API doesn&#39;t allow robust splitting - Contact ocm-feedback@redhat.com if you want to rely on this. | [optional] 
**cloud_provider** | [**CloudProvider**](CloudProvider.md) |  | [optional] 
**display_name** | **str** | Name of the region for display purposes, for example &#x60;N. Virginia&#x60;. | [optional] 
**enabled** | **bool** | Whether the region is enabled for deploying a managed cluster. | [optional] 
**govcloud** | **bool** | Whether the region is an AWS GovCloud region. | [optional] 
**name** | **str** | Human friendly identifier of the region, for example &#x60;us-east-1&#x60;.  NOTE: Currently for all cloud providers and all regions &#x60;id&#x60; and &#x60;name&#x60; have exactly the same values. | [optional] 
**supports_hypershift** | **bool** | &#39;true&#39; if the region is supported for Hypershift deployments, &#39;false&#39; otherwise. | [optional] 
**supports_multi_az** | **bool** | Whether the region supports multiple availability zones. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


