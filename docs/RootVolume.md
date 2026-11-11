# RootVolume

Root volume capabilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**AWSVolume**](AWSVolume.md) |  | [optional] 
**gcp** | [**GCPVolume**](GCPVolume.md) |  | [optional] 

## Example

```python
from ocm_client.models.root_volume import RootVolume

# TODO update the JSON string below
json = "{}"
# create an instance of RootVolume from a JSON string
root_volume_instance = RootVolume.from_json(json)
# print the JSON string representation of the object
print(RootVolume.to_json())

# convert the object into a dict
root_volume_dict = root_volume_instance.to_dict()
# create an instance of RootVolume from a dict
root_volume_from_dict = RootVolume.from_dict(root_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


