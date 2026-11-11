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

## Example

```python
from ocm_client.models.pending_delete_cluster import PendingDeleteCluster

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDeleteCluster from a JSON string
pending_delete_cluster_instance = PendingDeleteCluster.from_json(json)
# print the JSON string representation of the object
print(PendingDeleteCluster.to_json())

# convert the object into a dict
pending_delete_cluster_dict = pending_delete_cluster_instance.to_dict()
# create an instance of PendingDeleteCluster from a dict
pending_delete_cluster_from_dict = PendingDeleteCluster.from_dict(pending_delete_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


