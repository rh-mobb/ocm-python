# MachineTypeFeatures

Defines the features enabled or disabled on a particular machine type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**win_li** | **bool** |  | [optional] 

## Example

```python
from ocm_client.models.machine_type_features import MachineTypeFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTypeFeatures from a JSON string
machine_type_features_instance = MachineTypeFeatures.from_json(json)
# print the JSON string representation of the object
print(MachineTypeFeatures.to_json())

# convert the object into a dict
machine_type_features_dict = machine_type_features_instance.to_dict()
# create an instance of MachineTypeFeatures from a dict
machine_type_features_from_dict = MachineTypeFeatures.from_dict(machine_type_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


