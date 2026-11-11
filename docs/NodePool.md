# NodePool

Representation of a node pool in a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;NodePool&#39; if this is a complete object or &#39;NodePoolLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**aws_node_pool** | [**AWSNodePool**](AWSNodePool.md) |  | [optional] 
**auto_repair** | **bool** | Specifies whether health checks should be enabled for machines in the NodePool. | [optional] 
**autoscaling** | [**NodePoolAutoscaling**](NodePoolAutoscaling.md) |  | [optional] 
**availability_zone** | **str** | The availability zone upon which the node is created. | [optional] 
**azure_node_pool** | [**AzureNodePool**](AzureNodePool.md) |  | [optional] 
**image_type** | [**ImageType**](ImageType.md) |  | [optional] 
**kubelet_configs** | **List[str]** | The names of the KubeletConfigs for this node pool. | [optional] 
**labels** | **Dict[str, str]** | The labels set on the Nodes created. | [optional] 
**management_upgrade** | [**NodePoolManagementUpgrade**](NodePoolManagementUpgrade.md) |  | [optional] 
**node_drain_grace_period** | [**Value**](Value.md) |  | [optional] 
**replicas** | **int** | The number of Machines (and Nodes) to create. Replicas and autoscaling cannot be used together. | [optional] 
**status** | [**NodePoolStatus**](NodePoolStatus.md) |  | [optional] 
**subnet** | **str** | The subnet upon which the nodes are created. | [optional] 
**taints** | [**List[Taint]**](Taint.md) | The taints set on the Nodes created. | [optional] 
**tuning_configs** | **List[str]** | The names of the tuning configs for this node pool. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from ocm_client.models.node_pool import NodePool

# TODO update the JSON string below
json = "{}"
# create an instance of NodePool from a JSON string
node_pool_instance = NodePool.from_json(json)
# print the JSON string representation of the object
print(NodePool.to_json())

# convert the object into a dict
node_pool_dict = node_pool_instance.to_dict()
# create an instance of NodePool from a dict
node_pool_from_dict = NodePool.from_dict(node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


