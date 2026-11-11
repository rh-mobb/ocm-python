# AutoscalerScaleDownConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_after_add** | **str** | How long after scale up that scale down evaluation resumes. | [optional] 
**delay_after_delete** | **str** | How long after node deletion that scale down evaluation resumes, defaults to scan-interval. | [optional] 
**delay_after_failure** | **str** | How long after scale down failure that scale down evaluation resumes. | [optional] 
**enabled** | **bool** | Should cluster-autoscaler scale down the cluster. | [optional] 
**unneeded_time** | **str** | How long a node should be unneeded before it is eligible for scale down. | [optional] 
**utilization_threshold** | **str** | Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. | [optional] 

## Example

```python
from ocm_client.models.autoscaler_scale_down_config import AutoscalerScaleDownConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AutoscalerScaleDownConfig from a JSON string
autoscaler_scale_down_config_instance = AutoscalerScaleDownConfig.from_json(json)
# print the JSON string representation of the object
print(AutoscalerScaleDownConfig.to_json())

# convert the object into a dict
autoscaler_scale_down_config_dict = autoscaler_scale_down_config_instance.to_dict()
# create an instance of AutoscalerScaleDownConfig from a dict
autoscaler_scale_down_config_from_dict = AutoscalerScaleDownConfig.from_dict(autoscaler_scale_down_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


