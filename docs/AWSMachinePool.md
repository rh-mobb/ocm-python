# AWSMachinePool

Representation of aws machine pool specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AWSMachinePool&#39; if this is a complete object or &#39;AWSMachinePoolLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**additional_security_group_ids** | **List[str]** | Additional AWS Security Groups to be added machine pool. Note that machine pools can only be worker node at the time. | [optional] 
**availability_zone_types** | **Dict[str, str]** | Associates nodepool availability zones with zone types (e.g. wavelength, local). | [optional] 
**spot_market_options** | [**AWSSpotMarketOptions**](AWSSpotMarketOptions.md) |  | [optional] 
**subnet_outposts** | **Dict[str, str]** | Associates nodepool subnets with AWS Outposts. | [optional] 
**tags** | **Dict[str, str]** | Optional keys and values that the machine pool provisioner will add as AWS tags to all AWS resources it creates.  AWS tags must conform to the following standards: - Each resource may have a maximum of 25 tags - Tags beginning with \&quot;aws:\&quot; are reserved for system use and may not be set - Tag keys may be between 1 and 128 characters in length - Tag values may be between 0 and 256 characters in length - Tags may only contain letters, numbers, spaces, and the following characters: [_ . : / &#x3D; + - @] | [optional] 

## Example

```python
from ocm_client.models.aws_machine_pool import AWSMachinePool

# TODO update the JSON string below
json = "{}"
# create an instance of AWSMachinePool from a JSON string
aws_machine_pool_instance = AWSMachinePool.from_json(json)
# print the JSON string representation of the object
print(AWSMachinePool.to_json())

# convert the object into a dict
aws_machine_pool_dict = aws_machine_pool_instance.to_dict()
# create an instance of AWSMachinePool from a dict
aws_machine_pool_from_dict = AWSMachinePool.from_dict(aws_machine_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


