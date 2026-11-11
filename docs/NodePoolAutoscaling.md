# NodePoolAutoscaling

Representation of a autoscaling in a node pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;NodePoolAutoscaling&#39; if this is a complete object or &#39;NodePoolAutoscalingLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**max_replica** | **int** | The maximum number of replicas for the node pool. | [optional] 
**min_replica** | **int** | The minimum number of replicas for the node pool. | [optional] 

## Example

```python
from ocm_client.models.node_pool_autoscaling import NodePoolAutoscaling

# TODO update the JSON string below
json = "{}"
# create an instance of NodePoolAutoscaling from a JSON string
node_pool_autoscaling_instance = NodePoolAutoscaling.from_json(json)
# print the JSON string representation of the object
print(NodePoolAutoscaling.to_json())

# convert the object into a dict
node_pool_autoscaling_dict = node_pool_autoscaling_instance.to_dict()
# create an instance of NodePoolAutoscaling from a dict
node_pool_autoscaling_from_dict = NodePoolAutoscaling.from_dict(node_pool_autoscaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


