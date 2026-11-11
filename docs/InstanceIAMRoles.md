# InstanceIAMRoles

Contains the necessary attributes to support role-based authentication on AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_role_arn** | **str** | The IAM role ARN that will be attached to master instances | [optional] 
**worker_role_arn** | **str** | The IAM role ARN that will be attached to worker instances | [optional] 

## Example

```python
from ocm_client.models.instance_iam_roles import InstanceIAMRoles

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceIAMRoles from a JSON string
instance_iam_roles_instance = InstanceIAMRoles.from_json(json)
# print the JSON string representation of the object
print(InstanceIAMRoles.to_json())

# convert the object into a dict
instance_iam_roles_dict = instance_iam_roles_instance.to_dict()
# create an instance of InstanceIAMRoles from a dict
instance_iam_roles_from_dict = InstanceIAMRoles.from_dict(instance_iam_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


