# CPUTotalsNodeRoleOSMetricNode

Representation of information from telemetry about the CPU capacity by node role and OS of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_totals** | [**List[CPUTotalNodeRoleOSMetricNode]**](CPUTotalNodeRoleOSMetricNode.md) |  | [optional] 

## Example

```python
from ocm_client.models.cpu_totals_node_role_os_metric_node import CPUTotalsNodeRoleOSMetricNode

# TODO update the JSON string below
json = "{}"
# create an instance of CPUTotalsNodeRoleOSMetricNode from a JSON string
cpu_totals_node_role_os_metric_node_instance = CPUTotalsNodeRoleOSMetricNode.from_json(json)
# print the JSON string representation of the object
print(CPUTotalsNodeRoleOSMetricNode.to_json())

# convert the object into a dict
cpu_totals_node_role_os_metric_node_dict = cpu_totals_node_role_os_metric_node_instance.to_dict()
# create an instance of CPUTotalsNodeRoleOSMetricNode from a dict
cpu_totals_node_role_os_metric_node_from_dict = CPUTotalsNodeRoleOSMetricNode.from_dict(cpu_totals_node_role_os_metric_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


