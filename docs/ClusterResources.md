# ClusterResources

Cluster Resource which belongs to a cluster, example Cluster Deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ClusterResources&#39; if this is a complete object or &#39;ClusterResourcesLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster_id** | **str** | Cluster ID for the fetched resources | [optional] 
**creation_timestamp** | **datetime** | Date and time when the resources were fetched. | [optional] 
**resources** | **Dict[str, str]** | Returned map of cluster resources fetched. | [optional] 

## Example

```python
from ocm_client.models.cluster_resources import ClusterResources

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResources from a JSON string
cluster_resources_instance = ClusterResources.from_json(json)
# print the JSON string representation of the object
print(ClusterResources.to_json())

# convert the object into a dict
cluster_resources_dict = cluster_resources_instance.to_dict()
# create an instance of ClusterResources from a dict
cluster_resources_from_dict = ClusterResources.from_dict(cluster_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


