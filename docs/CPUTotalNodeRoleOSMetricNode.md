# CPUTotalNodeRoleOSMetricNode

Representation of information from telemetry about a the CPU capacity by node role and OS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_total** | **float** | The total CPU capacity of nodes with this set of roles and operating system. | [optional] 
**node_roles** | **List[str]** | Representation of the node role for a cluster. | [optional] 
**operating_system** | **str** | The operating system. | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from ocm_client.models.cpu_total_node_role_os_metric_node import CPUTotalNodeRoleOSMetricNode

# TODO update the JSON string below
json = "{}"
# create an instance of CPUTotalNodeRoleOSMetricNode from a JSON string
cpu_total_node_role_os_metric_node_instance = CPUTotalNodeRoleOSMetricNode.from_json(json)
# print the JSON string representation of the object
print(CPUTotalNodeRoleOSMetricNode.to_json())

# convert the object into a dict
cpu_total_node_role_os_metric_node_dict = cpu_total_node_role_os_metric_node_instance.to_dict()
# create an instance of CPUTotalNodeRoleOSMetricNode from a dict
cpu_total_node_role_os_metric_node_from_dict = CPUTotalNodeRoleOSMetricNode.from_dict(cpu_total_node_role_os_metric_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


