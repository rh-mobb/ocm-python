# GCPImageOverride

GcpImageOverride specifies what a GCP VM Image should be used for a particular product and billing model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;GCPImageOverride&#39; if this is a complete object or &#39;GCPImageOverrideLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**billing_model** | [**BillingModelItem**](BillingModelItem.md) |  | [optional] 
**image_id** | **str** | ImageID is the id of the Google Cloud Platform image. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**project_id** | **str** | ProjectID is the id of the Google Cloud Platform project that hosts the image. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


