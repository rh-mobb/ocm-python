# PendingDeleteCluster

Represents a pending delete entry for a specific cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;PendingDeleteCluster&#39; if this is a complete object or &#39;PendingDeleteClusterLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**best_effort** | **bool** | Flag indicating if the cluster deletion should be best-effort mode or not. | [optional] 
**cluster** | [**Cluster**](Cluster.md) |  | [optional] 
**creation_timestamp** | **datetime** | Date and time when the cluster was initially created, using the format defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


