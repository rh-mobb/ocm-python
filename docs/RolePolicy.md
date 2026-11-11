# RolePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.role_policy import RolePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of RolePolicy from a JSON string
role_policy_instance = RolePolicy.from_json(json)
# print the JSON string representation of the object
print(RolePolicy.to_json())

# convert the object into a dict
role_policy_dict = role_policy_instance.to_dict()
# create an instance of RolePolicy from a dict
role_policy_from_dict = RolePolicy.from_dict(role_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


