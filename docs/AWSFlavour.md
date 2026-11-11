# AWSFlavour

Specification for different classes of nodes inside a flavour.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_instance_type** | **str** | AWS default instance type for the worker volume.  User can be overridden specifying in the cluster itself a type for compute node. | [optional] 
**infra_instance_type** | **str** | AWS default instance type for the infra volume. | [optional] 
**infra_volume** | [**AWSVolume**](AWSVolume.md) |  | [optional] 
**master_instance_type** | **str** | AWS default instance type for the master volume. | [optional] 
**master_volume** | [**AWSVolume**](AWSVolume.md) |  | [optional] 
**worker_volume** | [**AWSVolume**](AWSVolume.md) |  | [optional] 

## Example

```python
from ocm_client.models.aws_flavour import AWSFlavour

# TODO update the JSON string below
json = "{}"
# create an instance of AWSFlavour from a JSON string
aws_flavour_instance = AWSFlavour.from_json(json)
# print the JSON string representation of the object
print(AWSFlavour.to_json())

# convert the object into a dict
aws_flavour_dict = aws_flavour_instance.to_dict()
# create an instance of AWSFlavour from a dict
aws_flavour_from_dict = AWSFlavour.from_dict(aws_flavour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


