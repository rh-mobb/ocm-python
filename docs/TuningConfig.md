# TuningConfig

Representation of a tuning config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;TuningConfig&#39; if this is a complete object or &#39;TuningConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**name** | **str** | Name of the tuning config. | [optional] 
**spec** | **object** | Spec of the tuning config. | [optional] 

## Example

```python
from ocm_client.models.tuning_config import TuningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TuningConfig from a JSON string
tuning_config_instance = TuningConfig.from_json(json)
# print the JSON string representation of the object
print(TuningConfig.to_json())

# convert the object into a dict
tuning_config_dict = tuning_config_instance.to_dict()
# create an instance of TuningConfig from a dict
tuning_config_from_dict = TuningConfig.from_dict(tuning_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


