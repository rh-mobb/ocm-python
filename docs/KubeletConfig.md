# KubeletConfig

OCM representation of KubeletConfig, exposing the fields of Kubernetes KubeletConfig that can be managed by users
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;KubeletConfig&#39; if this is a complete object or &#39;KubeletConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**pod_pids_limit** | **int** | Allows user to specify the podPidsLimit to be applied via KubeletConfig. Useful if workloads have greater PIDs limit requirements than the OCP default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


