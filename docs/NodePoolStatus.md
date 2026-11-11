# NodePoolStatus

Representation of the status of a node pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;NodePoolStatus&#39; if this is a complete object or &#39;NodePoolStatusLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**current_replicas** | **int** | The current number of replicas for the node pool. | [optional] 
**message** | **str** | Adds additional information about the NodePool status when the node pool doesn&#39;t reach the desired replicas. | [optional] 
**state** | [**NodePoolState**](NodePoolState.md) |  | [optional] 

## Example

```python
from ocm_client.models.node_pool_status import NodePoolStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NodePoolStatus from a JSON string
node_pool_status_instance = NodePoolStatus.from_json(json)
# print the JSON string representation of the object
print(NodePoolStatus.to_json())

# convert the object into a dict
node_pool_status_dict = node_pool_status_instance.to_dict()
# create an instance of NodePoolStatus from a dict
node_pool_status_from_dict = NodePoolStatus.from_dict(node_pool_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


