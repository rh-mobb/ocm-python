# AWSNodePool

Representation of aws node pool specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AWSNodePool&#39; if this is a complete object or &#39;AWSNodePoolLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**additional_security_group_ids** | **List[str]** | Additional AWS Security Groups to be added node pool. | [optional] 
**availability_zone_types** | **Dict[str, str]** | Associates nodepool availability zones with zone types (e.g. wavelength, local). | [optional] 
**capacity_reservation** | [**AWSCapacityReservation**](AWSCapacityReservation.md) |  | [optional] 
**ec2_metadata_http_tokens** | [**Ec2MetadataHttpTokens**](Ec2MetadataHttpTokens.md) |  | [optional] 
**instance_profile** | **str** | InstanceProfile is the AWS EC2 instance profile, which is a container for an IAM role that the EC2 instance uses. | [optional] 
**instance_type** | **str** | InstanceType is an ec2 instance type for node instances (e.g. m5.large). | [optional] 
**root_volume** | [**AWSVolume**](AWSVolume.md) |  | [optional] 
**spot_market_options** | [**AwsNodePoolSpotMarketOptions**](AwsNodePoolSpotMarketOptions.md) |  | [optional] 
**subnet_outposts** | **Dict[str, str]** | Associates nodepool subnets with AWS Outposts. | [optional] 
**tags** | **Dict[str, str]** | Optional keys and values that the installer will add as tags to all AWS resources it creates.  AWS tags must conform to the following standards: - Each resource may have a maximum of 25 tags - Tags beginning with \&quot;aws:\&quot; are reserved for system use and may not be set - Tag keys may be between 1 and 128 characters in length - Tag values may be between 0 and 256 characters in length - Tags may only contain letters, numbers, spaces, and the following characters: [_ . : / &#x3D; + - @] | [optional] 

## Example

```python
from ocm_client.models.aws_node_pool import AWSNodePool

# TODO update the JSON string below
json = "{}"
# create an instance of AWSNodePool from a JSON string
aws_node_pool_instance = AWSNodePool.from_json(json)
# print the JSON string representation of the object
print(AWSNodePool.to_json())

# convert the object into a dict
aws_node_pool_dict = aws_node_pool_instance.to_dict()
# create an instance of AWSNodePool from a dict
aws_node_pool_from_dict = AWSNodePool.from_dict(aws_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


