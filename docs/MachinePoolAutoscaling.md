# MachinePoolAutoscaling

Representation of a autoscaling in a machine pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;MachinePoolAutoscaling&#39; if this is a complete object or &#39;MachinePoolAutoscalingLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**max_replicas** | **int** | The maximum number of replicas for the machine pool. | [optional] 
**min_replicas** | **int** | The minimum number of replicas for the machine pool. | [optional] 

## Example

```python
from ocm_client.models.machine_pool_autoscaling import MachinePoolAutoscaling

# TODO update the JSON string below
json = "{}"
# create an instance of MachinePoolAutoscaling from a JSON string
machine_pool_autoscaling_instance = MachinePoolAutoscaling.from_json(json)
# print the JSON string representation of the object
print(MachinePoolAutoscaling.to_json())

# convert the object into a dict
machine_pool_autoscaling_dict = machine_pool_autoscaling_instance.to_dict()
# create an instance of MachinePoolAutoscaling from a dict
machine_pool_autoscaling_from_dict = MachinePoolAutoscaling.from_dict(machine_pool_autoscaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


