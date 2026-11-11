# StsSupportJumpRole

Isolated STS support role created per organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_arn** | **str** | ARN of the support role created in the SRE jump account. | [optional] 

## Example

```python
from ocm_client.models.sts_support_jump_role import StsSupportJumpRole

# TODO update the JSON string below
json = "{}"
# create an instance of StsSupportJumpRole from a JSON string
sts_support_jump_role_instance = StsSupportJumpRole.from_json(json)
# print the JSON string representation of the object
print(StsSupportJumpRole.to_json())

# convert the object into a dict
sts_support_jump_role_dict = sts_support_jump_role_instance.to_dict()
# create an instance of StsSupportJumpRole from a dict
sts_support_jump_role_from_dict = StsSupportJumpRole.from_dict(sts_support_jump_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


