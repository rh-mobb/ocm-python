# AWSVolume

Holds settings for an AWS storage volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iops** | **int** | Volume provisioned IOPS. | [optional] 
**size** | **int** | Volume size in Gib. | [optional] 

## Example

```python
from ocm_client.models.aws_volume import AWSVolume

# TODO update the JSON string below
json = "{}"
# create an instance of AWSVolume from a JSON string
aws_volume_instance = AWSVolume.from_json(json)
# print the JSON string representation of the object
print(AWSVolume.to_json())

# convert the object into a dict
aws_volume_dict = aws_volume_instance.to_dict()
# create an instance of AWSVolume from a dict
aws_volume_from_dict = AWSVolume.from_dict(aws_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


