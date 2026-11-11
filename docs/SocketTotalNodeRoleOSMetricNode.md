# SocketTotalNodeRoleOSMetricNode

Representation of information from telemetry about a the socket capacity by node role and OS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_roles** | **List[str]** | Representation of the node role for a cluster. | [optional] 
**operating_system** | **str** | The operating system. | [optional] 
**socket_total** | **float** | The total socket capacity of nodes with this set of roles and operating system. | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from ocm_client.models.socket_total_node_role_os_metric_node import SocketTotalNodeRoleOSMetricNode

# TODO update the JSON string below
json = "{}"
# create an instance of SocketTotalNodeRoleOSMetricNode from a JSON string
socket_total_node_role_os_metric_node_instance = SocketTotalNodeRoleOSMetricNode.from_json(json)
# print the JSON string representation of the object
print(SocketTotalNodeRoleOSMetricNode.to_json())

# convert the object into a dict
socket_total_node_role_os_metric_node_dict = socket_total_node_role_os_metric_node_instance.to_dict()
# create an instance of SocketTotalNodeRoleOSMetricNode from a dict
socket_total_node_role_os_metric_node_from_dict = SocketTotalNodeRoleOSMetricNode.from_dict(socket_total_node_role_os_metric_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


