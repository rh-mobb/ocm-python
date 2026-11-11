# NodePoolManagementUpgrade

Representation of node pool management.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;NodePoolManagementUpgrade&#39; if this is a complete object or &#39;NodePoolManagementUpgradeLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**max_surge** | **str** | Maximum number of nodes in the NodePool of a ROSA HCP cluster that can be scheduled above the desired number of nodes during the upgrade. | [optional] 
**max_unavailable** | **str** | Maximum number of nodes in the NodePool of a ROSA HCP cluster that can be unavailable during the upgrade. | [optional] 
**type** | **str** | Type of strategy for handling upgrades. | [optional] 

## Example

```python
from ocm_client.models.node_pool_management_upgrade import NodePoolManagementUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of NodePoolManagementUpgrade from a JSON string
node_pool_management_upgrade_instance = NodePoolManagementUpgrade.from_json(json)
# print the JSON string representation of the object
print(NodePoolManagementUpgrade.to_json())

# convert the object into a dict
node_pool_management_upgrade_dict = node_pool_management_upgrade_instance.to_dict()
# create an instance of NodePoolManagementUpgrade from a dict
node_pool_management_upgrade_from_dict = NodePoolManagementUpgrade.from_dict(node_pool_management_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


