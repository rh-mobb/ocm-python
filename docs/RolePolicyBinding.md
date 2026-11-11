# RolePolicyBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**last_update_timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**policies** | [**List[RolePolicy]**](RolePolicy.md) |  | [optional] 
**status** | [**RolePolicyBindingStatus**](RolePolicyBindingStatus.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.role_policy_binding import RolePolicyBinding

# TODO update the JSON string below
json = "{}"
# create an instance of RolePolicyBinding from a JSON string
role_policy_binding_instance = RolePolicyBinding.from_json(json)
# print the JSON string representation of the object
print(RolePolicyBinding.to_json())

# convert the object into a dict
role_policy_binding_dict = role_policy_binding_instance.to_dict()
# create an instance of RolePolicyBinding from a dict
role_policy_binding_from_dict = RolePolicyBinding.from_dict(role_policy_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


