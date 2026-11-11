# AWSSTSRole

Representation of an sts role for a rosa cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hcp_managed_policies** | **bool** | Does this Role have HCP Managed Policies? | [optional] 
**is_admin** | **bool** | Does this role have Admin permission? | [optional] 
**managed_policies** | **bool** | Does this Role have Managed Policies? | [optional] 
**arn** | **str** | The AWS ARN for this Role | [optional] 
**type** | **str** | The type of this Role | [optional] 
**role_version** | **str** | The Openshift Version for this Role | [optional] 

## Example

```python
from ocm_client.models.awssts_role import AWSSTSRole

# TODO update the JSON string below
json = "{}"
# create an instance of AWSSTSRole from a JSON string
awssts_role_instance = AWSSTSRole.from_json(json)
# print the JSON string representation of the object
print(AWSSTSRole.to_json())

# convert the object into a dict
awssts_role_dict = awssts_role_instance.to_dict()
# create an instance of AWSSTSRole from a dict
awssts_role_from_dict = AWSSTSRole.from_dict(awssts_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


