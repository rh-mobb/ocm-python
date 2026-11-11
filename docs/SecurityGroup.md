# SecurityGroup

AWS security group object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The security group ID. | [optional] 
**name** | **str** | Name of the security group according to its &#x60;Name&#x60; tag on AWS. | [optional] 
**red_hat_managed** | **bool** | If the resource is RH managed. | [optional] 

## Example

```python
from ocm_client.models.security_group import SecurityGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroup from a JSON string
security_group_instance = SecurityGroup.from_json(json)
# print the JSON string representation of the object
print(SecurityGroup.to_json())

# convert the object into a dict
security_group_dict = security_group_instance.to_dict()
# create an instance of SecurityGroup from a dict
security_group_from_dict = SecurityGroup.from_dict(security_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


