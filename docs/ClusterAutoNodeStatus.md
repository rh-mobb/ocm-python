# ClusterAutoNodeStatus

Additional status information on the AutoNode configuration on this Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Messages relating to the status of the AutoNode installation on this Cluster | [optional] 
**node_count** | **int** | The number of Nodes AutoNode has provisioned in the cluster | [optional] 

## Example

```python
from ocm_client.models.cluster_auto_node_status import ClusterAutoNodeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoNodeStatus from a JSON string
cluster_auto_node_status_instance = ClusterAutoNodeStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoNodeStatus.to_json())

# convert the object into a dict
cluster_auto_node_status_dict = cluster_auto_node_status_instance.to_dict()
# create an instance of ClusterAutoNodeStatus from a dict
cluster_auto_node_status_from_dict = ClusterAutoNodeStatus.from_dict(cluster_auto_node_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


