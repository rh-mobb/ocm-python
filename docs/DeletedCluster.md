# DeletedCluster

Representation of a deleted cluster with its deleted_timestamp and the entire cluster details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;DeletedCluster&#39; if this is a complete object or &#39;DeletedClusterLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster** | [**Cluster**](Cluster.md) |  | [optional] 
**deleted_timestamp** | **datetime** | Date and time the cluster was effectively deleted | [optional] 

## Example

```python
from ocm_client.models.deleted_cluster import DeletedCluster

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedCluster from a JSON string
deleted_cluster_instance = DeletedCluster.from_json(json)
# print the JSON string representation of the object
print(DeletedCluster.to_json())

# convert the object into a dict
deleted_cluster_dict = deleted_cluster_instance.to_dict()
# create an instance of DeletedCluster from a dict
deleted_cluster_from_dict = DeletedCluster.from_dict(deleted_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


