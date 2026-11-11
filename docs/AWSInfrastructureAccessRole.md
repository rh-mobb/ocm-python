# AWSInfrastructureAccessRole

A set of acces permissions for AWS resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AWSInfrastructureAccessRole&#39; if this is a complete object or &#39;AWSInfrastructureAccessRoleLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**description** | **str** | Description of the role. | [optional] 
**display_name** | **str** | Human friendly identifier of the role, for example &#x60;Read only&#x60;. | [optional] 
**state** | [**AWSInfrastructureAccessRoleState**](AWSInfrastructureAccessRoleState.md) |  | [optional] 

## Example

```python
from ocm_client.models.aws_infrastructure_access_role import AWSInfrastructureAccessRole

# TODO update the JSON string below
json = "{}"
# create an instance of AWSInfrastructureAccessRole from a JSON string
aws_infrastructure_access_role_instance = AWSInfrastructureAccessRole.from_json(json)
# print the JSON string representation of the object
print(AWSInfrastructureAccessRole.to_json())

# convert the object into a dict
aws_infrastructure_access_role_dict = aws_infrastructure_access_role_instance.to_dict()
# create an instance of AWSInfrastructureAccessRole from a dict
aws_infrastructure_access_role_from_dict = AWSInfrastructureAccessRole.from_dict(aws_infrastructure_access_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


