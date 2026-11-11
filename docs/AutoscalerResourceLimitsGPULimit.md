# AutoscalerResourceLimitsGPULimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**ResourceRange**](ResourceRange.md) |  | [optional] 
**type** | **str** | The type of GPU to associate with the minimum and maximum limits. This value is used by the Cluster Autoscaler to identify Nodes that will have GPU capacity by searching for it as a label value on the Node objects. For example, Nodes that carry the label key &#x60;cluster-api/accelerator&#x60; with the label value being the same as the Type field will be counted towards the resource limits by the Cluster Autoscaler. | [optional] 

## Example

```python
from ocm_client.models.autoscaler_resource_limits_gpu_limit import AutoscalerResourceLimitsGPULimit

# TODO update the JSON string below
json = "{}"
# create an instance of AutoscalerResourceLimitsGPULimit from a JSON string
autoscaler_resource_limits_gpu_limit_instance = AutoscalerResourceLimitsGPULimit.from_json(json)
# print the JSON string representation of the object
print(AutoscalerResourceLimitsGPULimit.to_json())

# convert the object into a dict
autoscaler_resource_limits_gpu_limit_dict = autoscaler_resource_limits_gpu_limit_instance.to_dict()
# create an instance of AutoscalerResourceLimitsGPULimit from a dict
autoscaler_resource_limits_gpu_limit_from_dict = AutoscalerResourceLimitsGPULimit.from_dict(autoscaler_resource_limits_gpu_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


