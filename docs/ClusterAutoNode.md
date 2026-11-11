# ClusterAutoNode

The AutoNode configuration for the Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode indicates the current state of AutoNode on this cluster. Valid values: \&quot;enabled\&quot;, \&quot;disabled\&quot;. | [optional] 
**status** | [**ClusterAutoNodeStatus**](ClusterAutoNodeStatus.md) |  | [optional] 

## Example

```python
from ocm_client.models.cluster_auto_node import ClusterAutoNode

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoNode from a JSON string
cluster_auto_node_instance = ClusterAutoNode.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoNode.to_json())

# convert the object into a dict
cluster_auto_node_dict = cluster_auto_node_instance.to_dict()
# create an instance of ClusterAutoNode from a dict
cluster_auto_node_from_dict = ClusterAutoNode.from_dict(cluster_auto_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


