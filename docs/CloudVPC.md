# CloudVPC

Description of a cloud provider virtual private cloud.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_security_groups** | [**List[SecurityGroup]**](SecurityGroup.md) | List of AWS security groups with details. | [optional] 
**aws_subnets** | [**List[Subnetwork]**](Subnetwork.md) | List of AWS subnetworks with details. | [optional] 
**cidr_block** | **str** | CIDR block of the virtual private cloud. | [optional] 
**id** | **str** | ID of virtual private cloud. | [optional] 
**name** | **str** | Name of virtual private cloud according to its &#x60;Name&#x60; tag on AWS. | [optional] 
**red_hat_managed** | **bool** | If the resource is RH managed. | [optional] 
**subnets** | **List[str]** | List of subnets used by the virtual private cloud. | [optional] 

## Example

```python
from ocm_client.models.cloud_vpc import CloudVPC

# TODO update the JSON string below
json = "{}"
# create an instance of CloudVPC from a JSON string
cloud_vpc_instance = CloudVPC.from_json(json)
# print the JSON string representation of the object
print(CloudVPC.to_json())

# convert the object into a dict
cloud_vpc_dict = cloud_vpc_instance.to_dict()
# create an instance of CloudVPC from a dict
cloud_vpc_from_dict = CloudVPC.from_dict(cloud_vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


