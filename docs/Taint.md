# Taint

Representation of a Taint set on a MachinePool in a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | The effect on the node for the pods matching the taint, i.e: NoSchedule, NoExecute, PreferNoSchedule. | [optional] 
**key** | **str** | The key for the taint | [optional] 
**value** | **str** | The value for the taint. | [optional] 

## Example

```python
from ocm_client.models.taint import Taint

# TODO update the JSON string below
json = "{}"
# create an instance of Taint from a JSON string
taint_instance = Taint.from_json(json)
# print the JSON string representation of the object
print(Taint.to_json())

# convert the object into a dict
taint_dict = taint_instance.to_dict()
# create an instance of Taint from a dict
taint_from_dict = Taint.from_dict(taint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


