# AWSSTSAccountRole

Representation of an sts account role for a rosa cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AWSSTSRole]**](AWSSTSRole.md) | The list of STS Roles for this Account Role | [optional] 
**prefix** | **str** | The Prefix for this Account Role | [optional] 

## Example

```python
from ocm_client.models.awssts_account_role import AWSSTSAccountRole

# TODO update the JSON string below
json = "{}"
# create an instance of AWSSTSAccountRole from a JSON string
awssts_account_role_instance = AWSSTSAccountRole.from_json(json)
# print the JSON string representation of the object
print(AWSSTSAccountRole.to_json())

# convert the object into a dict
awssts_account_role_dict = awssts_account_role_instance.to_dict()
# create an instance of AWSSTSAccountRole from a dict
awssts_account_role_from_dict = AWSSTSAccountRole.from_dict(awssts_account_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


