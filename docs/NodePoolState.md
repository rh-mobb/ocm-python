# NodePoolState

Representation of the status of a node pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;NodePoolState&#39; if this is a complete object or &#39;NodePoolStateLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**last_updated_timestamp** | **datetime** | The current number of replicas for the node pool. | [optional] 
**value** | **str** | The current state of the node pool | [optional] 

## Example

```python
from ocm_client.models.node_pool_state import NodePoolState

# TODO update the JSON string below
json = "{}"
# create an instance of NodePoolState from a JSON string
node_pool_state_instance = NodePoolState.from_json(json)
# print the JSON string representation of the object
print(NodePoolState.to_json())

# convert the object into a dict
node_pool_state_dict = node_pool_state_instance.to_dict()
# create an instance of NodePoolState from a dict
node_pool_state_from_dict = NodePoolState.from_dict(node_pool_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


