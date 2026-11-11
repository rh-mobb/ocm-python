# AutoscalerResourceLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpus** | [**List[AutoscalerResourceLimitsGPULimit]**](AutoscalerResourceLimitsGPULimit.md) | Minimum and maximum number of different GPUs in cluster, in the format &lt;gpu_type&gt;:&lt;min&gt;:&lt;max&gt;. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times. | [optional] 
**cores** | [**ResourceRange**](ResourceRange.md) |  | [optional] 
**max_nodes_total** | **int** | Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number. | [optional] 
**memory** | [**ResourceRange**](ResourceRange.md) |  | [optional] 

## Example

```python
from ocm_client.models.autoscaler_resource_limits import AutoscalerResourceLimits

# TODO update the JSON string below
json = "{}"
# create an instance of AutoscalerResourceLimits from a JSON string
autoscaler_resource_limits_instance = AutoscalerResourceLimits.from_json(json)
# print the JSON string representation of the object
print(AutoscalerResourceLimits.to_json())

# convert the object into a dict
autoscaler_resource_limits_dict = autoscaler_resource_limits_instance.to_dict()
# create an instance of AutoscalerResourceLimits from a dict
autoscaler_resource_limits_from_dict = AutoscalerResourceLimits.from_dict(autoscaler_resource_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


