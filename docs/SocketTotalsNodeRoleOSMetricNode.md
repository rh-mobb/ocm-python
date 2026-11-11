# SocketTotalsNodeRoleOSMetricNode

Representation of information from telemetry about the socket capacity by node role and OS of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**socket_totals** | [**List[SocketTotalNodeRoleOSMetricNode]**](SocketTotalNodeRoleOSMetricNode.md) |  | [optional] 

## Example

```python
from ocm_client.models.socket_totals_node_role_os_metric_node import SocketTotalsNodeRoleOSMetricNode

# TODO update the JSON string below
json = "{}"
# create an instance of SocketTotalsNodeRoleOSMetricNode from a JSON string
socket_totals_node_role_os_metric_node_instance = SocketTotalsNodeRoleOSMetricNode.from_json(json)
# print the JSON string representation of the object
print(SocketTotalsNodeRoleOSMetricNode.to_json())

# convert the object into a dict
socket_totals_node_role_os_metric_node_dict = socket_totals_node_role_os_metric_node_instance.to_dict()
# create an instance of SocketTotalsNodeRoleOSMetricNode from a dict
socket_totals_node_role_os_metric_node_from_dict = SocketTotalsNodeRoleOSMetricNode.from_dict(socket_totals_node_role_os_metric_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


