# MachinePoolSecurityGroupFilter

Security Group Filter object, containing name of the filter tag and value of the filter tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.machine_pool_security_group_filter import MachinePoolSecurityGroupFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MachinePoolSecurityGroupFilter from a JSON string
machine_pool_security_group_filter_instance = MachinePoolSecurityGroupFilter.from_json(json)
# print the JSON string representation of the object
print(MachinePoolSecurityGroupFilter.to_json())

# convert the object into a dict
machine_pool_security_group_filter_dict = machine_pool_security_group_filter_instance.to_dict()
# create an instance of MachinePoolSecurityGroupFilter from a dict
machine_pool_security_group_filter_from_dict = MachinePoolSecurityGroupFilter.from_dict(machine_pool_security_group_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


