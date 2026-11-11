# RolePolicyBindingStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.role_policy_binding_status import RolePolicyBindingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RolePolicyBindingStatus from a JSON string
role_policy_binding_status_instance = RolePolicyBindingStatus.from_json(json)
# print the JSON string representation of the object
print(RolePolicyBindingStatus.to_json())

# convert the object into a dict
role_policy_binding_status_dict = role_policy_binding_status_instance.to_dict()
# create an instance of RolePolicyBindingStatus from a dict
role_policy_binding_status_from_dict = RolePolicyBindingStatus.from_dict(role_policy_binding_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


